from odoo import models, fields, api

class Hotel(models.Model):
    _name = 'hms.hotel'

name = fields.Char()
code = fields.Char()
location = fields.Char()