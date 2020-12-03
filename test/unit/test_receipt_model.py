# -*- coding: utf-8 -*-
import sys
import unittest
from decimal import Decimal

from yookassa.domain.models.amount import Amount
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.receipt import Receipt
from yookassa.domain.models.receipt_customer import ReceiptCustomer
from yookassa.domain.models.receipt_item import ReceiptItem, PaymentSubject, PaymentMode


class TestReceiptModel(unittest.TestCase):

    def test_receipt_cast(self):
        self.maxDiff = None
        receipt = Receipt()
        receipt.phone = '79990000000'
        receipt.email = 'test@email.com'
        receipt.tax_system_code = 1
        receipt.items = [
            {
                "description": "Product 1",
                "quantity": '2.1',
                "amount": {
                    "value": 250.0,
                    "currency": Currency.RUB
                },
                "vat_code": "2"
            },
            ReceiptItem(
                {
                    "description": "Product 2",
                    "quantity": 1.0,
                    "amount": {
                        "value": '100.01',
                        "currency": Currency.RUB
                    },
                    "vat_code": 2,
                    "payment_subject": PaymentSubject.AGENT_COMMISSION,
                    "payment_mode": PaymentMode.ADVANCE,
                    "product_code": "00 00 00 01 00 21 FA 41 00 23 05 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00",
                    "country_of_origin_code": "RU",
                    "customs_declaration_number": "90/210",
                    "excise": 2.00,
                }
            )

        ]

        self.assertTrue(receipt.has_items())
        self.assertEqual({
            'customer': {
                'phone': '79990000000',
                'email': 'test@email.com',
            },
            'phone': '79990000000',
            'email': 'test@email.com',
            'tax_system_code': 1,
            'items': [
                {
                    "description": "Product 1",
                    "quantity": 2.1,
                    "amount": {
                        "value": 250.0,
                        "currency": Currency.RUB
                    },
                    "vat_code": 2
                },
                {
                    "description": "Product 2",
                    "quantity": 1.0,
                    "amount": {
                        "value": 100.01,
                        "currency": Currency.RUB
                    },
                    "vat_code": 2,
                    'payment_subject': PaymentSubject.AGENT_COMMISSION,
                    'payment_mode': PaymentMode.ADVANCE,
                    "product_code": "00 00 00 01 00 21 FA 41 00 23 05 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00",
                    "country_of_origin_code": "RU",
                    "customs_declaration_number": "90/210",
                    "excise": 2.00,
                }
            ]
        }, dict(receipt))

        customer = ReceiptCustomer({'phone': '79990000000', 'email': 'test@email.com'})
        self.assertEqual({'phone': '79990000000', 'email': 'test@email.com'}, dict(receipt.customer))
        self.assertEqual(dict(customer), dict(receipt.customer))

        with self.assertRaises(TypeError):
            receipt.tax_system_code = 'invalid type'

        with self.assertRaises(TypeError):
            receipt.items = 'invalid items'

        with self.assertRaises(TypeError):
            receipt.items = [
                'invalid item value',
                {
                    "description": "Product 2",
                    "quantity": 1.0,
                    "amount": {
                        "value": 100.0,
                        "currency": Currency.RUB
                    },
                    "vat_code": 2,
                    "payment_subject": PaymentSubject.AGENT_COMMISSION,
                    "payment_mode": PaymentMode.ADVANCE,
                    "product_code": "00 00 00 01 00 21 FA 41 00 23 05 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00",
                    "country_of_origin_code": "RU",
                    "customs_declaration_number": "90/210",
                    "excise": 2.00,
                }
            ]

    def test_receipt_item(self):
        receipt_item = ReceiptItem()
        receipt_item.description = "Product"
        receipt_item.quantity = 1.0
        receipt_item.amount = Amount({
            "value": 100.0,
            "currency": Currency.RUB
        })
        receipt_item.vat_code = 2
        receipt_item.payment_subject = PaymentSubject.AGENT_COMMISSION
        receipt_item.payment_mode = PaymentMode.ADVANCE
        receipt_item.product_code = '00 00 00 01 00 21 FA 41 00 23 05 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00'
        receipt_item.country_of_origin_code = "RU"
        receipt_item.customs_declaration_number = "90/210"
        receipt_item.excise = 2.00

        self.assertEqual({
            "description": "Product",
            "quantity": 1.0,
            "amount": {
                "value": 100.0,
                "currency": Currency.RUB
            },
            "vat_code": 2,
            "payment_subject": PaymentSubject.AGENT_COMMISSION,
            "payment_mode": PaymentMode.ADVANCE,
            "product_code": "00 00 00 01 00 21 FA 41 00 23 05 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00",
            "country_of_origin_code": "RU",
            "customs_declaration_number": "90/210",
            "excise": 2.00,
        }, dict(receipt_item))

        with self.assertRaises(TypeError):
            receipt_item.amount = 'invalid amount'

    @unittest.skipIf(sys.version_info < (3, 0), "Version Python < 3.0")
    def test_decimal_calc(self):
        receipt = Receipt()
        receipt.phone = '79990000000'
        receipt.email = 'test@email.com'
        receipt.tax_system_code = 1
        receipt.items = [
            {
                "description": "Product 1",
                "quantity": '2.1',
                "amount": {
                    "value": 250.0,
                    "currency": Currency.RUB
                },
                "vat_code": "2"
            },
            {
                "description": "Product 2",
                "quantity": 1.0,
                "amount": {
                        "value": '100.01',
                        "currency": Currency.RUB
                    },
                "vat_code": "2"
            }
        ]

        summ = round(receipt.items[0].amount.value * receipt.items[0].quantity, 2)
        self.assertEqual(Decimal('525.00'), Decimal(summ))

        summ = round(receipt.items[1].amount.value * receipt.items[1].quantity, 2)
        self.assertEqual(Decimal('100.01'), Decimal(summ))
