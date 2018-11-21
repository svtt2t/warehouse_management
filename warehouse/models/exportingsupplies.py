from odoo import api, models, fields


class exportingsupplies(models.Model):
    _name = 'vnitpro.exporting'
    code = fields.Text()
    name = fields.Char(string="Name", required=True)
    warehouse_id = fields.Many2one('warehouse_management',
                                   ondelete='cascade', string="Warehouse", required=True)


    details_ids = fields.One2many('vnitpro.details', 'importsupplies_id')



    compute_name = fields.Char('Compute_name')

    @api.depends('code', 'name')
    def _compute_name(self):
        if self.code and self.name:
            self.compute_name = self.code + ' - ' + self.name




class Details(models.Model):
    _name = 'vnitpro.details'
    importsupplies_id = fields.Many2one('vnitpro.exporting', string="Exporting")
    quantity_id = fields.Integer(string="Number", required=True)
    supplies_id = fields.Many2one('vnitpro.supplies', string="Supplies")
    groupsupplies_id = fields.Many2one('vnitpro.groupsupplies', related='supplies_id.group_supplies', readonly=True)

