# -*- coding: utf-8 -*-
# from odoo import http


# class Fruteriamultimedia(http.Controller):
#     @http.route('/fruteriamultimedia/fruteriamultimedia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fruteriamultimedia/fruteriamultimedia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fruteriamultimedia.listing', {
#             'root': '/fruteriamultimedia/fruteriamultimedia',
#             'objects': http.request.env['fruteriamultimedia.fruteriamultimedia'].search([]),
#         })

#     @http.route('/fruteriamultimedia/fruteriamultimedia/objects/<model("fruteriamultimedia.fruteriamultimedia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fruteriamultimedia.object', {
#             'object': obj
#         })
