# -*- coding: utf-8 -*-
# from odoo import http


# class DetallComanda(http.Controller):
#     @http.route('/detall_comanda/detall_comanda/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/detall_comanda/detall_comanda/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('detall_comanda.listing', {
#             'root': '/detall_comanda/detall_comanda',
#             'objects': http.request.env['detall_comanda.detall_comanda'].search([]),
#         })

#     @http.route('/detall_comanda/detall_comanda/objects/<model("detall_comanda.detall_comanda"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('detall_comanda.object', {
#             'object': obj
#         })
