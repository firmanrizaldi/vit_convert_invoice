#-*- coding: utf-8 -*-

{
	"name": "Convert invoice",
	"version": "1.0", 
	"depends": [
		'base','account','sale', 'om_account_accountant'
	],
	"author": "Akhmad D. Sembiring [vitraining.com]",
	"category": "Utility",
	"website": "http://vitraining.com",
	"images": ["static/description/images/main_screenshot.jpg"],
	"price": "10",
	"license": "OPL-1",
	"currency": "USD",
	"summary": "This is the Convert invoice module generated by StarUML Odoo Generator Pro Version",
	"description": """

Information
======================================================================

* created menus
* created objects
* created views
* logics

""",
	"data": [
		"security/ir.model.access.csv",
		"data/group.xml",
		"data/product.xml",
		"view/menu.xml",
		"view/convert_invoice.xml",
		"report/convert_invoice.xml",
	],
	"installable": True,
	"auto_install": False,
	"application": True,
}