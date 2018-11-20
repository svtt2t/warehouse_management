from odoo import api, models, fields


class DinhPham(models.Model):
    _name = 'supplies'

    name = fields.Char(string="Name", required=True)
    code = fields.Char()
    compute_name = fields.Char(compute='_compute_name')
    group_supplies = fields.Many2one('groupsupplies')


    @api.depends('name', 'code')
    def _compute_name(self):
        if self.code and self.name:
            self.compute_name = self.code + ' - ' + self.name
