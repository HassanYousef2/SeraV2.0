# -*- coding: utf-8 -*-
{
    'name': "Techscope Warehouse Passowrd",

    'summary': """
        Techscope Warehouse Passowrd""",

    'description': """
        Techscope Warehouse Passowrd
    """,

    'author': "Abdulrahman Rabie, TechScope Team",
    'website': "http://techscopeco.com/",

    'category': 'stock',
    'version': '14.0.1',

    'depends': ['base','web','stock',],

    'data': [

        # 'security/ir.model.access.csv',
        'views/webclient_templates.xml',
        'views/stock_warehouse.xml',
        'views/stock_picking.xml',
        # 'views/aug_batch.xml',
        # 'views/aug_step.xml',
        # 'views/sale_order.xml',
        # 'views/product.xml',
        # 'wizard/aug_wizard.xml',
    ],
    'demo': [

    ],
}
