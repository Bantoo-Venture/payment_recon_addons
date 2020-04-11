from __future__ import unicode_literals
import frappe, erpnext
from frappe.utils import flt, today
from frappe import msgprint, _
from frappe.model.document import Document
from erpnext.accounts.utils import (get_outstanding_invoices,
	update_reference_in_payment_entry, reconcile_against_document)
from erpnext.controllers.accounts_controller import get_advance_payment_entries


@frappe.whitelist()
def get_unnallocated_parties(doctype, txt, searchfield, start, page_len, filters):

	company = filters["company"]
	party_type = filters["party_type"]
	bank_cash_account = filters["bank_cash_account"]
	receivable_payable_account = filters["receivable_payable_account"]

	dr_or_cr = ("credit_in_account_currency" if erpnext.get_party_account_type(party_type) == 'Receivable'
		else "debit_in_account_currency")

	bank_account_condition = ("t2.against_account like %(bank_cash_account)s" if bank_cash_account else "1=1")

	limit_cond = "limit 100";

	paid_parties = frappe.db.sql("""
		select
			DISTINCT party
		from
			`tabJournal Entry` t1, `tabJournal Entry Account` t2
		where
			t1.name = t2.parent and t1.docstatus = 1 and t2.docstatus = 1
			and t2.party_type = %(party_type)s
			and t2.account = %(account)s and {dr_or_cr} > 0
			and (t2.reference_type is null or t2.reference_type = '' or
				(t2.reference_type in ('Sales Order', 'Purchase Order')
					and t2.reference_name is not null and t2.reference_name != ''))
			and (CASE
				WHEN t1.voucher_type in ('Debit Note', 'Credit Note')
				THEN 1=1
				ELSE {bank_account_condition}
			END)
		order by t1.posting_date {limit_cond}
		""".format(**{
			"dr_or_cr": dr_or_cr,
			"bank_account_condition": bank_account_condition,
			"limit_cond": limit_cond
		}), {
			"party_type": party_type,
			"account": receivable_payable_account,
			"bank_cash_account": "%%%s%%" % bank_cash_account
		}, as_dict=0)

	unreconciled_parties = []
	condition = ""

	for party in paid_parties:
		invoices = get_outstanding_invoices(party_type, party,
						receivable_payable_account, condition=condition)
		if invoices:
			unreconciled_parties.append(party)

	return unreconciled_parties