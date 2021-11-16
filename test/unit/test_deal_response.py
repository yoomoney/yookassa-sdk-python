# -*- coding: utf-8 -*-
import unittest
from decimal import Decimal

from yookassa.domain.models.amount import Amount
from yookassa.domain.response.deal_response import DealResponse


class TestDealResponse(unittest.TestCase):

    def test_response_cast(self):
        self.maxDiff = None
        response = DealResponse({
            "type": "safe_deal",
            "fee_moment": "payment_succeeded",
            "id": "dl-285e5ee7-0022-5000-8000-01516a44b147",
            "balance": {
                "value": "800.00",
                "currency": "RUB"
            },
            "payout_balance": {
                "value": "800.00",
                "currency": "RUB"
            },
            "status": "opened",
            "created_at": "2021-06-18T07:28:39.390497Z",
            "expires_at": "2021-09-16T07:28:39.390513Z",
            "metadata": {
                "order_id": "37"
            },
            "description": "SAFE_DEAL 123554642-2432FF344R",
            "test": False
        })

        self.assertIsInstance(response.balance, Amount)
        self.assertIsInstance(response.balance, Amount)

        self.assertEqual(response.metadata, {
            "order_id": "37"
        })
        self.assertFalse(response.test)
        self.assertEqual(response.id, "dl-285e5ee7-0022-5000-8000-01516a44b147")
        self.assertEqual(response.status, "opened")
        self.assertEqual(response.balance.value, 800.00)
        self.assertEqual(response.payout_balance.value, 800.00)
        self.assertEqual(response.description, "SAFE_DEAL 123554642-2432FF344R")
        self.assertEqual(response.created_at, "2021-06-18T07:28:39.390497Z")
        self.assertEqual(response.expires_at, "2021-09-16T07:28:39.390513Z")
        self.assertEqual(dict(response.payout_balance), {
            "value": "800.00",
            "currency": "RUB"
        })

