# -*- coding: utf-8 -*-
{
    'name': "travel_management",

    'summary': "Travel Information",
    'author': "Salim Hossain",
    'depends': ['base','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_views.xml',
        'views/travel_booking_views.xml',
        'views/travel_package_views.xml',  
        'views/sales_order_inherit.xml',
        'views/cronjob_views.xml',  

    ],
    
}

