# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common.receipt_type import ReceiptType
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.settlement import Settlement, SettlementType
from yookassa.domain.request.receipt_request_builder import ReceiptRequestBuilder


class TestReceiptRequestBuilder(unittest.TestCase):

    def test_build_object(self):
        self.maxDiff = None
        builder = ReceiptRequestBuilder()
        builder.set_customer({'phone': '79990000000', 'email': 'test@email.com'}) \
            .set_type(ReceiptType.PAYMENT) \
            .set_send(True) \
            .set_tax_system_code(1) \
            .set_items([
                {
                    "description": "Product 1",
                    "quantity": 2.0,
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
                        "value": 100.0,
                        "currency": Currency.RUB
                    },
                    "vat_code": 2
                }
            ]) \
            .set_settlements([
                Settlement({
                    'type': SettlementType.CASHLESS,
                    'amount': {
                        'value': 350.0,
                        'currency': Currency.RUB
                    }
                })
            ]) \
            .set_payment_id('215d8da0-000f-50be-b000-0003308c89be')

        request = builder.build()

        self.assertEqual({
            'customer': {'email': 'test@email.com', 'phone': '79990000000'},
            'type': 'payment',
            'send': True,
            'tax_system_code': 1,
            'email': 'test@email.com',
            'phone': '79990000000',
            'items': [
                {
                    'description': 'Product 1',
                    'quantity': '2.0',
                    'amount': {
                        'value': '250.00',
                        'currency': Currency.RUB
                    },
                    'vat_code': 2
                },
                {
                    'description': 'Product 2',
                    'quantity': '1.0',
                    'amount': {
                        'value': '100.00',
                        'currency': Currency.RUB
                    },
                    'vat_code': 2
                }
            ],
            'settlements': [
                {
                    'type': 'cashless',
                    'amount': {
                        'value': '350.00',
                        'currency': 'RUB'
                    }
                }
            ],
            'payment_id': '215d8da0-000f-50be-b000-0003308c89be'
        }, dict(request))
