# -*- coding: utf-8 -*-
import sys
import unittest

if sys.version_info >= (3, 3):
    from unittest.mock import patch
else:
    from mock import patch

from yookassa.configuration import Configuration
from yookassa.domain.models.amount import Amount
from yookassa.domain.request import DealRequest
from yookassa.domain.response import DealResponse, DealListResponse
from yookassa.deal import Deal


class TestDealFacade(unittest.TestCase):
    def setUp(self):
        Configuration.configure(account_id='test_account_id', secret_key='test_secret_key')

    def test_create_deal_with_dict(self):
        self.maxDiff = None
        deal_facade = Deal()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "type": "safe_deal",
                "fee_moment": "deal_closed",
                "id": "dl-285e5ee7-0022-5000-8000-01516a44b147",
                "balance": {
                    "value": -45,
                    "currency": "RUB"
                },
                "payout_balance": {
                    "value": 0,
                    "currency": "RUB"
                },
                "status": "closed",
                "created_at": "2021-06-18T07:28:39.390Z",
                "expires_at": "2021-09-16T07:28:39.390Z",
                "metadata": {
                    "order_id": 37
                },
                "description": "SAFE_DEAL 123554642-2432FF344R",
                "test": False
            }
            deal = deal_facade.create({
                "type": "safe_deal",
                "fee_moment": "deal_closed",
                "metadata": {
                    "order_id": 37
                },
                "description": "SAFE_DEAL 123554642-2432FF344R"
            }, 'asd213')

        self.assertIsInstance(deal, DealResponse)
        self.assertIsInstance(deal.balance, Amount)
        self.assertIsInstance(deal.payout_balance, Amount)

    def test_create_deal_with_object(self):
        self.maxDiff = None
        deal_facade = Deal()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "type": "safe_deal",
                "fee_moment": "deal_closed",
                "id": "dl-285e5ee7-0022-5000-8000-01516a44b147",
                "balance": {
                    "value": -45,
                    "currency": "RUB"
                },
                "payout_balance": {
                    "value": 0,
                    "currency": "RUB"
                },
                "status": "closed",
                "created_at": "2021-06-18T07:28:39.390Z",
                "expires_at": "2021-09-16T07:28:39.390Z",
                "metadata": {
                    "order_id": 37
                },
                "description": "SAFE_DEAL 123554642-2432FF344R",
                "test": False
            }
            deal = deal_facade.create(DealRequest({
                "type": "safe_deal",
                "fee_moment": "deal_closed",
                "metadata": {
                    "order_id": 37
                },
                "description": "SAFE_DEAL 123554642-2432FF344R"
            }))

        self.assertIsInstance(deal, DealResponse)
        self.assertIsInstance(deal.balance, Amount)
        self.assertIsInstance(deal.payout_balance, Amount)

    def test_deal_info(self):
        deal_facade = Deal()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "type": "safe_deal",
                "fee_moment": "deal_closed",
                "id": "dl-285e5ee7-0022-5000-8000-01516a44b147",
                "balance": {
                    "value": -45,
                    "currency": "RUB"
                },
                "payout_balance": {
                    "value": 0,
                    "currency": "RUB"
                },
                "status": "closed",
                "created_at": "2021-06-18T07:28:39.390Z",
                "expires_at": "2021-09-16T07:28:39.390Z",
                "metadata": {
                    "order_id": 37
                },
                "description": "SAFE_DEAL 123554642-2432FF344R",
                "test": False
            }
            deal = deal_facade.find_one('dl-285e5ee7-0022-5000-8000-01516a44b147')

        self.assertIsInstance(deal, DealResponse)
        self.assertIsInstance(deal.balance, Amount)
        self.assertIsInstance(deal.payout_balance, Amount)

    def test_deal_list(self):
        deal_facade = Deal()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "items": [
                    {
                        "type": "safe_deal",
                        "fee_moment": "deal_closed",
                        "id": "dl-285e5ee7-0022-5000-8000-01516a44b147",
                        "balance": {
                            "value": -45,
                            "currency": "RUB"
                        },
                        "payout_balance": {
                            "value": 0,
                            "currency": "RUB"
                        },
                        "status": "closed",
                        "created_at": "2021-06-18T07:28:39.390Z",
                        "expires_at": "2021-09-16T07:28:39.390Z",
                        "metadata": {
                            "order_id": 37
                        },
                        "description": "SAFE_DEAL 123554642-2432FF344R",
                        "test": False
                    }
                ],
                "type": "list",
                "next_cursor": "37a5c87d-3984-51e8-a7f3-8de646d39ec15"
            }
            deal = deal_facade.list({
                'status': 'closed',
                'limit': 1
            })

            self.assertIsInstance(deal, DealListResponse)
            self.assertIsInstance(deal.items, list)

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            Deal().find_one('')

        with self.assertRaises(TypeError):
            Deal().create('invalid params')
