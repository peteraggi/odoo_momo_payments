# 🌐 Odoo MTN Mobile Money (MoMo) Payment Gateway

Seamlessly integrate MTN's Mobile Money payments into your Odoo eCommerce platform with this professional module. Accept secure mobile payments directly through your Odoo Community Edition without requiring an Enterprise license.

## ✨ Key Features

- **End-to-End Payment Processing**: Complete MoMo transactions within Odoo's native interface
- **Dual Environment Support**: Test in sandbox mode before going live
- **Real-Time Verification**: Automatic payment confirmation and reconciliation
- **Omnichannel Compatibility**: Works with:
  - Odoo eCommerce storefronts
  - Customer portal invoices
  - Payment links
- **Secure API Integration**: PCI-compliant connection to MTN's mobile money platform

## 📋 Prerequisites

- Odoo Community Edition (v17+ recommended)
- Active MTN MoMo merchant account
- Valid API credentials from MTN
- Server with internet access to connect to MTN APIs

## 🚀 Getting Started

### Official MoMo Onboarding

1. **Apply for Live Account**:  
   Visit [MTN Developer Portal](https://momodeveloper.mtn.com/golive)  
   → Select your operating country  
   → Choose "CollectionsProduct" (minimum requirement)

2. **Complete Registration**:  
   Submit all required business documentation  
   Wait for MTN approval (typically 2-5 business days)

3. **Obtain API Credentials**:  
   - Subscription Key  
   - API User ID  
   - API Primary Key  
   *(Contact aggipeter25@gmail.com for setup assistance if needed)*

## 🛠 Installation Guide

# Clone repository to your custom addons directory
git clone https://github.com/yourusername/odoo_momo_payments.git

# Add path to odoo.conf
addons_path = /path/to/your/custom/addons

# Update Odoo modules
./odoo-bin -u all -d your_database_name
# Odoo MTN Mobile Money Integration Guide

## Post-Installation Steps

1. **Enable Developer Mode** in your Odoo instance
2. **Update Apps List** to refresh available modules
3. Search for **"MTN MoMo Payments"** in the Apps menu
4. Click **Install** to activate the module

---

## ⚙ Configuration Settings

### Access Path:
`Invoicing → Configuration → Payment Acquirers → MTN MoMo`

### Core Configuration Options:

**Provider State:**
- 🧪 **Test Mode**: Sandbox environment with auto-generated credentials
- ✅ **Enabled**: Live transaction mode (requires complete credentials)
- ❌ **Disabled**: Deactivates the payment provider

**Authentication Credentials:**
- 🔑 **Secret Key** (Mandatory for all modes)
- 👤 **API User UUID** (Required for live production only)
- 🔐 **API Primary Key** (Required for live production only)

**Financial Setup:**
- 📒 Create/assign a dedicated **Payment Journal** for MoMo transactions

---

## 🔄 Payment Processing Flow

### eCommerce Checkout Process:
1. Customer selects **"MTN MoMo"** as payment method
2. Enters registered mobile number
3. Confirms payment amount
4. Receives push notification on MoMo app
5. Approves transaction → Instant Odoo confirmation
6. Order status updates to **Paid** automatically

### Invoice Payment Process:
1. Customer accesses payment link
2. Completes same MoMo verification steps
3. Real-time invoice status synchronization

---

## ⏱ Technical Implementation Details

**Payment Initialization:**
- Triggers RTP API call upon "Pay Now" action

**Status Verification:**
- System polls payment status every **3 seconds**
- Maximum **20 retries** (60 second total timeout)

**Transaction Management:**
- Detailed logging of all transaction attempts
- Automatic journal entry generation
- Success/Failure status tracking for reconciliation

---

## 🆘 Support Services

For technical assistance or custom development requests:
📧 **Email:** [aggipeter25@gmail.com](mailto:aggipeter25@gmail.com)

---

## 📜 License Agreement

```sql
Copyright (C) 2024 aggipeter25

Licensed under Odoo Proprietary License v1.0

Key Provisions:
- Valid license required for operational use
- Modification rights granted
- Redistribution prohibited
- No expressed warranties
- Commercial use permitted with proper licensing
