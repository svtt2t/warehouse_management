# -*- coding: utf-8 -*-
{
    'name': 'Category',
    'description': 'Warehouse management',
    'summary': 'Warehouse',
    'category': 'Warehouse',
    "sequence": 1,
    'version': '1.0.0',
    'author': 'Nam,Minh,Dinh',
    'website': 'https://www.facebook.com/bechoibebo',
    'depends': ['base'],
    'data': [
        'views/supplies_views.xml',
        'views/warehouse_views.xml',
        'views/groupsupplies_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
