# -*- coding: utf-8 -*-
import unittest
from yookassa.domain.models.deal import DealType, FeeMoment
from yookassa.domain.request import DealRequest


class TestDealRequest(unittest.TestCase):

    def test_request_cast(self):
        self.maxDiff = None
        request = DealRequest()
        request.type = DealType.SAFE_DEAL
        request.fee_moment = FeeMoment.DEAL_CLOSED
        request.description = 'Test description'
        request.metadata = {'key': 'value'}

        self.assertEqual({
            'type': 'safe_deal',
            'fee_moment': 'deal_closed',
            'description': 'Test description',
            'metadata': {'key': 'value'},
        }, dict(request))

    def test_request_setters(self):
        request = DealRequest({
            'type': 'safe_deal',
            'fee_moment': 'deal_closed',
            'description': 'Test description',
            'metadata': {'key': 'value'},
        })

        with self.assertRaises(ValueError):
            request.description = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                                  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def test_request_validate(self):
        request = DealRequest()

        with self.assertRaises(ValueError):
            request.validate()

        request.description = 'Test description'

        with self.assertRaises(ValueError):
            request.validate()

        request.metadata = {'key': 'value'}
        with self.assertRaises(ValueError):
            request.validate()

        request.fee_moment = FeeMoment.DEAL_CLOSED
        with self.assertRaises(ValueError):
            request.validate()

        request = DealRequest()
        request.type = DealType.SAFE_DEAL
        request.description = 'Test description'
        request.metadata = {'key': 'value'}
        with self.assertRaises(ValueError):
            request.validate()

        request = DealRequest()
        request.fee_moment = FeeMoment.DEAL_CLOSED
        request.description = 'Test description'
        request.metadata = {'key': 'value'}
        with self.assertRaises(ValueError):
            request.validate()
