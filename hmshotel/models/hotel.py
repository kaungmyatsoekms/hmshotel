from odoo import models, fields, api

class HotelModel(models.Model):
    _name = 'hms.hotel'

name = fields.Char()
code = fields.Char()
location = fields.Char()