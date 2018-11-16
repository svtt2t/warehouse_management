from odoo import api, models,  fields
class DinhPham(models.Model):
    _name = 'xuatvt'
    code = fields.Text()
    name = fields.Char(string="Name", required=True)
    warehouse_id = fields.Many2one('warehouse_management',
                                     ondelete='cascade', string="warehouse", required=True)
    compute_name = fields.Char('compute_name')

    @api.onchange('code', 'name')
    def _onchange_compute_name(self):
        if self.code and self.name:
            self.compute_name = self.code + ' - ' + self.name

   
