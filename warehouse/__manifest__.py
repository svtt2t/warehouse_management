# -*- coding: utf-8 -*-
{
    'name': 'Warehouse Management',
    'description': 'Warehouse management',
    'summary': 'Warehouse',
    'category': 'Warehouse',
    "sequence": 1,
    'version': '1.0.0',
    'author': 'Nam Nam',
    'website': 'https://www.facebook.com/bechoibebo',
    'depends': ['configure'],
    'data': [
        'views/exportingsupplies_views.xml',
        'views/importsupplies_views.xml',
        'menu/warehouse_management_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
