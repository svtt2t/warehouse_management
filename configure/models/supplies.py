from odoo import api, models, fields


class supplies(models.Model):
    _name = 'vnitpro.supplies'

    code = fields.Char("Code Supplies", required=True)
    name = fields.Char("Name Supplies", required=True)
    group_supplies = fields.Many2one('vnitpro.groupsupplies')
    compute_name = fields.Char('Compute Name')

    @api.depends('code', 'name')
    def _compute_name(self):
        if self.code and self.name:
            self.compute_name = self.code + ' - ' + self.name
