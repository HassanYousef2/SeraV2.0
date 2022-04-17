# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError, Warning, ValidationError
import json
import requests
import base64
import logging
class AUGWizard(models.Model):
    _name = 'aug.wizard'
    
    def fetch_orders(self):
        url = "https://datahub.arabunionglass.com/getData.php"
        payload = {}
        payload["dataType"] = 'json'
        payload["dataSection"] = 'orders'
        payload["dataCommand"] = 'readAll'
        headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9', }
        def _fetch_order_recursive( pageNext, pageMax):
            pageMax = pageMax
            pageNext = pageNext
            payload["page"] = str(int(pageNext) - 1)
            if int(pageNext) - 1 > pageMax:
                return
            response = requests.request(
                "POST", url, headers=headers, data=payload)
            if response.status_code == 200:
                body = response.json()
                if not body['hasError']:
                    data = body['data']["results"]
                    aug_order = self.env['aug.order']
                    pageMax = body['data']["pageMax"]
                    if body['data']["pageNext"]:
                        pageNext = int(body['data']["pageNext"]) + 1
                    else:
                        pageNext+=1
                    for order in data:
                        if not aug_order.search([('aug_order_id', '=', order['ORDERID'])]):
                            aug_order.create({
                                'aug_order_id': order['ORDERID'],
                                'aug_order_number': order['order_no'],
                                'aug_order_invoice_address_title': order['order_invoice_address_title'],
                                'aug_order_invoice_address_name': order['order_invoice_address_name'],
                                'aug_page_number': body['data']['pageCurrent'],
                            })
                    _fetch_order_recursive(pageNext, pageMax)
                            
        _fetch_order_recursive(2,1)



    def fetch_batches(self):
        url = "https://datahub.arabunionglass.com/getData.php"
        payload = {}
        payload["dataType"] = 'json'
        payload["dataSection"] = 'batches'
        payload["dataCommand"] = 'readAll'
        headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9', }
        last_batch = self.env['aug.batch'].search(
            [], order='aug_batch_id desc', limit=1)
        pageNext = 0
        pageMax = 0
        if last_batch:
            pageNext = last_batch.aug_page_number
            pageMax = last_batch.aug_page_number

        def _fetch_batch_recursive( pageNext, pageMax):
            pageMax = pageMax
            pageNext = pageNext
            payload["page"] = str(int(pageNext) - 1)
            if int(pageNext) - 1 > pageMax:
                return
            response = requests.request(
                "POST", url, headers=headers, data=payload)
            if response.status_code == 200:
                body = response.json()
                if not body['hasError']:
                    data = body['data']["results"]
                    aug_batch = self.env['aug.batch']
                    pageMax = body['data']["pageMax"]
                    if body['data']["pageNext"]:
                        pageNext = int(body['data']["pageNext"]) + 1
                    else:
                        pageNext+=1
                    for batch in data:
                        if not aug_batch.search([('aug_batch_id', '=', batch['BATCHID'])]):
                            aug_batch.create({
                                'aug_batch_id': batch['BATCHID'],
                                'aug_batch_number': batch['batch_no'],
                                'aug_page_number': body['data']['pageCurrent'],
                            })
                            self.env.cr.commit()
                    _fetch_batch_recursive(pageNext, pageMax)
                            
        _fetch_batch_recursive(2, 1)

    def fetch_steps(self):
        url = "https://datahub.arabunionglass.com/getData.php"
        payload = {}
        payload["dataType"] = 'json'
        payload["dataSection"] = 'orders_steps'
        payload["dataCommand"] = 'readAll'
        headers = {
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9', }
        last_step = self.env['aug.step'].search(
            [], order='aug_page_number desc', limit=1)
        pageNext = 0
        pageMax = 0
        if last_step:
            pageNext = last_step.aug_page_number
            pageMax = last_step.aug_page_number+10
        payload["page"] = pageNext
        print("SSSSSSSS")
        print("SSSSSSSS")
        print(pageNext)
        print("SSSSSSSS")
        print("SSSSSSSS")
        print("SSSSSSSS")
        def _fetch_step_recursive(pageNext, pageMax):
            pageMax = pageMax
            pageNext = pageNext
            payload["page"] = str(int(pageNext) - 1)
            if int(pageNext) - 1 > pageMax:
                return
            response = requests.request(
                "POST", url, headers=headers, data=payload)
            if response.status_code == 200:
                body = response.json()
                if not body['hasError']:
                    data = body['data']["results"]
                    aug_step = self.env['aug.step']
                    pageMax = body['data']["pageMax"]

                    if body['data']["pageNext"]:
                        pageNext = int(body['data']["pageNext"]) + 1
                    else:
                        pageNext+=1
                    print("DDDDDD")
                    print(pageNext)
                    print("DDDDDD")
                    print(pageNext)
                    print("DDDDDD")
                    print("DDDDDD")
                    for step in data:
                        if not aug_step.search([('aug_step_id', '=', step['STEPID'])]):
                            aug_step.create({
                                'aug_step_id': step['STEPID'],
                                'aug_step_number': step['step_no'],
                                'aug_order_number': step['step_order_no'],
                                'aug_api_payload': json.dumps(step, ensure_ascii=False).encode('utf8'),
                                'aug_page_number': body['data']['pageCurrent'],
                            })
                            self.env.cr.commit()
                    _fetch_step_recursive(pageNext, pageMax)
                            
        _fetch_step_recursive(pageNext, pageMax)



    

