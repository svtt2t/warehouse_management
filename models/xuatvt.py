from odoo import api, models,  fields

class DinhPham(models.Model):
    _name = 'xuatvt'

    code = fields.Text()
    name = fields.Char(string="Name", required=True)
    warehouse_id = fields.Many2one('warehouse_management',
                                     ondelete='cascade', string="warehouse", required=True)
    compute_name = fields.Char(compute='_compute_name')
    details_ids = fields.One2many('details', 'Exportingsupplies_id')
    # details_ids = fields.One2many('supplies', 'details_id', string="details")
    # supplies_id = fields.Many2many(comodel_name='supplies', string="Supplies")


    @api.depends('name', 'code')
    def _compute_name(self):
        if self.code and self.name:
            self.compute_name = self.code + ' - ' + self.name

class Details(models.Model):
    _name = 'details'
    Exportingsupplies_id = fields.Many2one('xuatvt', string="Name Exportingsupplies")
    quantity_id = fields.Integer(string="Number", required=True)
    supplies_id = fields.Many2one('supplies', string="Supplies")
    groupsupplies_id = fields.Many2one('groupsupplies', related='supplies_id.group_supplies', readonly=True)

