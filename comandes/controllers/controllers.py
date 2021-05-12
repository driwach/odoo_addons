# -*- coding: utf-8 -*-
# from odoo import http


# class Comandes(http.Controller):
#     @http.route('/comandes/comandes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/comandes/comandes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('comandes.listing', {
#             'root': '/comandes/comandes',
#             'objects': http.request.env['comandes.comandes'].search([]),
#         })

#     @http.route('/comandes/comandes/objects/<model("comandes.comandes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('comandes.object', {
#             'object': obj
#         })
