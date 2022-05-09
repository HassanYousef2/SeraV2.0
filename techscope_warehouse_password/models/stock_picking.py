
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.http import request
class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    password = fields.Char(string='Password', copy= False)
    warehouse_id = fields.Char(string='Password', compute='_get_warehouse_id', store=True)

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        warehouse_id = request.session.warehouse_id
        if domain:
            domain = ['&', ['warehouse_id', '=', warehouse_id]] + domain
        else:
            domain = [('warehouse_id', '=', warehouse_id)]
        return super(StockPicking, self).search_read(domain=domain, fields=fields, offset=offset, limit=limit, order=order)
    @api.depends('location_id.warehouse_id.password')
    def _get_warehouse_id(self):
        for rec in self:
            if rec.location_id:
                warehouse_id = rec.location_id.get_warehouse()
                if warehouse_id:
                    rec.warehouse_id = warehouse_id.id
                else:
                    rec.warehouse_id = False
            else:
                rec.warehouse_id = False
    def button_validate(self):
        for rec in self:
            warehouse_id = rec.location_id.get_warehouse()
            if warehouse_id.password == rec.password:
                return super(StockPicking, self).button_validate()
            else:
                raise UserError(_('Password is not correct'))

    def action_cancel(self):
        for rec in self:
            warehouse_id = rec.location_id.get_warehouse()
            if warehouse_id.password == rec.password:
                return super(StockPicking, self).action_cancel()
            else:
                raise UserError(_('Password is not correct'))

    def button_scrap(self):
        for rec in self:
            warehouse_id = rec.location_id.get_warehouse()
            if warehouse_id.password == rec.password:
                return super(StockPicking, self).button_scrap()
            else:
                raise UserError(_('Password is not correct'))

    def action_toggle_is_locked(self):
        for rec in self:
            warehouse_id = rec.location_id.get_warehouse()
            if warehouse_id.password == rec.password:
                return super(StockPicking, self).action_toggle_is_locked()
            else:
                raise UserError(_('Password is not correct'))
    
    def do_unreserve(self):
        for rec in self:
            warehouse_id = rec.location_id.get_warehouse()
            if warehouse_id.password == rec.password:
                return super(StockPicking, self).do_unreserve()
            else:
                raise UserError(_('Password is not correct'))
    
    def action_assign(self):
        for rec in self:
            warehouse_id = rec.location_id.get_warehouse()
            if warehouse_id.password == rec.password:
                return super(StockPicking, self).action_assign()
            else:
                raise UserError(_('Password is not correct'))
