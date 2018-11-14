# -*- coding: utf-8 -*-
#

from odoo import models, api, fields, _


class BaseCurrency(models.Model):
    _name = 'groupsupplies'

    code=fields.Text()
    name=fields.Text()