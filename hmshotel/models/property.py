-*- coding: utf-8 -*-

from odoo import models, fields, api


class property(models.Model):
    _name = 'property.property'
    _description = 'property.property'

    property_code = fields.Char()
    property_name = fields.Char()
    address1 = fields.Char()
    address2 = fields.Char()
    address3 = fields.Char()
    country_id = fields.Char()
    state_id = fields.char()
    city_id = fields.Char()
    telephone = fields.Char()
    fax = fields.Char()
    email = fields.Char()
    website = fields.Char()
    social_media_links = fields.Char()
    no_of_room = fields.Integer(size=4)
    proprety_license = fields.Char()
    property_rating = fields.Char()
    property_logo = fields.binary()
    property_photo = fields.binary()