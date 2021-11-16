# -*- coding: utf-8 -*-
import sys
import unittest

from yookassa.domain.models import Currency, PayoutDealInfo
from yookassa.domain.models.payout_data.payout_destination import PayoutDestination
from yookassa.domain.models.payout_data.response.payout_destination_bank_card import PayoutDestinationBankCard

if sys.version_info >= (3, 3):
    from unittest.mock import patch
else:
    from mock import patch

from yookassa.configuration import Configuration
from yookassa.domain.models.amount import Amount
from yookassa.domain.request import PayoutRequest
from yookassa.domain.response import PayoutResponse
from yookassa.payout import Payout


class TestPayoutFacade(unittest.TestCase):
    def setUp(self):
        Configuration.configure(account_id='test_account_id', secret_key='test_secret_key')

    def test_create_payout_with_dict(self):
        self.maxDiff = None
        payout_facade = Payout()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "id": "po-2855a19a-0003-5000-a000-0efa9e7f4264",
                "amount": {
                    "value": "320.00",
                    "currency": "RUB"
                },
                "status": "succeeded",
                "payout_destination": {
                    "type": "bank_card",
                    "card": {
                        "first6": "555555",
                        "last4": "4477",
                        "card_type": "MasterCard",
                        "issuer_country": "RU",
                        "issuer_name": "Sberbank Of Russia"
                    }
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
            }
            payout = payout_facade.create({
                "amount": {
                    "value": 320.0,
                    "currency": Currency.RUB
                },
                "payout_destination": {
                    "type": "bank_card",
                    "card": {
                        "number": "5555555555554477"
                    }
                },
                "description": "Выплата по заказу №37",
                "metadata": {
                    "order_id": "37"
                },
                "deal": {
                    "id": "dl-285e5ee7-0022-5000-8000-01516a44b147"
                }
            }, 'asd213')

        self.assertIsInstance(payout, PayoutResponse)
        self.assertIsInstance(payout.amount, Amount)
        self.assertIsInstance(payout.payout_destination, PayoutDestination)
        self.assertIsInstance(payout.metadata, dict)
        self.assertIsInstance(payout.deal, PayoutDealInfo)

    def test_create_payout_with_object(self):
        self.maxDiff = None
        payout_facade = Payout()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "id": "po-2855a19a-0003-5000-a000-0efa9e7f4264",
                "amount": {
                    "value": "320.00",
                    "currency": "RUB"
                },
                "status": "succeeded",
                "payout_destination": {
                    "type": "bank_card",
                    "card": {
                        "first6": "555555",
                        "last4": "4477",
                        "card_type": "MasterCard",
                        "issuer_country": "RU",
                        "issuer_name": "Sberbank Of Russia"
                    }
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
            }
            payout = payout_facade.create(PayoutRequest({
                "amount": {
                    "value": 320.0,
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
            }))

        self.assertIsInstance(payout, PayoutResponse)
        self.assertIsInstance(payout.amount, Amount)
        self.assertIsInstance(payout.metadata, dict)
        self.assertIsInstance(payout.deal, PayoutDealInfo)

    def test_payout_info(self):
        payout_facade = Payout()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "id": "po-2855a19a-0003-5000-a000-0efa9e7f4264",
                "amount": {
                    "value": "320.00",
                    "currency": "RUB"
                },
                "status": "succeeded",
                "payout_destination": {
                    "type": "bank_card",
                    "card": {
                        "first6": "555555",
                        "last4": "4477",
                        "card_type": "MasterCard",
                        "issuer_country": "RU",
                        "issuer_name": "Sberbank Of Russia"
                    }
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
            }
            payout = payout_facade.find_one('po-2855a19a-0003-5000-a000-0efa9e7f4264')

        self.assertIsInstance(payout, PayoutResponse)
        self.assertIsInstance(payout.amount, Amount)
        self.assertIsInstance(payout.metadata, dict)
        self.assertIsInstance(payout.deal, PayoutDealInfo)
        self.assertIsInstance(payout.payout_destination, PayoutDestinationBankCard)

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            Payout().find_one('')

        with self.assertRaises(TypeError):
            Payout().create('invalid params')
