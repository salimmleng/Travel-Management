# -*- coding: utf-8 -*-
{
    'name': "Hospital Management System",
    'author':'Walmut Software Solutions',
    'license': 'LGPL-3',
    'version': '17.0.1.1',
    'depends':[
        'mail','product',
    ],
    'data':[
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/patient_views.xml',
        'views/patient_readonly_views.xml',
        'views/appointment_views.xml',
        'views/patient_tag_views.xml',
        'views/appointment_line_views.xml',
        'views/menu.xml',
        
    ]
   
}

