# -*- coding: utf-8 -*-
{
    'name': 'Pune Gas',
    'category': 'Pune Gas ',
    'version': '18.0.0.0',
    'summary': 'Custom Odoo Features',    
    'description': """Custom Odoo Features""",
    'depends': [
        'base',
        'stock',
        'sale_management',
        'purchase',
    ],
    'data': [
        'report/sale_order_templates.xml',
    ],
    'assets': {
        # 'web.assets_frontend': [
        # ],
        "web.assets_backend": [
            'pune_gas/static/src/js/section_wise_subtotal.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}