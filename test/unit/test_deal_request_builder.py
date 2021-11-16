# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models.deal import DealType, FeeMoment
from yookassa.domain.request import DealRequestBuilder


class TestDealRequestBuilder(unittest.TestCase):

    def test_build_object(self):
        self.maxDiff = None
        request = None
        builder = DealRequestBuilder() \
            .set_type(DealType.SAFE_DEAL) \
            .set_fee_moment(FeeMoment.PAYMENT_SUCCEEDED) \
            .set_description('SAFE_DEAL 123554642-2432FF344R') \
            .set_metadata({'order_id': '37'})

        request = builder.build()

        self.assertEqual({
            "type": "safe_deal",
            "fee_moment": "payment_succeeded",
            "metadata": {
                "order_id": "37"
            },
            "description": "SAFE_DEAL 123554642-2432FF344R"
        }, dict(request))
