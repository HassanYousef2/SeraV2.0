# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp.http import request
from odoo.exceptions import UserError
from odoo.addons.auth_signup.controllers.main import AuthSignupHome

from werkzeug.exceptions import BadRequest

from odoo.http import OpenERPSession 
from odoo.exceptions import AccessDenied
from odoo.http import request
from odoo import registry as registry_get
from odoo import http, _
from odoo.addons.auth_signup.controllers.main import AuthSignupHome

from odoo.http import request

class AuthSignupHomeExt(AuthSignupHome):
    @http.route(['/warehouse/get_all'], type='json', auth="public", methods=['POST'], website=True)
    def get_all_warehouses(self):
        warehouses = request.env['stock.warehouse'].sudo().search([])
        w_list = []
        for warehouse in warehouses:
            w_list.append({'id':
             warehouse.id, 'name': warehouse.name})
        return w_list

    @http.route('/web/login', type='http', auth="none")
    def web_login(self, redirect=None, **kw):
        response = super(AuthSignupHomeExt, self).web_login(redirect, **kw)
        if request.httprequest.method == 'GET' and redirect and request.session.uid:
            response = super(AuthSignupHomeExt, self).web_login(redirect, **kw)
            return response
        if request.httprequest.method == 'POST':
            warehouse = request.params['warehouse']
            w_password = request.params['w_password']
            values = request.params.copy()
            if warehouse:
                warehouse = request.env['stock.warehouse'].sudo().search([('name', '=', warehouse)])
                if warehouse and not(warehouse.password == w_password):
                    values['error'] = _("Wrong Warehouse Password")
                    response = request.render('web.login', values)
                    response.headers['X-Frame-Options'] = 'DENY'
                    return response
        
        return response
#----------------------------------------------------------
# Controller
#----------------------------------------------------------
class OpenERPSession2(OpenERPSession):
    def finalize(self):
        self.rotate = True
        request.uid = self.uid = self.pop('pre_uid')
        user = request.env(user=self.uid)['res.users'].browse(self.uid)
        self.session_token = user._compute_session_token(self.sid)
        # self.temp_pass = request.params['w_password']
        self.warehouse_id = request.env['stock.warehouse'].sudo().search([('name', '=', request.params['warehouse'])]).id
        self.get_context()


OpenERPSession.finalize = OpenERPSession2.finalize




