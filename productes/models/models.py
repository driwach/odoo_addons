# -*- coding: utf-8 -*-

# from odoo import models, fields, api

# -*- coding: utf-8 -*-

# from odoo import models, fields, api
from odoo import models, fields, api

class productes(models.Model):
    _name = 'productes.productes'
    _description = 'productes.productes'
    id_categoria = fields.Many2one("categoria.categoria", string="Categoria")
    id_proveidor = fields.Many2many("proveidor.proveidor", string="Proveidor")
    name = fields.Char(string="Nom del Producte", required=True)
    code = fields.Integer(string="Codí producte", required=True)
    image = fields.Image(string="Imatge")
    description = fields.Char(string="Descripció")
    price = fields.Float(string="preu de compra proveïdor (Cost)")
    pvp = fields.Float(string="PVP")
    barcode = fields.Char(string="codi de barres")

# class productes(models.Model):
#     _name = 'productes.productes'
#     _description = 'productes.productes'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

# class productes(models.Model):
#     _name = 'productes.productes'
#     _description = 'productes.productes'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
