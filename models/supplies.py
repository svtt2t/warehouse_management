from odoo import api, models,  fields

class Warehouse_Management(models.Model):
    _name = 'VatTu'
    code = fields.Text()
    name = fields.Char(string="Name", required=True)
