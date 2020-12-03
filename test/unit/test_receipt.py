# -*- coding: utf-8 -*-
import sys
import unittest

from yookassa import Receipt
from yookassa.domain.common import ReceiptType
from yookassa.domain.models import Amount, Currency, ReceiptCustomer, ReceiptItemSupplier
from yookassa.domain.models.settlement import SettlementType, Settlement
from yookassa.domain.request import ReceiptItemRequest, ReceiptRequest
from yookassa.domain.response import ReceiptListResponse, ReceiptResponse

if sys.version_info >= (3, 3):
    from unittest.mock import patch
else:
    from mock import patch

from yookassa.configuration import Configuration


class TestReceipt(unittest.TestCase):

    def setUp(self):
        Configuration.configure(account_id='test_account_id', secret_key='test_secret_key')

    def test_list(self):
        self.maxDiff = None
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "type": "list",
                "items": [
                    {
                        "id": "rt_1da5c87d-0984-50e8-a7f3-8de646dd9ec9",
                        "type": "refund",
                        "refund_id": "215d8da0-000f-50be-b000-0003308c89be",
                        "fiscal_document_number": "3986",
                        "fiscal_storage_number": "9288000100115785",
                        "fiscal_attribute": "2617603921",
                        "registered_at": "2019-05-13T17:56:00.000+03:00",
                        "fiscal_provider_id": "fd9e9404-eaca-4000-8ec9-dc228ead2345",
                        "tax_system_code": 1,
                        "receipt_registration": 'succeeded',
                        "items": None,
                        "settlements": [
                            {
                                "type": "cashless",
                                "amount": {
                                    "value": "45.67",
                                    "currency": "RUB"
                                }
                            }
                        ],
                        "on_behalf_of": "string"
                    }
                ]
            }

            params = {"refund_id": "24be8857-000f-5000-a000-1833ed1577f3"}
            rec_list = Receipt.list(params)

            self.assertIsInstance(rec_list, ReceiptListResponse)
            self.assertEqual(rec_list.type, "list")
            self.assertIsInstance(rec_list.items[0], ReceiptResponse)

    def test_create(self):
        self.maxDiff = None
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                "id": "rt_1da5c87d-0984-50e8-a7f3-8de646dd9ec9",
                "type": "payment",
                "refund_id": "215d8da0-000f-50be-b000-0003308c89be",
                "fiscal_document_number": "3986",
                "fiscal_storage_number": "9288000100115785",
                "fiscal_attribute": "2617603921",
                "registered_at": "2019-05-13T17:56:00.000+03:00",
                "fiscal_provider_id": "fd9e9404-eaca-4000-8ec9-dc228ead2345",
                "tax_system_code": 1,
                "receipt_registration": 'succeeded',
                "items": None,
                "settlements": [
                    {
                        "type": "cashless",
                        "amount": {
                            "value": "45.67",
                            "currency": "RUB"
                        }
                    }
                ],
                "on_behalf_of": "string"
            }

            params = {
                'type': ReceiptType.PAYMENT,
                'send': True,
                'email': 'test@email.com',
                'phone': '79990000000',
                'items': [
                    {
                        'description': 'Product 1',
                        'quantity': 2.0,
                        'amount': Amount({
                            'value': 250.0,
                            'currency': Currency.RUB
                        }),
                        'vat_code': 2,
                        'payment_mode': 'full_payment',
                        'payment_subject': 'commodity',
                        'country_of_origin_code': 'CN',
                        'product_code': '00 00 00 01 00 21 FA 41 00 23 05 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00',
                        'customs_declaration_number': '10714040/140917/0090376',
                        'excise': '20.00',
                        'supplier': {
                            'name': 'string',
                            'phone': 'string',
                            'inn': 'string'
                        }
                    },
                    {
                        'description': 'Product 2',
                        'quantity': 1.0,
                        'amount': {
                            'value': 100.0,
                            'currency': Currency.RUB
                        },
                        'vat_code': 2,
                        'supplier': ReceiptItemSupplier({
                            'name': 'string',
                            'phone': 'string',
                            'inn': 'string'
                        })
                    }
                ],
                'settlements': [
                    {
                        'type': SettlementType.CASHLESS,
                        'amount': {
                            'value': 250.0,
                            'currency': Currency.RUB
                        }
                    }
                ],
                'tax_system_code': 1,
                'payment_id': '215d8da0-000f-50be-b000-0003308c89be',
                'on_behalf_of': 'string'
            }
            rec = Receipt.create(params)

            self.assertIsInstance(rec, ReceiptResponse)
            self.assertEqual(rec.type, ReceiptType.PAYMENT)

            request = ReceiptRequest()
            request.type = ReceiptType.PAYMENT
            request.send = True
            request.customer = ReceiptCustomer({'phone': '79990000000', 'email': 'test@email.com'})
            request.items.append(
                ReceiptItemRequest({
                    "description": "Product 1",
                    "quantity": 2.0,
                    "amount": Amount({'value': 250.0, 'currency': Currency.RUB}),
                    "vat_code": 2
                }))
            request.items.append(
                ReceiptItemRequest({
                    "description": "Product 2",
                    "quantity": 1.0,
                    "amount": Amount({'value': 100.0, 'currency': Currency.RUB}),
                    "vat_code": 2
                }))
            request.settlements.append(
                Settlement({
                    'type': SettlementType.CASHLESS,
                    'amount': Amount({'value': 250.0, 'currency': Currency.RUB})
                }))
            request.tax_system_code = 1
            request.payment_id = '215d8da0-000f-50be-b000-0003308c89be'
            rec = Receipt.create(request)

            self.assertIsInstance(rec, ReceiptResponse)
            self.assertEqual(rec.type, "payment")

        with self.assertRaises(TypeError):
            Receipt.create('invalid data')
