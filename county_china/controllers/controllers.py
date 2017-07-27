# -*- coding: utf-8 -*-
from odoo import http

# class CountyChina(http.Controller):
#     @http.route('/county_china/county_china/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/county_china/county_china/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('county_china.listing', {
#             'root': '/county_china/county_china',
#             'objects': http.request.env['county_china.county_china'].search([]),
#         })

#     @http.route('/county_china/county_china/objects/<model("county_china.county_china"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('county_china.object', {
#             'object': obj
#         })