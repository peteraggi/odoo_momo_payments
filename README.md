# Odoo MTN Mobile Money (MoMo) Payments Integration

This module integrates **MTN Mobile Money (MoMo)** with the **Odoo Community Edition**. It allows you to receive payments seamlessly through MoMo on your **Odoo E-commerce website** and **Customer Portal**.

---

## 🌟 Features

- Accept payments via MTN MoMo directly on your Odoo site
- Integrates with Odoo's sales orders and customer invoices
- Real-time payment confirmation
- Works with Odoo Community Edition (no Enterprise license required)
- Clean and secure API integration

---

## 🛠️ Requirements

- Odoo Community Edition (17 or v18 recommended)
- MTN MoMo Merchant Account (with API credentials)
- Internet access for server to reach MTN MoMo APIs

---

## 📦 Installation

1. **Download or clone** this module into your custom addons directory:
   ```bash
   git clone https://github.com/yourusername/odoo_momo_payments.git
Edit your odoo.conf to include the path to your custom addons:

ini
Copy
Edit
addons_path = /path/to/your/custom/addons
Restart your Odoo server:

bash
Copy
Edit
./odoo-bin -u all -d your_database_name
Activate Developer Mode, go to Apps, click Update App List, search for MTN MoMo Payments, and click Install.

⚙️ Configuration
Navigate to Invoicing → Configuration → Payment Acquirers

Click on MTN MoMo

Enable the acquirer by setting the status to Enabled

Fill in the required fields:

Subscription Key

API User ID

API Primary Key

Target Environment (sandbox or production)

Configure journal and callback URL

Save and test the connection.

🚀 Usage
Customers will now see MTN MoMo as a payment option during checkout or when paying an invoice

They enter their phone number and confirm the MoMo push request on their phone

Once payment is successful, Odoo marks the order/invoice as paid

🙋‍♂️ Support & Setup Assistance
For help with installation, configuration, or custom features, please contact:

📧 aggipeter25@gmail.com

🧾 License
This software and its source code are provided under the Odoo Proprietary License v1.0:

pgsql
Copy
Edit
Copyright (C) 2024-present by aggipeter25

This software and associated files (the "Software") may only be used (executed,
modified, executed after modifications) if you have purchased a valid license
from the author.

You may develop Odoo modules based on the Software and distribute them under
the license of your choice, provided that it is compatible with the terms of
this License.

It is forbidden to publish, distribute, sublicense, or sell copies of the
Software or modified copies of the Software.

The above copyright notice and this permission notice must be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
USE OR OTHER DEALINGS IN THE SOFTWARE.
🧠 Credits
Developed and maintained by aggipeter25

🔗 Stay Updated
To receive future updates, request a demo, or discuss partnership opportunities:

📧 aggipeter25@gmail.com
