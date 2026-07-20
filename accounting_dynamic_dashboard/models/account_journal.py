from odoo import models, fields

class AccountJournal(models.Model):
    _inherit = 'account.journal'

    custom_dashboard_visibility = fields.Boolean(
        string='Show on Custom Dashboard',
        default=True,
        help="Check this box to show this journal on the custom Bank, Cash, Sales & Purchase Dashboard."
    )

    def _fill_bank_cash_dashboard_data(self, dashboard_data):
        super()._fill_bank_cash_dashboard_data(dashboard_data)
        if not self.env.context.get('is_custom_dashboard'):
            return
            
        for journal in self.filtered(lambda j: j.type in ('bank', 'cash')):
            if not journal.default_account_id:
                continue
            
            currency = journal.currency_id or journal.company_id.currency_id
            
            domain = [
                ('account_id', '=', journal.default_account_id.id),
                ('parent_state', '=', 'posted'),
                ('company_id', 'in', self.env.companies.ids)
            ]
            res = self.env['account.move.line']._read_group(
                domain,
                [],
                ['balance:sum']
            )
            true_balance = res[0][0] if res else 0.0

            dashboard_data[journal.id]['account_balance'] = currency.format(true_balance)
            dashboard_data[journal.id]['nb_misc_operations'] = 0
            dashboard_data[journal.id]['misc_operations_balance'] = None
