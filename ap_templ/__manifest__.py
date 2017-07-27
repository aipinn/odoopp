# -*- coding: utf-8 -*-
{
    'name': "ap_templ",

    'summary': """
        创建模板""",

    'description': """
        这是一个模板
    """,

    'author': "peng",
    'website': "http://www.e3rong.com:8069",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',
    'sequence':'2',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/ap_templ.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}