from odoo import api, models, fields


class DinhPham(models.Model):
    _name = 'supplies'

    code = fields.Char(string="Code Supplies", required=True)
    name = fields.Char(string="Name Supplies", required=True)
    group_supplies = fields.Many2one('groupsupplies')
    # importsupplies_id = fields.Many2one('importsupplies', string="importsupplies")
