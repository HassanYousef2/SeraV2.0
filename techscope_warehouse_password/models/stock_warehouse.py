
from odoo import api, fields, models, _


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'
    
    password = fields.Char(string='Password', required=True)


    def get_all_warehouses(self):
        warehouses = self.env['stock.warehouse'].sudo().search([])
        w_list = []
        for warehouse in warehouses:
            w_list.append({'id': warehouse.id, 'name': warehouse.name})
        return 