# -*- coding: utf-8 -*-
#

from odoo import models, api, fields, _


class NamNam(models.Model):
    _name = 'vnitpro.importsupplies'
    code = fields.Char(string="Code", required=True)
    name = fields.Char(string="Name", required=True)
    warehouse_id = fields.Many2one('vnitpro.warehouse_management', string="Warehouse")
    details_ids = fields.One2many('vnitpro.details', 'importsupplies_id')
    # details_ids = fields.One2many('supplies', 'details_id', string="details")
    # supplies_id = fields.Many2many(comodel_name='supplies', string="Supplies")

    compute_name = fields.Char('compute_name')

    @api.depends('code', 'name')
    def _compute_name(self):
        if self.code and self.name:
            self.compute_name = self.code + ' - ' + self.name


class Details(models.Model):
    _name = 'vnitpro.details'
    importsupplies_id = fields.Many2one('vnitpro.importsupplies', string="Name Importsupplies")
    quantity_id = fields.Integer(string="Number", required=True)
    supplies_id = fields.Many2one('vnitpro.supplies', string="Supplies")
    groupsupplies_id = fields.Many2one('vnitpro.groupsupplies', related='supplies_id.group_supplies', readonly=True)
