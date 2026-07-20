from odoo import http

class DashboardBanner(http.Controller):
    @http.route('/ag_bank_cash_dashboard/banner', type='json', auth='user')
    def dashboard_banner(self):
        return {
            'html': '''
            <div style="text-align: center; width: 100%; padding: 15px 0 5px 0;">
                <h2 style="font-weight: bold; color: #016b8b; font-size: 2.2rem; margin: 0;">Accounting Dashboard</h2>
            </div>
            '''
        }
