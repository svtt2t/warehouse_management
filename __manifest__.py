# -*- coding: utf-8 -*-
{
    'name': 'Warehouse',
    'description': 'Warehouse management',
    'summary': 'Warehouse',
    'category': 'Warehouse',
    "sequence": 2,
    'version': '1.0.0',
    'author': 'PhamDinh',
    'website': 'https://www.facebook.com/phamdinh442',
    'depends': ['base'],
    'data': [
        'views/views'
        'views/abc.xml'
        'views/warehouse_management_views.xml',
	    'menu/warehouse_management_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}