# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models.requestor import RequestorThirdPartyClient, RequestorMerchant, RequestorFactory


class TestRequestor(unittest.TestCase):

    # def test_notification_payment(self):
    #     self.maxDiff = None
    #     notification = WebhookNotification({
    #         "type": "notification",
    #         "event": "payment.waiting_for_capture",
    #         "object": {
    #             "id": "22d6d597-000f-5000-9000-145f6df21d6f",
    #             "status": "waiting_for_capture",
    #             "paid": True,
    #             "amount": {
    #                 "value": "2.00",
    #                 "currency": "RUB"
    #             },
    #             "authorization_details": {
    #                 "rrn": "10000000000",
    #                 "auth_code": "000000"
    #             },
    #             "created_at": "2018-07-10T14:27:54.691Z",
    #             "description": "Заказ №72",
    #             "expires_at": "2018-07-17T14:28:32.484Z",
    #             "metadata": {},
    #             "payment_method": {
    #                 "type": "bank_card",
    #                 "id": "22d6d597-000f-5000-9000-145f6df21d6f",
    #                 "saved": False,
    #                 "card": {
    #                     "first6": "555555",
    #                     "last4": "4444",
    #                     "expiry_month": "07",
    #                     "expiry_year": "2021",
    #                     "card_type": "MasterCard",
    #                     "issuer_country": "RU",
    #                     "issuer_name": "Sberbank"
    #                 },
    #                 "title": "Bank card *4444"
    #             },
    #             "refundable": False,
    #             "test": False
    #         }
    #     })
    #
    #     self.assertIsInstance(notification.type, str)
    #     self.assertIsInstance(notification.event, str)
    #     self.assertIsInstance(notification.object, PaymentResponse)
    #
    #     data = {
    #         "type": "notification",
    #         "event": "payment.waiting_for_capture",
    #         "object": {}
    #     }
    #
    #     with self.assertRaises(ValueError):
    #         WebhookNotification(data)
    #
    #     data = {
    #         "type": "notification",
    #         "event": "payment.waiting_for_capture",
    #         "object": 'Invalid object type'
    #     }
    #
    #     with self.assertRaises(TypeError):
    #         WebhookNotification(data)
    #
    # def test_notification_refund(self):
    #     self.maxDiff = None
    #     notification = RefundWebhookNotification({
    #         "type": "notification",
    #         "event": "refund.succeeded",
    #         "object": {
    #             'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
    #             'payment_id': '21b23365-000f-500b-9000-070fa3554403',
    #             'created_at': "2017-11-30T15:11:33+00:00",
    #             'amount': {
    #                 "value": 250.0,
    #                 "currency": "RUB"
    #             },
    #             'receipt_registration': 'pending',
    #             'comment': 'test comment',
    #             'status': 'pending'
    #         }
    #     })
    #
    #     self.assertIsInstance(notification.type, str)
    #     self.assertIsInstance(notification.event, str)
    #     self.assertIsInstance(notification.object, Requestor)
    #
    #     data = {
    #         "type": "notification",
    #         "event": "refund.succeeded",
    #         "object": {}
    #     }
    #
    #     with self.assertRaises(ValueError):
    #         RefundWebhookNotification(data)
    #
    #     data = {
    #         "type": "notification",
    #         "event": "refund.succeeded",
    #         "object": 'Invalid object type'
    #     }
    #
    #     with self.assertRaises(TypeError):
    #         RefundWebhookNotification(data)

    def test_requestor_factory(self):
        self.maxDiff = None
        body = {
            "type": "third_party_client",
            "client_id": "123456",
            "client_name": "Merchant App"
        }

        requestor = RequestorFactory().create(body)

        self.assertIsInstance(requestor, RequestorThirdPartyClient)
        self.assertIsInstance(requestor.type, str)
        self.assertIsInstance(requestor.client_id, str)
        self.assertIsInstance(requestor.client_name, str)

        body = {
            "type": "merchant",
            "account_id": "67192",
        }

        requestor = RequestorFactory().create(body)

        self.assertIsInstance(requestor, RequestorMerchant)
        self.assertIsInstance(requestor.type, str)
        self.assertIsInstance(requestor.account_id, str)

        with self.assertRaises(TypeError):
            RequestorFactory().create('invalid data')

        with self.assertRaises(ValueError):
            RequestorFactory().create({'invalid': 'data'})
