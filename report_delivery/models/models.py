from odoo import models, fields,api

class ProductProductInherit(models.Model):
    _inherit = 'product.product'

    cartoon_capacity = fields.Integer(string="Cartoon Capacity")



class ResCompany(models.Model):
    _inherit = 'res.company'

    qr_image = fields.Binary("QR Code Image")



class SaleOrderLineCartoon(models.Model):
    _inherit = 'sale.order.line'

    carton_qty = fields.Float(string='Carton Quantity', compute='_compute_carton_qty', store=True)
    
    @api.depends('product_uom_qty', 'product_id')
    def _compute_carton_qty(self):
        for line in self:
            if line.product_id and line.product_id.cartoon_capacity:
                line.carton_qty = line.product_uom_qty / line.product_id.cartoon_capacity
            else:
                line.carton_qty = 0




class SaleOrderLineDiscount(models.Model):
    _inherit = 'sale.order.line'

    discount_amount = fields.Monetary(
        string="Discount Amount",
        compute="_compute_discount_amount",
        store=True,
        currency_field='currency_id'
    )

    @api.depends('price_unit', 'product_uom_qty', 'discount')
    def _compute_discount_amount(self):
        for line in self:
            line.discount_amount = (line.price_unit * line.product_uom_qty) * (line.discount / 100)