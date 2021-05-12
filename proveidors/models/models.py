# -*- coding: utf-8 -*-

from odoo import models, fields, api


class proveidors(models.Model):
    _name = 'proveidors.proveidors'
    _description = 'proveidors.proveidors'

    name = fields.Char(string="Nom companyia", required=True)
    contact = fields.Char(string="Persona de contacte")
    title = fields.Char(string="Títol de la persona de contacte")
    state = fields.Char(string="Provincia")
    city = fields.Char(string="Ciutat")
    adress = fields.Char(string="Adreça")
    codi = fields.Char(string="CP")
    pais = fields.Char(string="Pais")
    telefon = fields.Char(string="Telefon")
    fax = fields.Char(string="Fax")
    web = fields.Char(string="Webpage")

# class proveidors(models.Model):
#     _name = 'proveidors.proveidors'
#     _description = 'proveidors.proveidors'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
