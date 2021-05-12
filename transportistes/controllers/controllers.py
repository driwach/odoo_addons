# -*- coding: utf-8 -*-
# from odoo import http


# class Transportistes(http.Controller):
#     @http.route('/transportistes/transportistes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/transportistes/transportistes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('transportistes.listing', {
#             'root': '/transportistes/transportistes',
#             'objects': http.request.env['transportistes.transportistes'].search([]),
#         })

#     @http.route('/transportistes/transportistes/objects/<model("transportistes.transportistes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('transportistes.object', {
#             'object': obj
#         })
