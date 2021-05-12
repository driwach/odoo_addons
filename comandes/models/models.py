# -*- coding: utf-8 -*-

# from odoo import models, fields, api


class comandes(models.Model):
    _name = 'comandes.comandes'
    _description = 'comandes.comandes'
    _inherit = "adress.adress"
    id = fields.Char(string="id_commanda", required=True)
    id_client = fields.Many2many("clients.clients", string="ID_Client")
    id_empleat = fields.Many2many("empleats.empleats", string="ID_Empleat")
    enviatper = fields.Char(string="Enviar per")
    datacomanda = fields.Char(string="Data comanda")
    dataenviament = fields.Char(string="Data Enviament")
    pes = fields.Char(string="pes")
    nom_enviament = fields.Char(string="nom_enviament")
    regio = fields.Char(string="Regió")

    # adressa = fields.Char(string="Adressa")
    # ciutat = fields.Char(string="Ciutat")
    # cp = fields.Char(string="CP")
    # pais = fields.Char(string="País")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
