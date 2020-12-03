# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models import Currency
from yookassa.domain.models.receipt_item import PaymentMode, PaymentSubject
from yookassa.domain.response import PaymentListResponse, PaymentResponse, \
    ReceiptListResponse, ReceiptResponse, \
    RefundListResponse, RefundResponse


class TestAnyListResponse(unittest.TestCase):

    def test_response_cast_receipt(self):
        response = ReceiptListResponse({
            "type": "list",
            "items": [
                {
                    "id": "rt_1da5c87d-0984-50e8-a7f3-8de646dd9ec9",
                    "type": "payment",
                    "payment_id": "215d8da0-000f-50be-b000-0003308c89be",
                    "status": "succeeded",
                    "fiscal_document_number": "3986",
                    "fiscal_storage_number": "9288000100115785",
                    "fiscal_attribute": "2617603921",
                    "registered_at": "2019-05-13T17:56:00.000+03:00",
                    "fiscal_provider_id": "fd9e9404-eaca-4000-8ec9-dc228ead2345",
                    "tax_system_code": 1,
                    "items": [{
                        "description": "Capybara",
                        "quantity": 5,
                        "amount": {
                            "value": "2500.50",
                            "currency": "RUB"
                        },
                        "vat_code": 2,
                        "payment_mode": PaymentMode.FULL_PAYMENT,
                        "payment_subject": PaymentSubject.COMMODITY
                    }],
                    "settlements": None
                }
            ],
            "next_cursor": "fda5c87d-5984-50e8-a7f3-1de646dd9ec9"
        })

        self.assertIsInstance(response.items, list)
        self.assertIsInstance(response.items[0], ReceiptResponse)

        self.assertEqual(response.type, 'list')
        self.assertEqual(response.next_cursor, 'fda5c87d-5984-50e8-a7f3-1de646dd9ec9')

    def test_response_cast_refund(self):
        response = RefundListResponse({
            "type": "list",
            "items": [
                {
                    "id": "21b23b5b-000f-5061-a000-0674e49a8c10",
                    "payment_id": "21b23365-000f-500b-9000-070fa3554403",
                    "created_at": "2017-11-30T15:11:33+00:00",
                    "amount": {
                        "value": 250.0,
                        "currency": Currency.RUB
                    },
                    "receipt_registration": "pending",
                    "comment": "test comment",
                    "status": "pending"
                }
            ],
            "next_cursor": "fda5c87d-5984-50e8-a7f3-1de646dd9ec9"
        })

        self.assertIsInstance(response.items, list)
        self.assertIsInstance(response.items[0], RefundResponse)

        self.assertEqual(response.type, 'list')
        self.assertEqual(response.next_cursor, 'fda5c87d-5984-50e8-a7f3-1de646dd9ec9')

    def test_response_cast_payment(self):
        response = PaymentListResponse({
            "type": "list",
            "items": [
                {
                    "id": "21b23365-000f-500b-9000-070fa3554403",
                    "amount": {
                        "value": "1000.00",
                        "currency": "RUB"
                    },
                    "description": "Заказ №72",
                    "confirmation": {
                        "type": "redirect",
                        "return_url": "https://test.test/test",
                        "confirmation_url": "https://url",
                        "enforce": False
                    },
                    "payment_method": {
                        "type": "bank_card",
                        "id": "21b23365-000f-500b-9000-070fa3554403",
                        "saved": False
                    },
                    "status": "pending",
                    "recipient": {
                        "account_id": "67192",
                        "gateway_id": "352780"
                    },
                    "requestor": {
                        "type": "merchant",
                        "account_id": "67192",
                    },
                    "refunded_amount": {
                        "value": "1000.00",
                        "currency": "RUB"
                    },
                    "receipt_registration": "pending",
                    "created_at": "2017-11-30T15:11:33+00:00",
                    "expires_at": "2017-11-30T15:11:33+00:00",
                    "captured_at": "2017-11-30T15:11:33+00:00",
                    "paid": False,
                    "refundable": False,
                    "test": False,
                    "metadata": {
                        "float_value": "123.32",
                        "key": "data"
                    },
                    "cancellation_details": {
                        "party": "yoo_kassa",
                        "reason": "fraud_suspected"
                    },
                    "authorization_details": {
                        "rrn": "rrn",
                        "auth_code": "auth_code"
                    },
                    "transfers": [
                        {
                            "account_id": "79990000000",
                            "amount": {
                                "value": 100.01,
                                "currency": "RUB"
                            },
                            "status": "succeeded"
                        }
                    ],
                    "income_amount": {
                        "value": "990.00",
                        "currency": "RUB"
                    }
                }
            ],
            "next_cursor": "fda5c87d-5984-50e8-a7f3-1de646dd9ec9"
        })

        self.assertIsInstance(response.items, list)
        self.assertIsInstance(response.items[0], PaymentResponse)

        self.assertEqual(response.type, 'list')
        self.assertEqual(response.next_cursor, 'fda5c87d-5984-50e8-a7f3-1de646dd9ec9')
