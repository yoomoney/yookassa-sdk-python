# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models.currency import Currency
from yookassa.domain.request import PayoutRequestBuilder


class TestPayoutRequestBuilder(unittest.TestCase):

    def test_build_object(self):
        self.maxDiff = None

        builder = PayoutRequestBuilder()
        builder.set_amount({'value': 0.1, 'currency': Currency.RUB}) \
            .set_description('Выплата по заказу №37') \
            .set_payout_token('99091209012') \
            .set_metadata({'key': 'value'}) \
            .set_deal({
                'id': 'dl-285e5ee7-0022-5000-8000-01516a44b147'
            })

        request = builder.build()

        self.assertEqual({
            'amount': {'value': '0.10', 'currency': Currency.RUB},
            'description': 'Выплата по заказу №37',
            'payout_token': '99091209012',
            'metadata': {'key': 'value'},
            'deal': {
                'id': 'dl-285e5ee7-0022-5000-8000-01516a44b147'
            },
        }, dict(request))
