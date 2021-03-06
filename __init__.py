# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool

from . import sale

__all__ = ['register']


def register():
    Pool.register(
        sale.Line,
        module='sale_discount', type_='model')
    Pool.register(
        module='sale_discount', type_='wizard')
    Pool.register(
        module='sale_discount', type_='report')
