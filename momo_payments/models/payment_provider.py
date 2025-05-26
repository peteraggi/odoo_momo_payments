
from odoo import _, api, fields, models
from odoo.addons.momo_payments import const  # Create this constants file

class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('mtn_momo', "mtn_momo")], ondelete={'mtn_momo': 'set default'}
    )
    mtn_public_key = fields.Char(
        string="MTN Public Key",
        help="Public key for encrypting MTN API payloads",
        required_if_provider='mtn_momo',
    )
    mtn_api_key = fields.Char(
        string="MTN API Key",
        required_if_provider='mtn_momo',
        groups='base.group_system',
    )
    mtn_client_id = fields.Char(
        string="MTN Client ID",
        required_if_provider='mtn_momo',
        groups='base.group_system',
    )
    mtn_subscription_key = fields.Char(
        string="MTN Subscription Key",
        required_if_provider='mtn_momo',
        groups='base.group_system',
    )
    mtn_base_url = fields.Char(
        string="MTN API Base URL",
        default="https://sandbox.momodeveloper.mtn.com",  # Sandbox URL
        required_if_provider='mtn_momo',
        groups='base.group_system',
    )
    mtn_environment = fields.Selection(
        [('sandbox', 'Sandbox'), ('production', 'Production')],
        string="Environment",
        default='sandbox',
        # required=True
    )
    mtn_currency = fields.Char(
        string="Currency",
        default='UGX',
        # readonly=True
    )

    # ====== HELPER METHODS ====== #
    def format_uganda_phone_number(self, phone):
        """Format UG phone numbers to MTN Momo format (256...)"""
        phone = re.sub(r'\D', '', str(phone))  # Remove non-digits
        if phone.startswith('0'):
            return '256' + phone[1:]
        elif phone.startswith('256'):
            return phone
        else:
            return '256' + phone  # Default assumption
    # ====== MORE LOGIC WILL COME IN DOWN HERE IN ASHORT TIME FROM NOW====== #