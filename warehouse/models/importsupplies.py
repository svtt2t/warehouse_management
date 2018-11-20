# -*- coding: utf-8 -*-
#

from odoo import models, api, fields, _


class NamNam(models.Model):
    _name = 'importsupplies'
    code = fields.Char(string="Code", required=True)
    name = fields.Char(string="Name", required=True)
    warehouse_id = fields.Many2one('warehouse_management', string="Warehouse")
    details_ids = fields.One2many('details', 'importsupplies_id')
    # details_ids = fields.One2many('supplies', 'details_id', string="details")
    # supplies_id = fields.Many2many(comodel_name='supplies', string="Supplies")


class Details(models.Model):
    _name = 'details'
    importsupplies_id = fields.Many2one('importsupplies', string="Name Importsupplies")
    quantity_id = fields.Integer(string="Number", required=True)
    supplies_id = fields.Many2one('supplies', string="Supplies")
    groupsupplies_id = fields.Many2one('groupsupplies', related='supplies_id.group_supplies', readonly=True)
