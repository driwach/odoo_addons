# -*- coding: utf-8 -*-

# from odoo import models, fields, api

class categoria(models.Model):
    _name = 'categoria.categoria'
    _description = 'categoria.categoria'
    NomCategoria = fields.Char(string="nom")
    Descripció = fields.Char(string="desc")
    Imatge = fields.Image(string="imatge")
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
