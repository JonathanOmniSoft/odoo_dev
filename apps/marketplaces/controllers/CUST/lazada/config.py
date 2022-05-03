#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
import os
import odoo
import lazop
import requests

from odoo.http import request
from odoo import http, exceptions, _


# class config():
#   def __init__(self):
#       # Init DB
#       # Get APP, Client ID, Client Secret_key
#       self.app_id = "108986"
#       self.client_id = "108986"
#       self.client_secret = "GbDUTQw7T2qzRG0hmfsvthSQO213QaM0"

#       # All region Service Endpoints
#       self.service_endpoint = "https://api.lazada.com/rest"

#       client = lazop.LazopClient(self.service_endpoint, self.client_id ,self.client_secret)
#       request = lazop.LazopRequest('/auth/token/create')
#       request.add_api_param('code', '0_2DL4DV3jcU1UOT7WGI1A4rY91')
#       request.add_api_param('uuid', '38284839234')
#       response = client.execute(request)

#       self.access_token = response["access_token"]
#       self.refresh_token = response["refresh_token"]

# https://omnisoft.odoo.com/web#cids=1&action=menu
@http.route(['/lazada/cb'], type='https', auth="public", website=True)
def get_authcode(self, **kw):
  pass