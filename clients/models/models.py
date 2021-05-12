# -*- coding: utf-8 -*-

from odoo import models, fields, api

class clients(models.Model):
    _name = 'clients.clients'
    _description = 'clients.clients'


    id = fields.Char(string="ID_Clients", required=True)
    name = fields.Char(string="Nom_companiya", required=True)
    contacte = fields.Char(string="Persona de Contacte")
    Title_Contacte = fields.Char(string="Títol de la persona de contacte")
    state = fields.Char(string="Provincia")
    city = fields.Char(string="Ciutat")
    Adress = fields.Char(string="Adreça")
    cp = fields.Char(string="Codi Postal")
    country = fields.Char(string="Persona de Contacte")
    phone = fields.Char(string="Persona de Contacte")
    fax = fields.Char(string="Persona de Contacte")
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
