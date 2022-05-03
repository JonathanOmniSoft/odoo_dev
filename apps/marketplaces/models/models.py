# -*- coding: utf-8 -*-

from re import T
from attr import field
from pkg_resources import require
import odoo
import datetime
from odoo import models, fields, api, exceptions, tools, _
from odoo.exceptions import UserError
from odoo.tools.image import image_data_uri
import dateutil.parser
import werkzeug
import pytz
import json
import os
import base64

# Marketplace Seller platform
class MarketplaceIntegration(models.Model):
    _name = 'marketplace.platform'
    _description = 'Markplace Platform'

    name = fields.Char(required=True)
    app_id = fields.Char(required=True, string="Seller App ID")
    client_id = fields.Char(required=True, string="Client ID")
    client_secret = fields.Char(required=True, string="Client Serect Key")
    authtoken = fields.Html(required=True, string="API URL")
    access_token = fields.Char(invisible=True, readonly=True)
    token_type = fields.Char(invisible=True, readonly=True)

    company_id = fields.Many2one('res.company', string='Company Name')
    user_id = fields.Char(string="Seller ID")
    shop_name = fields.Char(string="Seller Shop Name")
    region = fields.Many2one('res.country', string='Region')

    created = fields.Datetime(required=True, default=lambda self: fields.datetime.now())


# Marketplace Group and Role
class MarketplaceUserManager(models.Model):
    _name = 'marketplace.user.manager'
    _description = 'User role in specify Markplace Platform'

    platform_id = fields.Many2one('marketplace.platform', 'MarketplaceIntegration')
    company_id = fields.Many2one('res.company', 'Company')

    username = fields.Char(required=True)
    role = fields.Char(Default = "Basic User")

    created = fields.Datetime()
