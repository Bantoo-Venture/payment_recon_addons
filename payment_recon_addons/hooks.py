# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "payment_recon_addons"
app_title = "Payment Recon Addons"
app_publisher = "Bantoo & Jenny Intenet"
app_description = "Enhancements to ERPNexts Payment Reconciliation Feature"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "dev@thebantoo.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/payment_recon_addons/css/payment_recon_addons.css"
# app_include_js = "/assets/payment_recon_addons/js/payment_recon_addons.js"

# include js, css files in header of web template
# web_include_css = "/assets/payment_recon_addons/css/payment_recon_addons.css"
# web_include_js = "/assets/payment_recon_addons/js/payment_recon_addons.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "payment_recon_addons.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "payment_recon_addons.install.before_install"
# after_install = "payment_recon_addons.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "payment_recon_addons.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"payment_recon_addons.tasks.all"
# 	],
# 	"daily": [
# 		"payment_recon_addons.tasks.daily"
# 	],
# 	"hourly": [
# 		"payment_recon_addons.tasks.hourly"
# 	],
# 	"weekly": [
# 		"payment_recon_addons.tasks.weekly"
# 	]
# 	"monthly": [
# 		"payment_recon_addons.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "payment_recon_addons.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "payment_recon_addons.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "payment_recon_addons.task.get_dashboard_data"
# }

