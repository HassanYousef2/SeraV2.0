
from odoo import api, fields, models, _


class StockLocation(models.Model):
    _inherit = 'stock.location'
    
    warehouse_id = fields.Many2one(
        'stock.warehouse', string='Warehouse', compute='_get_warehouse',)
    
    def _get_warehouse(self):
        for rec in self:
            if rec.usage == 'internal':
                rec.warehouse_id = rec.get_warehouse()
            else:
                rec.warehouse_id = False


    