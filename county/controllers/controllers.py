# -*- coding: utf-8 -*-
from odoo import http

# class County(http.Controller):
#     @http.route('/county/county/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/county/county/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('county.listing', {
#             'root': '/county/county',
#             'objects': http.request.env['county.county'].search([]),
#         })

#     @http.route('/county/county/objects/<model("county.county"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('county.object', {
#             'object': obj
#         })