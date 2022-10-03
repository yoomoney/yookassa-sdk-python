# -*- coding: utf-8 -*-
import sys
import unittest


from unittest.mock import patch

from yookassa import Settings, Configuration


class TestSettings(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        Configuration.configure(account_id='test_account_id', secret_key='test_secret_key')

    async def test_get_account_settings(self):
        self.maxDiff = None
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "account_id": Configuration.account_id,
                "test": False,
                "fiscalization_enabled": False,
                "payment_methods": [
                    "yoo_money",
                    "cash",
                    "bank_card"
                ]
            }
            settings = await Settings.get_account_settings()

        self.assertIsInstance(settings, dict)
        self.assertIsInstance(settings['payment_methods'], list)
        self.assertListEqual(settings['payment_methods'], ["yoo_money", "cash", "bank_card"])
        self.assertEqual(settings['account_id'], Configuration.account_id)
