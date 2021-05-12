# -*- coding: utf-8 -*-

from odoo import models, fields, api

class empleats(models.Model):
    _name = 'empleats.empleats'
    _description = 'empleats.empleats'


    id = fields.Char(string="ID_Empleat", required=True)
    name = fields.Char(string="Nom", required=True)
    lastname = fields.Char(string="Cognoms")
    fotografia = fields.Image(string="Fotografia")
    date = fields.Date(string="Data de contractació")
    province = fields.Char(string="Provincia")
    ciutat = fields.Char(string="Ciutat")
    Adress = fields.Char(string="Adreça")
    cp = fields.Char(string="Codi Postal")
    country = fields.Char(string="Persona de Contacte")
    phone = fields.Char(string="Persona de Contacte")
    fax = fields.Char(string="Persona de Contacte")

# class empleats(models.Model):
#     _name = 'empleats.empleats'
#     _description = 'empleats.empleats'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
