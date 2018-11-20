from odoo import api, models, fields


class Namnam(models.Model):
    _name = 'warehouse_management'

    code = fields.Char(string="Code Warehouse", required=True)
    name = fields.Char(string="Name Warehouse", required=True)
