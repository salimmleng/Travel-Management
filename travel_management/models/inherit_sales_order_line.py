from odoo import models, fields,api

class SaleOrderLineInherit(models.Model):

    _inherit = 'sale.order.line'

    employee_id = fields.Many2one('employee.info', string='Employee')



