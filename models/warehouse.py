from odoo import api, models, fields

class Namnam(models.Model):
	_name ='warehouse_management'
	
	name = fields.Char(string= "Name Warehouse",required=True)
	code = fields.Char()
	compute_name = fields.Char(compute='_compute_name')


	@api.depends('name', 'code')
	def _compute_name(self):
		if self.code and self.name:
			self.compute_name = self.code + ' - ' + self.name
