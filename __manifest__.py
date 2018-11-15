# -*- coding: utf-8 -*-
{
    'name': Warehouse management
    'description': 'Warehouse management',
    'summary': 'Warehouse',
    'category': 'Warehouse',
    "sequence": 2,
    'version': '1.0.0',
    'author': 'Nam Nam',
    'website': 'https://www.facebook.com/bechoibebo',
    'depends': ['base'],
    'data': [
        'views/ab.xml',
        'views/warehouse_views.xml',
        'views/groupsupplies_views.xml',
	    'menu/warehouse_management_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}