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


