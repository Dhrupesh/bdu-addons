# -*- coding: utf-8 -*-
# Copyright 2015 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# Copyright 2015 Antonio Espinosa <antonio.espinosa@tecnativa.com>
# Copyright 2015 Javier Iniesta <javieria@antiun.com>
# Copyright 2016 Antonio Espinosa - <antonio.espinosa@tecnativa.com>
# Copyright 2018 Willem Hulshof <w.hulshof@magnus.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Extend mail_mass_mailing_contact fields",
    "version": "10.0.1.0.2",
    "author": "Magnus, "
              "Odoo Community Association (OCA)",
    "website": "https://www.magnus.nl",
    "license": "AGPL-3",
    "category": "Marketing",
    'description': """
This module Extend mail_mass_mailing_contact fields
and improves performance of syncing in mass_mailing_list_dynamic
""",
    "depends": [
        'mass_mailing_partner',
        'mass_mailing_list_dynamic'
    ],
    'data': [
        'views/mail_mass_mailing_contact_view.xml',
    ],
    "installable": True,
}
