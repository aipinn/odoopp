# -*- coding: utf-8 -*-
from odoo import http

# class ApSaleTempl(http.Controller):
#     @http.route('/ap_templ/ap_templ/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ap_templ/ap_templ/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ap_templ.listing', {
#             'root': '/ap_templ/ap_templ',
#             'objects': http.request.env['ap_templ.ap_templ'].search([]),
#         })

#     @http.route('/ap_templ/ap_templ/objects/<model("ap_templ.ap_templ"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ap_templ.object', {
#             'object': obj
#         })