
# This file is part of the Momo Payments module for Odoo.
# It defines constants used throughout the module.
# Developed and Mastered by Peter Aggi
# Scintl Technologies
SUPPORTED_CURRENCIES = [
    'UGX',
]

#APIKEY: 
#CLEINTID: 
#PUBLIC_KEY:

# Mapping of transaction states to momo payment statuses.
PAYMENT_STATUS_MAPPING = {
    'pending': ['pending auth'],
    'done': ['successful'],
    'cancel': ['cancelled'],
    'error': ['failed'],
}
