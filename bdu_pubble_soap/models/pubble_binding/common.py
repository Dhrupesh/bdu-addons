# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models
from odoo.addons.queue_job.job import job, related_action
from ... unit.exporter import PubbleBaseExporter

class PubleBinding(models.AbstractModel):
    """ Abstract Model for the Bindings.

    All the models used as bindings between Pubble and Odoo
    """
    _name = 'pubble.binding'
    _inherit = 'external.binding'
    _description = 'Pubble Binding (abstract)'
    
    backend_id = fields.Many2one(
        comodel_name='pubble.backend',
        string='Pubble Backend',
        required=True,
        ondelete='restrict',
    )
    external_id = fields.Char(string='ID on Pubble', index=True)
    
            
    @job(default_channel='root')
    @related_action(action='related_action_unwrap_binding')
    @api.multi
    def export_record(self, fields=None):
        self.ensure_one()
        with self.backend_id.get_environment(self._name) as connector_env:
            exporter = connector_env.get_connector_unit(PubbleBaseExporter)
            exporter.run(self, fields=fields)