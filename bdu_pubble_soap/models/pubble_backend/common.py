# -*- coding: utf-8 -*-
# Copyright: 2015 LasLabs, Inc.
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import logging
import json
import urlparse

from contextlib import contextmanager, closing
from datetime import datetime, timedelta
from os import urandom

import psycopg2
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

import odoo
from odoo import models, fields, api, exceptions, _

from odoo.addons.connector.connector import ConnectorEnvironment
from suds.client import Client
from suds.plugin import MessagePlugin
from lxml import etree

_logger = logging.getLogger(__name__)



@contextmanager
def new_env(env):
    with api.Environment.manage():
        registry = odoo.modules.registry.RegistryManager.get(env.cr.dbname)
        with closing(registry.cursor()) as cr:
            new_env = api.Environment(cr, env.uid, env.context)
            try:
                yield new_env
            except:
                cr.rollback()
                raise
            else:
                cr.commit()

class LogPlugin(MessagePlugin):
    def __init__(self):
        self.last_sent_raw = None
        self.last_received_raw = None

    def sending(self, context):
        self.last_sent_raw = str(context.envelope)

    def received(self, context):
        self.last_received_raw = str(context.reply)
        
class PubbleBackend(models.Model):
    _name = 'pubble.backend'
    _description = 'Pubble Backend'
    _backend_type = 'pubble'


    def _default_company(self):
        return self.env['res.company']._company_default_get('pubble.backend')


    transmission_id = fields.Char(string='Transmission ID', store=True, size=16, )
    uri = fields.Char(string='Pubble URI')
    publisher = fields.Char(string='Publisher')
    apiKey = fields.Char(string='API Key')
    
    @api.multi
    def export_sale_order(self, model, from_date_field):
        selfexport_record
        
    @api.model
    def _scheduler_export_sale_order(self):
        self.search([]).export_sale_order()

    @api.multi
    def check_connection(self):
#         self.ensure_one()
        res = self.env['pubble.binding'].export_record(self)
        print "resresresresresres",res
        try:
            self.get_api_client()
        except ValueError as err:
            raise exceptions.UserError(
                _('Failed to connect (%s)') % (err,)
            )
        raise exceptions.UserError(
            _('Connection successful')
        )

    @contextmanager
    @api.multi
    def get_environment(self, model_name):
        self.ensure_one()
        yield ConnectorEnvironment(self, model_name)

    @api.model
    def get_api_client(self):
        try:
            plugin = LogPlugin()
            client = Client(self.uri, plugins=[plugin])
            SalesOrder = client.factory.create('ns1:salesOrder')
            response = client.service.processOrder(SalesOrder, self.transmission_id, self.publisher, self.apiKey)
           # self.write({'pubble_response': response, 'pubble_environment': publisher})
        except ValueError as err:
            raise exceptions.UserError(
                _('Failed to connect (%s)') % (err,)
            )
        raise exceptions.UserError(
            _('Connection successful')
        )


