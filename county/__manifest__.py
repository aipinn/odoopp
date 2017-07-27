# -*- coding: utf-8 -*-
{
    'name': "county",

    'summary': """
        这是county的简介""",

    'description': """
        关于此模块的描述
    """,
    'sequence':'0',
    'author': "PNEG",
    'website': "http://www.e3rong.com:8069",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',

        'views/county_province_view.xml',
        'sequence.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}