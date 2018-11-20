# -*- coding: utf-8 -*-
#

from odoo import models, api, fields, _


class BaseCurrency(models.Model):
    _name = 'groupsupplies'

    code = fields.Text()
    name = fields.Text()
    compute_name = fields.Char(compute='_compute_name')


    @api.depends('name', 'code')
    def _compute_name(self):
        if self.code and self.name:
            self.compute_name = self.code + ' - ' + self.name
