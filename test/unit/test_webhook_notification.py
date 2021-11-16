# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.notification import WebhookNotification, RefundWebhookNotification, WebhookNotificationFactory
from yookassa.domain.response import PaymentResponse, RefundResponse, DealResponse
from yookassa.domain.response.payout_response import PayoutResponse


class TestWebhookNotification(unittest.TestCase):

    def test_notification_payment(self):
        self.maxDiff = None
        notification = WebhookNotification({
            "type": "notification",
            "event": "payment.waiting_for_capture",
            "object": {
                "id": "22d6d597-000f-5000-9000-145f6df21d6f",
                "status": "waiting_for_capture",
                "paid": True,
                "amount": {
                    "value": "2.00",
                    "currency": "RUB"
                },
                "authorization_details": {
                    "rrn": "10000000000",
                    "auth_code": "000000"
                },
                "created_at": "2018-07-10T14:27:54.691Z",
                "description": "Заказ №72",
                "expires_at": "2018-07-17T14:28:32.484Z",
                "metadata": {},
                "payment_method": {
                    "type": "bank_card",
                    "id": "22d6d597-000f-5000-9000-145f6df21d6f",
                    "saved": False,
                    "card": {
                        "first6": "555555",
                        "last4": "4444",
                        "expiry_month": "07",
                        "expiry_year": "2021",
                        "card_type": "MasterCard",
                        "issuer_country": "RU",
                        "issuer_name": "Sberbank"
                    },
                    "title": "Bank card *4444"
                },
                "refundable": False,
                "test": False
            }
        })

        self.assertIsInstance(notification.type, str)
        self.assertIsInstance(notification.event, str)
        self.assertIsInstance(notification.object, PaymentResponse)

        data = {
            "type": "notification",
            "event": "payment.waiting_for_capture",
            "object": {}
        }

        with self.assertRaises(ValueError):
            WebhookNotification(data)

        data = {
            "type": "notification",
            "event": "payment.waiting_for_capture",
            "object": 'Invalid object type'
        }

        with self.assertRaises(TypeError):
            WebhookNotification(data)

    def test_notification_refund(self):
        self.maxDiff = None
        notification = RefundWebhookNotification({
            "type": "notification",
            "event": "refund.succeeded",
            "object": {
                'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
                'payment_id': '21b23365-000f-500b-9000-070fa3554403',
                'created_at': "2017-11-30T15:11:33+00:00",
                'amount': {
                    "value": 250.0,
                    "currency": "RUB"
                },
                'receipt_registration': 'pending',
                'comment': 'test comment',
                'status': 'pending'
            }
        })

        self.assertIsInstance(notification.type, str)
        self.assertIsInstance(notification.event, str)
        self.assertIsInstance(notification.object, RefundResponse)

        data = {
            "type": "notification",
            "event": "refund.succeeded",
            "object": {}
        }

        with self.assertRaises(ValueError):
            RefundWebhookNotification(data)

        data = {
            "type": "notification",
            "event": "refund.succeeded",
            "object": 'Invalid object type'
        }

        with self.assertRaises(TypeError):
            RefundWebhookNotification(data)

    def test_notification_factory(self):
        self.maxDiff = None
        body = {
            "type": "notification",
            "event": "refund.succeeded",
            "object": {
                'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
                'payment_id': '21b23365-000f-500b-9000-070fa3554403',
                'created_at': "2017-11-30T15:11:33+00:00",
                'amount': {
                    "value": 250.0,
                    "currency": "RUB"
                },
                'receipt_registration': 'pending',
                'comment': 'test comment',
                'status': 'pending'
            }
        }

        notification = WebhookNotificationFactory().create(body)

        self.assertIsInstance(notification.type, str)
        self.assertIsInstance(notification.event, str)
        self.assertIsInstance(notification.object, RefundResponse)

        body = {
            "type": "notification",
            "event": "payment.waiting_for_capture",
            "object": {
                "id": "22d6d597-000f-5000-9000-145f6df21d6f",
                "status": "waiting_for_capture",
                "paid": True,
                "amount": {
                    "value": "2.00",
                    "currency": "RUB"
                },
                "authorization_details": {
                    "rrn": "10000000000",
                    "auth_code": "000000"
                },
                "created_at": "2018-07-10T14:27:54.691Z",
                "description": "Заказ №72",
                "expires_at": "2018-07-17T14:28:32.484Z",
                "metadata": {},
                "payment_method": {
                    "type": "bank_card",
                    "id": "22d6d597-000f-5000-9000-145f6df21d6f",
                    "saved": False,
                    "card": {
                        "first6": "555555",
                        "last4": "4444",
                        "expiry_month": "07",
                        "expiry_year": "2021",
                        "card_type": "MasterCard",
                        "issuer_country": "RU",
                        "issuer_name": "Sberbank"
                    },
                    "title": "Bank card *4444"
                },
                "refundable": False,
                "test": False
            }
        }

        notification = WebhookNotificationFactory().create(body)

        self.assertIsInstance(notification.type, str)
        self.assertIsInstance(notification.event, str)
        self.assertIsInstance(notification.object, PaymentResponse)

        body = {
            "type": "notification",
            "event": "deal.closed",
            "object": {
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
            }
        }

        notification = WebhookNotificationFactory().create(body)

        self.assertIsInstance(notification.type, str)
        self.assertIsInstance(notification.event, str)
        self.assertIsInstance(notification.object, DealResponse)

        body = {
            "type": "notification",
            "event": "payout.succeeded",
            "object": {
                "id": "po-2855a19a-0003-5000-a000-0efa9e7f4264",
                "amount": {
                    "value": "320.00",
                    "currency": "RUB"
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
            }
        }

        notification = WebhookNotificationFactory().create(body)

        self.assertIsInstance(notification.type, str)
        self.assertIsInstance(notification.event, str)
        self.assertIsInstance(notification.object, PayoutResponse)

        with self.assertRaises(TypeError):
            WebhookNotificationFactory().create('invalid data')

        with self.assertRaises(ValueError):
            WebhookNotificationFactory().create({'invalid': 'data'})
