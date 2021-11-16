# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models.amount import Amount
from yookassa.domain.models.cancellation_details import CancellationDetails
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.deal import PayoutDealInfo
from yookassa.domain.models.payout import PayoutStatus
from yookassa.domain.models.payout_data.response.payout_destination_bank_card import PayoutDestinationBankCard
from yookassa.domain.response.payout_response import PayoutResponse


class TestPayoutResponse(unittest.TestCase):

    def test_response_cast(self):
        self.maxDiff = None
        response = PayoutResponse({
            "id": "po-2855a19a-0003-5000-a000-0efa9e7f4264",
            "amount": {
                "value": "320.00",
                "currency": Currency.RUB
            },
            "status": "succeeded",
            "payout_destination": {
                "type": "bank_card",
                "card": {
                    "first6": "220220",
                    "last4": "2537",
                    "card_type": "MIR",
                    "issuer_country": "RU",
                    "issuer_name": "Sberbank Of Russia"
                }
            },
            "cancellation_details": {
                "party": "yookassa",
                "reason": "one_time_limit_exceeded"
            },
            "description": "Выплата по заказу №37",
            "created_at": "2021-06-21T16:22:50.512Z",
            "deal": {
                "id": "dl-285e5ee7-0022-5000-8000-01516a44b147"
            },
            "metadata": {
                "order_id": "37"
            },
            "test": False
        })

        self.assertIsInstance(response.amount, Amount)
        self.assertIsInstance(response.payout_destination, PayoutDestinationBankCard)
        self.assertIsInstance(response.cancellation_details, CancellationDetails)
        self.assertIsInstance(response.deal, PayoutDealInfo)

        self.assertEqual(response.metadata, {
            "order_id": "37"
        })
        self.assertFalse(response.test)
        self.assertEqual(response.id, "po-2855a19a-0003-5000-a000-0efa9e7f4264")
        self.assertEqual(response.status, PayoutStatus.SUCCEEDED)
        self.assertEqual(response.amount.value, 320.00)

        self.assertEqual(response.description, "Выплата по заказу №37")
        self.assertEqual(response.created_at, "2021-06-21T16:22:50.512Z")
