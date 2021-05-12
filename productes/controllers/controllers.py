# -*- coding: utf-8 -*-
# from odoo import http


# class Productes(http.Controller):
#     @http.route('/productes/productes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/productes/productes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('productes.listing', {
#             'root': '/productes/productes',
#             'objects': http.request.env['productes.productes'].search([]),
#         })

#     @http.route('/productes/productes/objects/<model("productes.productes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('productes.object', {
#             'object': obj
#         })
