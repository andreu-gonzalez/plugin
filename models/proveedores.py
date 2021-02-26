from odoo import models, fields, api

class proveedores(models.Model):
    _inherit = 'fruteria.proveedores_model'
    _name = 'fruteria.proveedores_model'
    valoracion = fields.Float(string="valoracion")