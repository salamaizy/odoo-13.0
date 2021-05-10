# -*- coding: utf-8 -*-
{
    'name': "hotel",

    'summary': """
        This is hotel management that I created so thanks to me""",

    'description': """
        purpose Hotel popose Babe
    """,

    'author': "SALAMA",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hotel',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base_setup'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
