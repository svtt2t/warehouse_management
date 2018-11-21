# -*- coding: utf-8 -*-
#

from odoo import models, api, fields, _


class BaseCurrency(models.Model):
    _name = 'vnitpro.groupsupplies'

    code = fields.Char(string="Code Groupsupplies", required=True)
    name = fields.Char(string="Name Groupsupplies", required=True)
    compute_name = fields.Char('Compute_name')

    @api.depends('code', 'name')
    def _compute_name(self):
        if self.code and self.name:
            self.compute_name = self.code + ' - ' + self.name
