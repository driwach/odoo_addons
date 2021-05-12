# -*- coding: utf-8 -*-
# from odoo import http


# class Proveidors(http.Controller):
#     @http.route('/proveidors/proveidors/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proveidors/proveidors/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('proveidors.listing', {
#             'root': '/proveidors/proveidors',
#             'objects': http.request.env['proveidors.proveidors'].search([]),
#         })

#     @http.route('/proveidors/proveidors/objects/<model("proveidors.proveidors"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proveidors.object', {
#             'object': obj
#         })
