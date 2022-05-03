# -*- coding: utf-8 -*-
{
    'name': 'Marketplace Connector',
    'version': '0.1',
    'category': 'Sales',
    'summary': 'Integration: Shopify, Shopee, Lazada, Qoo10, Tokopedia',
    'description': 'Integrate global online marketplaces & web-stores with Odoo. Sync products, inventory and orders from multiple channels',
    'author': 'Jonathan Lim',
    'website': 'http://babyjugger.freehostia.com/',
    'license': 'OPL-1',
    'support': 'Jonathan.Lim@Omnisoftsolution.com',

    # any module necessary for this one to work correctly
    'depends': ['stock', 'sale_management', 'account'],

    # always loaded
   'data': [

        # Security 
        'security/ir.model.access.csv',
        'security/marketplace_security.xml',

        # Views
        'views/icon.xml',
        'views/menu.xml',
        'views/action.xml',

        # Data



    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/images/banner.jpg'],
    "installable": True,
    'application': True,
    'auto_install': False,
}
