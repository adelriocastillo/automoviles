from odoo import api, fields, models


class Automovil(models.Model):
    _name = 'automovil'
    _description = 'Automovil'

    name = fields.Char(string='Name')
