# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import json
import logging
import re
import tempfile

from jira import JIRAError
from jira.utils import json_loads

from odoo import api, fields, models, exceptions, _

from ...unit.backend_adapter import PubbleAdapter
from ...backend import pubble

_logger = logging.getLogger(__name__)


class pubbleSaleOrder(models.Model):
    _name = 'pubble.sale.order'
    _inherit = 'pubble.binding'
    _inherits = {'sale.order': 'odoo_id'}
    _description = 'Pubble Sale order'

    odoo_id = fields.Many2one(comodel_name='sale.order',
                              string='Order',
                              required=True,
                              index=True,
                              ondelete='restrict')


    @api.model
    def create(self, values):
        record = super(pubbleSaleOrder, self).create(values)
        if not record.jira_key:
            raise exceptions.UserError(
                _('The JIRA Key is mandatory in order to export a project')
            )
        return record

    @api.multi
    def write(self, values):
        if 'project_template' in values:
            raise exceptions.UserError(
                _('The project template cannot be modified.')
            )
        return super(pubbleSaleOrder, self).write(values)

    @api.multi
    def unlink(self):
        if any(self.mapped('external_id')):
            raise exceptions.UserError(
                _('Exported project cannot be deleted.')
            )
        return super(pubbleSaleOrder, self).unlink()


class SaleOrder(models.Model):
    _inherit = ["sale.order"]

    pubble_bind_ids = fields.One2many(
        comodel_name='pubble.sale.order',
        inverse_name='odoo_id',
        copy=False,
        string='Pubble Bindings',
        context={'active_test': False},
    )
    
    @api.depends('order_line.line_pubble_allow')
    @api.multi
    def _pubble_allow(self):
        for order in self:
            order.order_pubble_allow = False
            for line in order.order_line:
                if line.line_pubble_allow:
                    order.order_pubble_allow = True
                    break

    @api.depends('date_sent_pubble', 'write_date')
    @api.multi
    def _pubble_write_after_sent(self):
        for order in self:
            if order.date_sent_pubble:
                order.pubble_write_after_sent = order.date_sent_pubble < order.write_date

    @api.depends('order_line.pubble_sent')
    @api.multi
    def _pubble_sent(self):
        for order in self:
            order.pubble_sent = False
            for line in order.order_line:
                if line.pubble_sent:
                    order.pubble_sent = True
                    break
                


