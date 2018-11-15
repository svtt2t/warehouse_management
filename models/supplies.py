from odoo import api, models,  fields

class DinhPham(models.Model):
    _name = 'supplies'

    name = fields.Char(string="Name", required=True)
    code = fields.Text()
