# -*- coding: utf-8 -*-
#

from odoo import models, api, fields, _


class NamNam(models.Model):
    _name = 'vnitpro.importsupplies'

    code = fields.Char("Code", required=True)
    name = fields.Char("Name", required=True)
    warehouse_id = fields.Many2one('vnitpro.warehouse_management', "Warehouse")
    details_ids = fields.One2many('vnitpro.details', 'importsupplies_id')
    compute_name = fields.Char('Compute Name')

    @api.depends('code', 'name')
    def _compute_name(self):
        if self.code and self.name:
            self.compute_name = self.code + ' - ' + self.name


class Details(models.Model):
    _name = 'vnitpro.details'

    importsupplies_id = fields.Many2one('vnitpro.importsupplies', "Name Importsupplies")
    quantity_id = fields.Integer("Number", required=True)
    supplies_id = fields.Many2one('vnitpro.supplies', "Supplies")
    groupsupplies_id = fields.Many2one('vnitpro.groupsupplies', related='supplies_id.group_supplies', readonly=True)
