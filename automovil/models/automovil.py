from odoo import api, fields, models

 ## aqui se define el modelo

class Automovil(models.Model):
    _name = 'automovil'
    _description = 'Automovil'
    def _default_model_year(self):
        return fields.Date.add(fields.Date.today(), years=-10)
## name es un campo requerido
## se le puso un help para hacerlo mas facil para el usuario
    name = fields.Char(string='Name', required =True, help = "name of the car \n"
    "next rext \n"
    "seconds nexst")
    ## definicion de campo boleano
    is_on = fields.Boolean()
    velocity = fields.Float(digits='Automovil Velocity')
    doors_number = fields.Integer()
    description = fields.Text()
    model_year = fields.Date(string='Model Year',
                  default=_default_model_year, help = "1")
    ## toma el valor por default  ka fecha de hoy
    last_service_day = fields.Datetime(
        string='Last Service Day',
        default=fields.Datetime.now ,)
    last_verification_day = fields.Date(
        string='Last verification  Day',
        default=fields.Datetime.today,)
    ## le suma 6 meses a la fecha del siguiente servicio
    next_verification_day = fields.Date(
        string='Next Verification Day',
        default=fields.Date.add(fields.Date.today(), months=+6))
    cylinder = fields.Selection(
        string='Cylinder',
        selection=[('1' , '1 cylinder'),
                    ('2', '2 cylinders'),
                    ('14', '14 cylinders locos'),
                    ('8', '8 cylinders')],
                    default = "2")


    color = fields.Char(string='Color')
    ## explicacion de la funcion ONCHANGE, es deci,
    ## si se cambia la varible  de last_verificación
    @api.onchange('last_verification_day')
    def _onchange_last_verification_day(self):
        self.next_verification_day = fields.Date.add(self.last_verification_day, months=+6)
    ## explicacion de la funcion ONCHANGE, es deci,
    ## si se cambia la varible  de velocity es decir,
    ## si la velocidad es 0 entonces esta apagado
    ## si la velocidad es mayor que cero entonces esta prendido

    @api.onchange('velocity')
    def _onchange_velocity(self):
        if self.velocity <= 0:
            self.is_on = False
        else:
            self.is_on = True
