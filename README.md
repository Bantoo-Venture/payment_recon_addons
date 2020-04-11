## Payment Reconciliation Enhancement

Enhancements to ERPNexts Payment Reconciliation Feature
- 

#### Setup

- Open your bench cli

```cd ~/<bench_dir>```

- Get the app

```bench get-app payment_recon_addons https://github.com/Bantoo-Venture/payment_recon_addons.git```

- Install to your site

```bench --site <site_name> install-app payment_recon_addons```

- Add the javascript to your Payment Reconciliation

```
// add this to 
// erpnext/erpnext/accounts/doctype/payment_reconciliation/payment_reconciliation.js
// before party: function() {

party_type: function() {
		var me = this;
		const the_query = "payment_recon_addons.api.get_unnallocated_parties";
		
		if(!me.frm.doc.receivable_payable_account && me.frm.doc.party_type) {

			me.frm.set_query('party', function(){
				return {
					query: the_query,
					filters: {
						company: me.frm.doc.company,
						party_type: me.frm.doc.party_type,
						bank_cash_account: me.frm.doc.bank_cash_account,
						receivable_payable_account: me.frm.doc.receivable_payable_account
					}
				}
			});
		}
	},
  
```

##### Recommended Changes
- Move position of party field to the bottom
- Make Bank Field Mandatory

#### Down the pipeline
- Add to core
- Pull defaults
  - Company onload
  - Payable / Receivable Account on selection of Party Type

#### License

MIT
