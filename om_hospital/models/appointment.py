from odoo import models, fields,api

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread']
    _description = 'Hospital Appointment'
    _rec_names_search = ['reference', 'patient_id']     # eta deyer fole ami reference and patient id diye search korle tar record paye jabo
    _rec_name = 'patient_id'

    reference = fields.Char(string='Reference', default = 'New')
    patient_id = fields.Many2one('hospital.patient', string='Patient', ondelete="restrict")

    # on delete restrict holo patient er name jodi kono appointment thake tahole patient delete kora jabe na , validation error dibe
    # ondelete cascade holo patient er name appointment thakle seta soho patient delete hoye jabe
    date_appointment = fields.Date(string='Date')
    note = fields.Text(string='Note')
    state = fields.Selection(
        [('draft',"Draft"),
         ('confirmed','Confirmed'),
         ('ongoing', 'Ongoing'),
         ('done',"Done"),
         ('cancelled','Cancelled')
        ], default="draft")
    
    appointment_line_ids = fields.One2many('hospital.appointment.line','appointment_id', string='Lines')
    total_qty = fields.Float(compute ='_compute_total_quantity', string='Total Quantity', store = True)
    date_of_birth = fields.Date(string='DOB', related ='patient_id.date_of_birth')


    # store = True dile api depends decorator use korte hobe cause odoo jante cai kon kon field aber recompute korte hobe

    @api.model_create_multi
    def create(self,vals_list):
        print('odoo mates', vals_list)
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
                

        return super().create(vals_list)
    


    @api.depends('appointment_line_ids', 'appointment_line_ids.qty')
    def _compute_total_quantity(self):
        print("test",self)   # here self holo onek gulo data record set
        for rec in self:
            # total_qty = 0
            # print("test2",rec.appointment_line_ids)    # rec holo ekta data recordset
            # for line in rec.appointment_line_ids:
            #     print("line value",line.qty)
            #     total_qty = total_qty + line.qty   # 42 line er total_qty  38 line er declare kora total_qty ke update korse
            rec.total_qty = sum(rec.appointment_line_ids.mapped("qty"))   # uporer puro loop ta ek line e kora holo
            

    
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"[{rec.reference}] {rec.patient_id.name}"
    
    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'
            

    def action_ongoing(self):
        for rec in self:
            rec.state = 'ongoing'
    
    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'


class HospitalAppointmentLine(models.Model):
    _name = 'hospital.appointment.line'
    _description = 'Appointment Line'


    appointment_id = fields.Many2one('hospital.appointment',string="Appointment")
    product_id = fields.Many2one('product.product', string='Product')
    qty = fields.Float(string='Quantity')

