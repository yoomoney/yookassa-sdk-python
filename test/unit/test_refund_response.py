# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models import Amount, Currency, RefundSource
from yookassa.domain.response import RefundResponse


class TestRefundResponse(unittest.TestCase):
    def test_response_cast(self):
        response = RefundResponse({
            'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
            'payment_id': '21b23365-000f-500b-9000-070fa3554403',
            'created_at': "2017-11-30T15:11:33+00:00",
            'amount': {
                "value": 250.0,
                "currency": Currency.RUB
            },
            'receipt_registration': 'pending',
            'comment': 'test comment',
            'status': 'pending',
            'sources': [
                {
                    'account_id': '79990000000',
                    "amount": {
                        "value": 100.01,
                        "currency": Currency.RUB
                    },
                    "platform_fee_amount": {
                        "value": 10.01,
                        "currency": Currency.RUB
                    }
                }
            ]
        })

        self.assertEqual(response.id, '21b23b5b-000f-5061-a000-0674e49a8c10')
        self.assertEqual(response.payment_id, '21b23365-000f-500b-9000-070fa3554403')
        self.assertEqual(response.created_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.receipt_registration, 'pending')
        self.assertEqual(response.comment, 'test comment')
        self.assertIsInstance(response.amount, Amount)
        self.assertIsInstance(response.sources[0], RefundSource)
        self.assertEqual(response.status, 'pending')
