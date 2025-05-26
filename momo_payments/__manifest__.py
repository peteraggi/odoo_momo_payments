{ 
    #innitialize the module
    'name': "MTN Mobile money Odoo Payments",
    'summary': "Mobile Money Odoo Payments",
    'description': """ Mobile Money Odoo Payments  """,
    'author': "Scintl Technologies",
    'website': "https://www.scintl.co.ug",

    'version': '17.0.0.1',
    'category': 'Accounting/Payment Providers',
    'sequence': 250,
    'support': 'support@scintl.co.ug',
    'live_test_url': 'https://scintl.co.ug/contactus',
    'depends': ['payment', 'website_sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/payment_templates.xml',
        'data/payment_provider_data.xml',
        
    ],
    'assets': {
        'web.assets_frontend': [
            # 'mtn_momo/static/src/js/mtn_momo.js',
        ],
    },
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'license': 'LGPL-3',
}