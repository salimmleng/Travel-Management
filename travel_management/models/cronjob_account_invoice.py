from odoo import models, api

class AccountInvoice(models.Model):
    _inherit = 'account.move'

    @api.model
    def delete_old_drafts(self):
        old_drafts = self.search([('state', '=', 'draft')])
        old_drafts.unlink()
        print("Old drafts deleted!")
