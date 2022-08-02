from odoo import api, fields, models


class Automovil(models.Model):
    _name = 'automovil'
    _description = 'Automovil'

    name = fields.Char(string='Name')
    is_on = fields.Boolean()
    velocity = fields.Float(digits='Automovil Velocity')
    doors_number = fields.Integer()
    description = fields.Text()

