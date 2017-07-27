# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class county_china(models.Model):
#     _name = 'county_china.county_china'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class China_province(models.Model):
    _name = "county.province"
    _inherit = 'county.province'

    county = fields.Char(string='国家', required=True)
