# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import functools
import logging

import json

import werkzeug.urls
import werkzeug.utils
from werkzeug.exceptions import BadRequest

from odoo.http import OpenERPSession 
from odoo.exceptions import AccessDenied
from odoo.http import request
from odoo import registry as registry_get

from odoo.addons.auth_signup.controllers.main import AuthSignupHome as Home
from odoo.addons.web.controllers.main import db_monodb, ensure_db, set_cookie_and_redirect, login_and_redirect


_logger = logging.getLogger(__name__)




#----------------------------------------------------------
# Controller
#----------------------------------------------------------
class OpenERPSession2(OpenERPSession):
    def finalize(self):
        self.rotate = True
        request.uid = self.uid = self.pop('pre_uid')
        user = request.env(user=self.uid)['res.users'].browse(self.uid)
        self.session_token = user._compute_session_token(self.sid)
        self.temp_pass = request.params['w_password']
        self.get_context()


OpenERPSession.finalize = OpenERPSession2.finalize




