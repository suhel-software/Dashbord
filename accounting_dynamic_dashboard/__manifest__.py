{
    'name': 'Accounting Dynamic Dashboard',
    'version': '18.0.1.13',
    'summary': 'Custom Dashboard for Bank and Cash with merged balances',
    'description': """
This module completely revamps the standard Odoo Accounting Dashboard. It introduces a highly dynamic, beautifully styled Kanban interface with custom animations, soft shadows, and clean gradients for the best user experience. Developed by Imran Hoque.
    """,
    'author': 'Imran Hoque',
    'depends': ['account', 'at_accounting'],
    'data': [
        'views/dashboard_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'accounting_dynamic_dashboard/static/src/css/dashboard.css',
        ],
    },
    'images': [
        'static/description/screenshot_clean1.png',
        'static/description/screenshot_clean2.png',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
