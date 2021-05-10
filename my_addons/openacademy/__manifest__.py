# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
       This an project management about courses""",

    'description': """
        Long description of module's purpose
    """,

    'author': "salama",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base_setup'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/openacademy.xml',
        'views/partner.xml',
    #'views/templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
