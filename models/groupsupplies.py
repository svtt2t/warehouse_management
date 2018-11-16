# -*- coding: utf-8 -*-
#

from odoo import models, api, fields, _


class BaseCurrency(models.Model):
    _name = 'groupsupplies'

    code=fields.Text()
    name=fields.Text()
    compute_name = fields.Char('compute_name')

    @api.onchange('code', 'name')
    def _onchange_compute_name(self):
        if self.code and self.name:
            self.compute_name = self.code + ' - ' + self.name
