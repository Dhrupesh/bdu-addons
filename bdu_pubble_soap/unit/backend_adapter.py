# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)


from odoo.addons.connector.unit.backend_adapter import CRUDAdapter

JIRA_JQL_DATETIME_FORMAT = '%Y-%m-%d %H:%M'  # no seconds :-(


class PubbleAdapter(CRUDAdapter):
    """ External Records Adapter for Jira """

    def __init__(self, environment):
        """
        :param environment: current environment (backend, model_name, ...)
        :type environment: :py:class:`connector.connector.ConnectorEnvironment`
        """
        super(JiraAdapter, self).__init__(environment)
        self.client = self.backend_record.get_api_client()
