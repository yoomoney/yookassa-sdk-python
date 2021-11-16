# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common import PaymentMethodType
from yookassa.domain.models.amount import Amount
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.deal import PayoutDealInfo

from yookassa.domain.models.payout_data.request.payout_destination_yoomoney_wallet import \
    PayoutDestinationYooMoneyWallet
from yookassa.domain.request import PayoutRequest


class TestPayoutRequest(unittest.TestCase):

    def test_request_cast(self):
        self.maxDiff = None
        request = PayoutRequest()
        request.amount = Amount({"value": "320.00", "currency": "RUB"})
        request.description = "Выплата по заказу №37"
        request.payout_token = "<Синоним банковской карты>"
        request.metadata = {"order_id": "37"}
        request.deal = PayoutDealInfo({'id': 'dl-285e5ee7-0022-5000-8000-01516a44b147'})

        self.assertEqual({
            "amount": {
                "value": "320.00",
                "currency": Currency.RUB
            },
            "payout_token": "<Синоним банковской карты>",
            "description": "Выплата по заказу №37",
            "metadata": {
               "order_id": "37"
            },
            "deal": {
              "id": "dl-285e5ee7-0022-5000-8000-01516a44b147"
            }
          }, dict(request))

    def test_request_setters(self):
        request = PayoutRequest({
            "amount": {"value": 320.0, "currency": Currency.RUB},
            "payout_destination_data": {'type': PaymentMethodType.YOO_MONEY, 'account_number': '41001614575714'},
            "description": "Выплата по заказу №37",
            "metadata": {
               "order_id": "37"
            },
            "deal": {
              "id": "dl-285e5ee7-0022-5000-8000-01516a44b147"
            }
        })

        self.assertIsInstance(request.amount, Amount)
        self.assertIsInstance(request.payout_destination_data, PayoutDestinationYooMoneyWallet)
        self.assertIsInstance(request.deal, PayoutDealInfo)

        with self.assertRaises(TypeError):
            request.amount = 'invalid amount'

        with self.assertRaises(TypeError):
            request.payout_destination_data = 'invalid payout_destination_data'

        with self.assertRaises(TypeError):
            request.payout_token = ''

        with self.assertRaises(ValueError):
            request.description = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                                  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def test_request_validate(self):
        request = PayoutRequest()

        with self.assertRaises(ValueError):
            request.validate()

        request.amount = Amount({'value': 0.0, 'currency': Currency.RUB})

        with self.assertRaises(ValueError):
            request.validate()

        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})
        request.description = "Выплата по заказу №37"
        with self.assertRaises(ValueError):
            request.validate()

        request = PayoutRequest()
        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})
        with self.assertRaises(ValueError):
            request.validate()

        request = PayoutRequest()
        request.amount = Amount({'value': 0.1, 'currency': Currency.RUB})
        request.payout_token = '123'
        request.payout_destination_data = PayoutDestinationYooMoneyWallet()
        with self.assertRaises(ValueError):
            request.validate()
