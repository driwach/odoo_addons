# -*- coding: utf-8 -*-

# from odoo import models, fields, api


 class detall_comanda(models.Model):
     _name = 'detall_comanda.detall_comanda'
     _description = 'detall_comanda.detall_comanda'
     id_comanda = fields.One2one("comandes.comandes", string="ID_comanda")
     id_producte = fields.Many2many("productes.productes", string="ID_comanda")
     quantitat = fields.Integer(string="quantitat")
     preu = fields.Float(string="Preu Untitat")
     desc = fields.Float(string="descompte")
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
