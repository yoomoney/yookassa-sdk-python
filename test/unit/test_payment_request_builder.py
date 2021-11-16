# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common.confirmation_type import ConfirmationType
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.settlement import SettlementPayoutType
from yookassa.domain.request.payment_request_builder import PaymentRequestBuilder


class TestPaymentRequestBuilder(unittest.TestCase):

    def test_build_object(self):
        self.maxDiff = None
        request = None
        builder = PaymentRequestBuilder()
        builder.set_receipt({
            'phone': '79990000000',
            'email': 'test@email.com',
            'tax_system_code': 1,
            'items': [
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
            ]}) \
            .set_amount({'value': 0.1, 'currency': Currency.RUB}) \
            .set_recipient({'account_id': '213', 'gateway_id': '123'}) \
            .set_capture(False) \
            .set_save_payment_method(True) \
            .set_confirmation({'type': ConfirmationType.REDIRECT, 'return_url': 'return.url'}) \
            .set_payment_method_data({'type': PaymentMethodType.WEBMONEY}) \
            .set_client_ip('192.0.0.0') \
            .set_payment_method_id('123') \
            .set_payment_token('99091209012') \
            .set_metadata({'key': 'value'}) \
            .set_transfers([
                {
                    'account_id': '79990000000',
                    "amount": {
                        "value": 100.01,
                        "currency": Currency.RUB
                    },
                    "platform_fee_amount": {
                        "value": 10.01,
                        "currency": Currency.RUB
                    },
                    "metadata": {
                        "meta1": 'metatest 1',
                        "meta2": 'metatest 2'
                    }
                }
            ]) \
            .set_deal({
                'id': 'dl-28646d17-0022-5000-8000-01e154d1324b',
                'settlements': [
                    {
                        "type": SettlementPayoutType.PAYOUT,
                        "amount": {
                            "value": "80.00",
                            "currency": Currency.RUB
                        }
                    }
                ]
            }) \
            .set_merchant_customer_id('79990001122')

        request = builder.build()

        self.assertEqual({
            'amount': {'value': '0.10', 'currency': Currency.RUB},
            'recipient': {
                'account_id': '213',
                'gateway_id': '123'
            },
            'save_payment_method': True,
            'capture': False,
            'payment_method_data': {'type': PaymentMethodType.WEBMONEY},
            'receipt': {
                'customer': {'email': 'test@email.com', 'phone': '79990000000'},
                'phone': '79990000000',
                'email': 'test@email.com',
                'tax_system_code': 1,
                'items': [
                    {
                        "description": "Product 1",
                        "quantity": "2.0",
                        "amount": {
                            "value": "250.00",
                            "currency": Currency.RUB
                        },
                        "vat_code": 2
                    },
                    {
                        "description": "Product 2",
                        "quantity": "1.0",
                        "amount": {
                            "value": "100.00",
                            "currency": Currency.RUB
                        },
                        "vat_code": 2
                    }
                ]},
            'payment_method_id': '123',
            'payment_token': '99091209012',
            'confirmation': {'type': ConfirmationType.REDIRECT, 'return_url': 'return.url'},
            'client_ip': '192.0.0.0',
            'metadata': {'key': 'value'},
            'transfers': [{
                'account_id': '79990000000',
                "amount": {
                    "value": "100.01",
                    "currency": Currency.RUB
                },
                "platform_fee_amount": {
                    "value": "10.01",
                    "currency": Currency.RUB
                },
                "metadata": {
                    "meta1": 'metatest 1',
                    "meta2": 'metatest 2'
                }
            }],
            'deal': {
                'id': 'dl-28646d17-0022-5000-8000-01e154d1324b',
                'settlements': [{
                    'type': 'payout',
                    'amount': {
                        'value': "80.00",
                        'currency': 'RUB'
                    }
                }]
            },
            'merchant_customer_id': '79990001122'
        }, dict(request))
