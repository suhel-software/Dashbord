# Accounting Dynamic Dashboard

## Overview
**Accounting Dynamic Dashboard** is a premium, custom UI enhancement module for Odoo 18. It replaces the standard Odoo Invoicing/Accounting dashboard with a more visually appealing, modern, and dynamic dashboard designed specifically for Bank, Cash, Sale, and Purchase journals.

## Author
**Imran Hoque**

## Technical Specifications
- **Module Name (Technical):** `accounting_dynamic_dashboard`
- **Version:** 18.0.1.12
- **Depends:** `account`, `at_accounting`

## Key Features
1. **Premium Aesthetics (UI/UX):**
   - Applies modern CSS styling to the Kanban cards including soft shadows, rounded corners, and a clean background.
   - Smooth hover micro-animations that lift the cards upon mouse interaction, creating a dynamic user experience.
   - Beautiful linear-gradient background added to the graph sections to make data visualization pop.
   
2. **Simplified Navigation:**
   - Overrides the default accounting menu to automatically display this custom dashboard upon entering the Accounting application.
   - Removes unnecessary breadcrumb text (like the duplicate "Dashboard" title next to the search bar) via targeted CSS to maintain a clean workspace.

3. **Custom Journal Filtering:**
   - Adds custom fields (`custom_dashboard_visibility` and `sequence`) to the `account.journal` model to strictly control which journals appear on this dashboard.

## Installation & Configuration
1. Place the `accounting_dynamic_dashboard` folder into your Odoo custom addons directory.
2. Restart the Odoo server.
3. Go to the **Apps** menu, click "Update Apps List", and search for "Accounting Dynamic Dashboard".
4. Click **Install**.
5. Once installed, simply open your **Accounting** app. The new dashboard will load by default.

## Note
This module is strictly dependent on `at_accounting`. If installing on a fresh database, ensure that the `at_accounting` module is available in your addons path, as it relies on its root menu structure.
