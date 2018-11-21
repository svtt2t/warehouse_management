from odoo import api, models, fields


class Namnam(models.Model):
    _name = 'vnitpro.warehouse_management'

    code = fields.Char("Code Warehouse", required=True)
    name = fields.Char("Name Warehouse", required=True)
    compute_name = fields.Char('Compute Name')

    @api.depends('code', 'name')
    def _compute_name(self):
        if self.code and self.name:
            self.compute_name = self.code + ' - ' + self.name
