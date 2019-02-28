# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)


def delay_export(env, model_name, record_id, vals, **job_kwargs):
    """ Delay a job which export a binding record.

    (A binding record being a ``jira.res.partner``,
    ``jira.product.product``, ...)

    The additional kwargs are passed to ``with_delay()``, they can be:
        ``priority``, ``eta``, ``max_retries``.
    """
    if env.context.get('connector_no_export'):
        return
    binding = env[model_name].browse(record_id)
    fields = vals.keys()
    binding.with_delay(**job_kwargs).export_record(fields=fields)


