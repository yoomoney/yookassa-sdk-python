# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.request import WebhookRequest
from yookassa.domain.response import WebhookList, WebhookResponse

from unittest.mock import patch

from yookassa import Configuration, Webhook


class TestWebhook(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        Configuration.configure(account_id='test_account_id', secret_key='test_secret_key')

    async def test_list(self):
        self.maxDiff = None
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "type": "list",
                "items": [
                    {
                        "id": "wh-e44e8088-bd73-43b1-959a-954f3a7d0c54",
                        "event": "payment.canceled",
                        "url": "https://www.merchant-website.com/notification_url"
                    },
                    {
                        "id": "wh-22d6d597-000f-5000-9000-145f6df21d6f",
                        "event": "payment.succeeded",
                        "url": "https://www.merchant-website.com/notification_url"
                    }
                ]
            }
            wh_list = await Webhook.list()

            self.assertIsInstance(wh_list, WebhookList)
            self.assertEqual(wh_list.type, "list")
            self.assertIsInstance(wh_list.items[0], WebhookResponse)

    async def test_add(self):
        self.maxDiff = None
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "id": "wh-22d6d597-000f-5000-9000-145f6df21d6f",
                "event": "payment.succeeded",
                "url": "https://www.merchant-website.com/notification_url"
            }

            params = WebhookRequest({
                "event": "payment.succeeded",
                "url": "https://www.merchant-website.com/notification_url",
            })
            wh = await Webhook.add(params)

            self.assertIsInstance(wh, WebhookResponse)
            self.assertEqual(wh.event, "payment.succeeded")

            params = {
                "event": "payment.succeeded",
                "url": "https://www.merchant-website.com/notification_url",
            }
            wh = await Webhook.add(params)

            self.assertIsInstance(wh, WebhookResponse)
            self.assertEqual(wh.event, "payment.succeeded")

        with self.assertRaises(TypeError):
            await Webhook.add('invalid data')

    async def test_remove(self):
        self.maxDiff = None
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {}

            response = await Webhook.remove("wh-22d6d597-000f-5000-9000-145f6df21d6f")

            self.assertIsInstance(response, WebhookResponse)
