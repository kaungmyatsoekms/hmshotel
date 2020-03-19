# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hmshotel(models.Model):
    _name = 'hmshotel.hmshotel'
    _description = 'hmshotel.hmshotel'

    name = fields.Char()
    code = fields.Char()
    location = fields.Char()
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

class HotelFloor(models.Model):
    _name = 'hotel.floor'
    _description = 'Floor'

    name = fields.Char('Floor Name', size=64, required=True, index=True)
    sequence = fields.Integer('Sequence', size=64, index=True) 


# class HotelRoomType(models.Model):
#     _name - 'hotel.room.type'
#     _description = 'Roome Type'

#     name = fields.Char('Name', size = 64, required = True )
#     categ_id = fields.Many2one('hotel.room.type', 'Category')
#     child_id = fields.One2many('hotel.room.type', 'categ_id','Child Categories')


class property(models.Model):
    _name = 'property.property'
    _description = 'propert property'

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