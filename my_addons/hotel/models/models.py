# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hotel(models.Model):
    _name = 'hotel.hotel'

    name = fields.Char(String='Name')
    chamber = fields.Integer(string='Chamber No')
    division = fields.Char('Div')

