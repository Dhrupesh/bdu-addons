# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo.addons.connector.event import (on_record_create,
                                         on_record_write,
                                         )
from ... import common
from ...backend import pubble
from ...unit.exporter import PubbleBaseExporter
from ...unit.backend_adapter import PubbleAdapter


@on_record_create(model_names='pubble.sale.order')
@on_record_write(model_names='pubble.sale.order')
def delay_export(env, model_name, record_id, vals):
    common.delay_export(env, model_name, record_id, vals, priority=10)


# @on_record_write(model_names='sale.order')
# def delay_export_all_bindings(env, model_name, record_id, vals):
#     print "valsvalsvals",vals
#     
#     if vals.keys() == ['jira_bind_ids']:
#         # Binding edited from the project's view.
#         # When only this field has been modified, an other job has
#         # been delayed for the jira.product.product record.
#         return
#     common.delay_export_all_bindings(env, model_name, record_id, vals)


@pubble
class PubbleSaleOrderExporter(PubbleBaseExporter):
    _model_name = ['pubble.sale.order']


    def _run(self, fields=None):
        adapter = self.unit_for(PubbleAdapter)

        key = self.binding.jira_key
        name = self.binding.name[:80]
#         template = self.binding.project_template
        # TODO: add lead

