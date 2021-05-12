# -*- coding: utf-8 -*-
# from odoo import http


# class Categoria(http.Controller):
#     @http.route('/categoria/categoria/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/categoria/categoria/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('categoria.listing', {
#             'root': '/categoria/categoria',
#             'objects': http.request.env['categoria.categoria'].search([]),
#         })

#     @http.route('/categoria/categoria/objects/<model("categoria.categoria"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('categoria.object', {
#             'object': obj
#         })
