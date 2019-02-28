# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo.addons.connector.backend import Backend

pubble = Backend('pubble')

""" Generic QoQa Backend. """

pubble_version = Backend(parent=pubble, version='1.0.0')
""" Backend for Pubble """
