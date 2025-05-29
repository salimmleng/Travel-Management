# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'report_delivery',
    'author': 'Salim Hossain',
    'summary': 'Report Delivery',
    'depends': ['base','product','sale'],
    'description': "Hello",
    'data': [
        'views/report_views.xml',
        'views/sales_order_inherit_cartoon.xml',
        'reports/delivery_report_inherit.xml',
        'reports/invoice_report_inherit.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',

}
    
