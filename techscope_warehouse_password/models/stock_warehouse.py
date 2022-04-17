
from odoo import api, fields, models, _


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'
    
    password = fields.Char(string='Password', required=True)


    