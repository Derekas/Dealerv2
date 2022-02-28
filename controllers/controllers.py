# -*- coding: utf-8 -*-
# from odoo import http


# class Dealerv2App(http.Controller):
#     @http.route('/dealerv2_app/dealerv2_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dealerv2_app/dealerv2_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dealerv2_app.listing', {
#             'root': '/dealerv2_app/dealerv2_app',
#             'objects': http.request.env['dealerv2_app.dealerv2_app'].search([]),
#         })

#     @http.route('/dealerv2_app/dealerv2_app/objects/<model("dealerv2_app.dealerv2_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dealerv2_app.object', {
#             'object': obj
#         })
