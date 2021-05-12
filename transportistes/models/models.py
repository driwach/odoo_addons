# -*- coding: utf-8 -*-

from odoo import models, fields, api


class transportistes(models.Model):
    _name = 'transportistes.transportistes'
    _description = 'transportistes.transportistes'
    id = fields.Char(string="ID_Transport", required=True)
    name = fields.Char(string="Nom companyia", required=True)
    contact = fields.Char(string="Persona de contacte")
    phone = fields.Char(string="Provincia")

# class transportistes(models.Model):
#     _name = 'transportistes.transportistes'
#     _description = 'transportistes.transportistes'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
