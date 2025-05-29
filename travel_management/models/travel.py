from odoo import api, fields, models
from odoo.exceptions import ValidationError


class TravelPackage(models.Model):
    _name = 'travel.package'
    _description = 'Travel Package'

    name = fields.Char(string='Package Title', required=True)
    description = fields.Text(string='Description')
    destination = fields.Char(string='Destination', required=True)
    package_type = fields.Selection([
        ('domestic', 'Domestic'),
        ('international', 'International'),
        ('adventure', 'Adventure'),
        ('honeymoon', 'Honeymoon'),
    ], string='Type', required=True)
    duration_days = fields.Integer(string='Duration (Days)', required=True)
    price = fields.Float(string='Price', required=True)
    image = fields.Binary(string='Image')
    is_active = fields.Boolean(default=True)




class TravelBooking(models.Model):
    _name = 'travel.booking'
    _description = 'Travel Booking'

    customer_id = fields.Many2one('employee.info', string='Employee', required=True)
    package_id = fields.Many2one('travel.package', string='Package', required=True)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.today)
    travel_date = fields.Date(string='Travel Date', required=True)
    num_people = fields.Integer(string='Number of People', default=1)
    total_price = fields.Float(string='Total Price', compute='_compute_total_price', store=True)
    status = fields.Selection([
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed')
    ], default='pending', string='Status')


    # Api depends
    @api.depends('num_people', 'package_id.price')
    def _compute_total_price(self):
        for rec in self:
            rec.total_price = rec.num_people * rec.package_id.price


    # Api onchange
    @api.onchange('num_pepple','package_id')
    def _onchange_total_price(self):
        if self.package_id and self.num_people:
            self.total_price = self.num_people * self.package_id.price
        else:
            self.total_price = 0.0



    # Api contraint
    @api.constrains('travel_date')
    def _check_travel_date(self):
        for rec in self:
            if rec.travel_date < fields.Date.today():
                raise ValidationError("Travel date cannot be in the past.")




