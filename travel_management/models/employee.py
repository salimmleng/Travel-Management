from odoo import models, fields

class Employee(models.Model):
    _name='employee.info'
    _description="employee information"

    name = fields.Char(string='Employee Name', required=True)
    phone = fields.Integer(string='Phone')
    address = fields.Char(string='Address')


    def action_create_record(self):
        new_employee = self.env['employee.info'].create({
            'name': 'Korim uddin',
            'phone': 123456,
            'address': 'Mohammadpur'
        })
        print(f"Created Employee: {new_employee.name}, ID: {new_employee.id}")


    def action_write_record(self):
        for rec in self:
            rec.write({
                'address': 'Adabor'
            })
            print(f"Updated Employee ID {rec.id}: Address changed to {rec.address}")


    def action_unlink_record(self):
        for rec in self:
            print(f"Deleting Employee ID {rec.id} - Name: {rec.name}")
            rec.unlink()


    def action_browse_record(self):
        emp = self.env['employee.info'].browse(3)
        if emp.exists():
            emp.address = 'Browsed address'
            print(f"Browsed Employee ID {emp.id}: Address updated to {emp.address}")
        else:
            print(f"No employee found with ID {emp.id}")



    def action_search_record(self):
        employees = self.env['employee.info'].search([('name', '=', 'Rana hossain')])
        for emp in employees:
            emp.address = 'Address Found by Search'

            print(f"Searched Employee ID {emp.id} address to: {emp.address}")

 


    def action_search_count(self):
        count = self.env['employee.info'].search_count([('name', '!=', False)])
        print("Total Employees:", count)



    def action_copy_record(self):
        if self:
            new_copy = self.copy()
            print("Copied Employee:", new_copy.name)


    def action_read_fields(self):
        records = self.env['employee.info'].search([], limit=3)
        data = records.read(['name', 'phone'])
        print('Read data', data)


    def action_check_exists(self):
        if self.exists():
            print(f"{self.exists}, exists")
        else:
            print('Record does not exists.')

