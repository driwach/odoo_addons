# -*- coding: utf-8 -*-
# from odoo import http


# class Empleats(http.Controller):
#     @http.route('/empleats/empleats/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/empleats/empleats/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('empleats.listing', {
#             'root': '/empleats/empleats',
#             'objects': http.request.env['empleats.empleats'].search([]),
#         })

#     @http.route('/empleats/empleats/objects/<model("empleats.empleats"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('empleats.object', {
#             'object': obj
#         })
