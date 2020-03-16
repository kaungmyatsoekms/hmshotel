# -*- coding: utf-8 -*-
# from odoo import http


# class Hmshotel(http.Controller):
#     @http.route('/hmshotel/hmshotel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hmshotel/hmshotel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hmshotel.listing', {
#             'root': '/hmshotel/hmshotel',
#             'objects': http.request.env['hmshotel.hmshotel'].search([]),
#         })

#     @http.route('/hmshotel/hmshotel/objects/<model("hmshotel.hmshotel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hmshotel.object', {
#             'object': obj
#         })
