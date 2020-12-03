# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common.receipt_type import ReceiptType
from yookassa.domain.models import Amount, Currency, ReceiptCustomer, ReceiptItemSupplier
from yookassa.domain.models.settlement import SettlementType, Settlement
from yookassa.domain.request.receipt_item_request import ReceiptItemRequest
from yookassa.domain.request.receipt_request import ReceiptRequest


class TestReceiptRequest(unittest.TestCase):

    def test_request_cast(self):
        request = ReceiptRequest()
        request.type = ReceiptType.PAYMENT
        request.send = True
        request.customer = ReceiptCustomer({'phone': '79990000000', 'email': 'test@email.com'})
        request.items = [
            ReceiptItemRequest({
                "description": "Product 1",
                "quantity": 2.0,
                "amount": {
                    "value": 250.0,
                    "currency": Currency.RUB
                },
                "vat_code": 2
            }),
            ReceiptItemRequest({
                "description": "Product 2",
                "quantity": 1.0,
                "amount": {
                    "value": 100.0,
                    "currency": Currency.RUB
                },
                "vat_code": 2
            })
        ]
        request.settlements = [
            Settlement({
                'type': SettlementType.CASHLESS,
                'amount': {
                    'value': 250.0,
                    'currency': Currency.RUB
                }
            })
        ]
        request.tax_system_code = 1
        request.payment_id = '215d8da0-000f-50be-b000-0003308c89be'

        self.assertEqual({
            'type': ReceiptType.PAYMENT,
            'send': True,
            'customer': {'email': 'test@email.com', 'phone': '79990000000'},
            'email': 'test@email.com',
            'phone': '79990000000',
            'items': [
                {
                    'description': 'Product 1',
                    'quantity': 2.0,
                    'amount': {
                        'value': 250.0,
                        'currency': Currency.RUB
                    },
                    'vat_code': 2
                },
                {
                    'description': 'Product 2',
                    'quantity': 1.0,
                    'amount': {
                        'value': 100.0,
                        'currency': Currency.RUB
                    },
                    'vat_code': 2
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
            'payment_id': '215d8da0-000f-50be-b000-0003308c89be'
        }, dict(request))

    def test_request_setters(self):
        request = ReceiptRequest({
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
        })

        self.assertIsInstance(request.customer, ReceiptCustomer)
        self.assertIsInstance(request.items, list)
        self.assertIsInstance(request.settlements, list)

        with self.assertRaises(TypeError):
            request.items[0].supplier = 'invalid supplier'

        with self.assertRaises(TypeError):
            request.items[0].amount = 'invalid amount'

        with self.assertRaises(TypeError):
            request.customer = 'invalid customer'

        with self.assertRaises(TypeError):
            request.items = 'invalid items'

        with self.assertRaises(TypeError):
            request.items = ['invalid item']

        with self.assertRaises(TypeError):
            request.settlements = 'invalid settlements'

        with self.assertRaises(TypeError):
            request.settlements = ['invalid settlement']

        with self.assertRaises(TypeError):
            request.send = 'invalid send'

        with self.assertRaises(TypeError):
            request.tax_system_code = 'invalid tax_system_code'

    def test_request_validate(self):
        request = ReceiptRequest()

        with self.assertRaises(ValueError):
            request.validate()

        request.type = ReceiptType.PAYMENT

        with self.assertRaises(ValueError):
            request.validate()

        request.send = True

        with self.assertRaises(ValueError):
            request.validate()

        request.customer = ReceiptCustomer({'phone': '79990000000', 'email': 'test@email.com'})

        with self.assertRaises(ValueError):
            request.validate()

        request.items = [
            ReceiptItemRequest({
                "description": "Product 1",
                "quantity": 2.0,
                "amount": {
                    "value": 250.0,
                    "currency": Currency.RUB
                },
                "vat_code": 2
            }),
            ReceiptItemRequest({
                "description": "Product 2",
                "quantity": 1.0,
                "amount": {
                    "value": 100.0,
                    "currency": Currency.RUB
                },
                "vat_code": 2
            })
        ]

        with self.assertRaises(ValueError):
            request.validate()

        request.settlements = [
            Settlement({
                'type': SettlementType.CASHLESS,
                'amount': {
                    'value': 250.0,
                    'currency': Currency.RUB
                }
            })
        ]

        with self.assertRaises(ValueError):
            request.validate()

        request.tax_system_code = 1

        with self.assertRaises(ValueError):
            request.validate()

        request.refund_id = '215d8da0-000f-50be-b000-0003308c89be'

        with self.assertRaises(ValueError):
            request.validate()

        request.type = ReceiptType.REFUND
        request.payment_id = '215d8da0-000f-50be-b000-0003308c89be'

        with self.assertRaises(ValueError):
            request.validate()

        request.items = None
        request.settlements = None
        with self.assertRaises(ValueError):
            request.validate()
