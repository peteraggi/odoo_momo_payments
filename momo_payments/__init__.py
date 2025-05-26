from . import controllers
from . import models


from odoo.addons.payment import setup_provider, reset_payment_provider

# Post-init hook to set up the payment provider
def post_init_hook(env):
    setup_provider(env, 'mtn_momo')

# Uninstall hook to reset the payment provider
def uninstall_hook(env):
    reset_payment_provider(env, 'mtn_momo')