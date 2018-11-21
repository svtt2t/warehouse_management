from odoo import api, models, fields


class supplies(models.Model):
    _name = 'vnitpro.supplies'

    code = fields.Char(string="Code Supplies", required=True)
    name = fields.Char(string="Name Supplies", required=True)
    group_supplies = fields.Many2one('vnitpro.groupsupplies')
    # importsupplies_id = fields.Many2one('importsupplies', string="importsupplies")
    compute_name = fields.Char('Compute_name')

    @api.depends('code', 'name')
    def _compute_name(self):
        if self.code and self.name:
            self.compute_name = self.code + ' - ' + self.name
