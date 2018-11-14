from odoo import api, models, fields

class Namnam(models.Model):
	_name ='warehouse_management'
	
	name = fields.Char(string= "Name Warehouse",required=True)
	code = fields.Text()