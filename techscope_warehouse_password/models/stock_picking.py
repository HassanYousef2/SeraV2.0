
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.http import request
class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    password = fields.Char(string='Password', copy= False)
    warehouse_password = fields.Char(string='Password', compute='_get_warehouse_password', store=True)

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        user_pass = request.session.temp_pass
        if domain:
            domain = ['&', ['warehouse_password', '=', user_pass]] + domain
        else:
            domain = [('warehouse_password', '=', user_pass)]
        return super(StockPicking, self).search_read(domain=domain, fields=fields, offset=offset, limit=limit, order=order)
    @api.depends('location_id.warehouse_id.password')
    def _get_warehouse_password(self):
        for rec in self:
            if rec.location_id:
                warehouse_id = rec.location_id.get_warehouse()
                if warehouse_id:
                    rec.warehouse_password = warehouse_id.password
                else:
                    rec.warehouse_password = False
            else:
                rec.warehouse_password = False
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
