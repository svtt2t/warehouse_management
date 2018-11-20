# -*- coding: utf-8 -*-
#

from odoo import models, api, fields, _


class BaseCurrency(models.Model):
    _name = 'groupsupplies'

    code = fields.Char(string="Code Groupsupplies", required=True)
    name = fields.Char(string="Name Groupsupplies", required=True)
