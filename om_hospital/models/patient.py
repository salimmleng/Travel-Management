from odoo import models, fields,api
from odoo.exceptions import UserError, ValidationError

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'Patient Master'


    name = fields.Char(string='Name',required = True, tracking= True)
    date_of_birth  = fields.Date(string='DOB')
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender')

    tag_ids = fields.Many2many(
        'patient.tag', string="tags"
    )

    
    # Ondelete using decorator
    
    @api.ondelete(at_uninstall=False)
    def _check_patient_appointments(self):
        for rec in self:
            domain=[('patient_id','=', rec.id)]
            appointments= self.env['hospital.appointment'].search(domain)
            if appointments:
                raise ValidationError("You can not delete the  patient now, Appointments existing for the patient.")


    # def unlink(self):
    #     for rec in self:
    #         domain=[('patient_id','=', rec.id)]
    #         appointments= self.env['hospital.appointment'].search(domain)
    #         if appointments:
    #             raise ValidationError("You can not delete the  patient now, Appointments existing.")

    #     return super().unlink()
    


    



