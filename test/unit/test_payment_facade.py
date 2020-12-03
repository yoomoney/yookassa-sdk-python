# -*- coding: utf-8 -*-
import sys
import unittest

if sys.version_info >= (3, 3):
    from unittest.mock import patch
else:
    from mock import patch

from yookassa.configuration import Configuration
from yookassa.domain.models.amount import Amount
from yookassa.domain.models.payment_data.response.payment_data_bank_card import PaymentDataBankCard
from yookassa.domain.request.capture_payment_request import CapturePaymentRequest
from yookassa.domain.request.payment_request import PaymentRequest
from yookassa.domain.response.payment_list_response import PaymentListResponse
from yookassa.domain.response.payment_response import PaymentResponse
from yookassa.payment import Payment


class TestPaymentFacade(unittest.TestCase):
    def setUp(self):
        Configuration.configure(account_id='test_account_id', secret_key='test_secret_key')

    def test_create_payment_with_dict(self):
        self.maxDiff = None
        payment_facade = Payment()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                'amount': {'currency': 'RUB', 'value': 1.0},
                'created_at': '2017-11-30T15:45:31.130Z',
                'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
                'metadata': {'float_value': '123.32', 'key': 'data'},
                'paid': False,
                'payment_method': {'type': 'bank_card'},
                'recipient': {'account_id': '156833', 'gateway_id': '468284'},
                'status': 'waiting_for_capture'
            }
            payment = payment_facade.create({
                "amount": {
                    "value": "1.00",
                    "currency": "RUB"
                },
                "receipt": {
                    "items": [
                        {
                            "description": "Item description",
                            "amount": {
                                "value": "1.00",
                                "currency": "RUB"
                            },
                            "quantity": 1,
                            "vat_code": 3
                        }
                    ],
                    "tax_system_id": 2,
                    "email": "test@test.com"
                },
                "payment_method_data": {
                    "type": "bank_card"
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": "https://test.test/test"
                },
                "capture": False,
                "save_payment_method": False,
                "metadata": {
                    "key": "data",
                    "float_value": 123.32
                }
            }, 'asd213')

        self.assertIsInstance(payment, PaymentResponse)
        self.assertIsInstance(payment.amount, Amount)
        self.assertIsInstance(payment.payment_method, PaymentDataBankCard)

    def test_create_payment_with_object(self):
        self.maxDiff = None
        payment_facade = Payment()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                'amount': {'currency': 'RUB', 'value': 1.0},
                'created_at': '2017-11-30T15:45:31.130Z',
                'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
                'metadata': {'float_value': '123.32', 'key': 'data'},
                'paid': False,
                'payment_method': {'type': 'bank_card'},
                'recipient': {'account_id': '156833', 'gateway_id': '468284'},
                'status': 'waiting_for_capture'
            }
            payment = payment_facade.create(PaymentRequest({
                "amount": {
                    "value": "1.00",
                    "currency": "RUB"
                },
                "receipt": {
                    "items": [
                        {
                            "description": "Item description",
                            "amount": {
                                "value": "1.00",
                                "currency": "RUB"
                            },
                            "quantity": 1,
                            "vat_code": 3
                        }
                    ],
                    "tax_system_id": 2,
                    "email": "test@test.com"
                },
                "payment_method_data": {
                    "type": "bank_card"
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": "https://test.test/test"
                },
                "capture": False,
                "save_payment_method": False,
                "metadata": {
                    "key": "data",
                    "float_value": 123.32
                }
            }))

        self.assertIsInstance(payment, PaymentResponse)
        self.assertIsInstance(payment.amount, Amount)
        self.assertIsInstance(payment.payment_method, PaymentDataBankCard)

    def test_create_capture_with_dict(self):
        payment_facade = Payment()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                'amount': {'currency': 'RUB', 'value': 1.0},
                'created_at': '2017-11-30T15:45:31.130Z',
                'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
                'metadata': {'float_value': '123.32', 'key': 'data'},
                'paid': False,
                'payment_method': {'type': 'bank_card'},
                'recipient': {'account_id': '156833', 'gateway_id': '468284'},
                'status': 'waiting_for_capture'
            }

            payment = payment_facade.capture('21b23b5b-000f-5061-a000-0674e49a8c10', {
                "amount": {
                    "value": "1.00",
                    "currency": "RUB"
                },
                "receipt": {
                    "items": [
                        {
                            "description": "Item description",
                            "amount": {
                                "value": "1.00",
                                "currency": "RUB"
                            },
                            "quantity": 1,
                            "vat_code": 3
                        }
                    ],
                    "tax_system_id": 2,
                    "email": "test@test.com"
                },
                "payment_method_data": {
                    "type": "bank_card"
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": "https://test.test/test"
                },
                "capture": False,
                "save_payment_method": False,
                "metadata": {
                    "key": "data",
                    "float_value": 123.32
                }
            }, 'asd213')

        self.assertIsInstance(payment, PaymentResponse)
        self.assertIsInstance(payment.amount, Amount)
        self.assertIsInstance(payment.payment_method, PaymentDataBankCard)

    def test_create_capture_with_object(self):
        payment_facade = Payment()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                'amount': {'currency': 'RUB', 'value': 1.0},
                'created_at': '2017-11-30T15:45:31.130Z',
                'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
                'metadata': {'float_value': '123.32', 'key': 'data'},
                'paid': False,
                'payment_method': {'type': 'bank_card'},
                'recipient': {'account_id': '156833', 'gateway_id': '468284'},
                'status': 'waiting_for_capture'
            }

            payment = payment_facade.capture('21b23b5b-000f-5061-a000-0674e49a8c10', CapturePaymentRequest({
                "amount": {
                    "value": "1.00",
                    "currency": "RUB"
                },
                "receipt": {
                    "items": [
                        {
                            "description": "Item description",
                            "amount": {
                                "value": "1.00",
                                "currency": "RUB"
                            },
                            "quantity": 1,
                            "vat_code": 3
                        }
                    ],
                    "tax_system_id": 2,
                    "email": "test@test.com"
                },
                "payment_method_data": {
                    "type": "bank_card"
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": "https://test.test/test"
                },
                "capture": False,
                "save_payment_method": False,
                "metadata": {
                    "key": "data",
                    "float_value": 123.32
                }
            }))

        self.assertIsInstance(payment, PaymentResponse)
        self.assertIsInstance(payment.amount, Amount)
        self.assertIsInstance(payment.payment_method, PaymentDataBankCard)

    def test_create_capture(self):
        payment_facade = Payment()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                'amount': {'currency': 'RUB', 'value': 1.0},
                'created_at': '2017-11-30T15:45:31.130Z',
                'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
                'metadata': {'float_value': '123.32', 'key': 'data'},
                'paid': False,
                'payment_method': {'type': 'bank_card'},
                'recipient': {'account_id': '156833', 'gateway_id': '468284'},
                'status': 'waiting_for_capture'
            }

            payment = payment_facade.capture('21b23b5b-000f-5061-a000-0674e49a8c10')

        self.assertIsInstance(payment, PaymentResponse)
        self.assertIsInstance(payment.amount, Amount)
        self.assertIsInstance(payment.payment_method, PaymentDataBankCard)

    def test_payment_info(self):
        payment_facade = Payment()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                'amount': {'currency': 'RUB', 'value': 1.0},
                'created_at': '2017-11-30T15:45:31.130Z',
                'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
                'metadata': {'float_value': '123.32', 'key': 'data'},
                'paid': False,
                'payment_method': {'type': 'bank_card'},
                'recipient': {'account_id': '156833', 'gateway_id': '468284'},
                'status': 'waiting_for_capture'
            }
            payment = payment_facade.find_one('21b23b5b-000f-5061-a000-0674e49a8c10')

        self.assertIsInstance(payment, PaymentResponse)
        self.assertIsInstance(payment.amount, Amount)
        self.assertIsInstance(payment.payment_method, PaymentDataBankCard)

    def test_payment_cancel(self):
        payment_facade = Payment()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                'amount': {'currency': 'RUB', 'value': 1.0},
                'created_at': '2017-11-30T15:45:31.130Z',
                'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
                'metadata': {'float_value': '123.32', 'key': 'data'},
                'paid': False,
                'payment_method': {'type': 'bank_card'},
                'recipient': {'account_id': '156833', 'gateway_id': '468284'},
                'status': 'canceled'
            }
            payment = payment_facade.cancel('21b23b5b-000f-5061-a000-0674e49a8c10')

        self.assertIsInstance(payment, PaymentResponse)
        self.assertIsInstance(payment.amount, Amount)
        self.assertIsInstance(payment.payment_method, PaymentDataBankCard)

    def test_payment_list(self):
        payment_facade = Payment()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                'items': [
                    {
                        'amount': {'currency': 'RUB', 'value': 2025.0},
                        'captured_at': '2018-08-02T08:26:26.067Z',
                        'created_at': '2018-08-02T08:25:03.280Z',
                        'description': 'Оплата заказа №69',
                        'id': '22f4d39f-000f-5000-9000-1549325826d3',
                        'metadata': {'module_version': '1.0.13', 'order_id': '69'},
                        'paid': True,
                        'payment_method': {
                            'card': {
                                'card_type': 'Unknown',
                                'expiry_month': '10',
                                'expiry_year': '2020',
                                'last4': '1026'
                            },
                            'id': '22f4d39f-000f-5000-9000-1549325826d3', 'saved': False, 'title': 'BANK_CARD 1026',
                            'type': 'bank_card'
                        },
                        'receipt_registration': 'canceled',
                        'recipient': {'account_id': '502704', 'gateway_id': '1512688'},
                        'refunded_amount': {'value': '0.00', 'currency': 'RUB'},
                        'status': 'succeeded'
                    }
                ],
                'next_page': '2018-08-02 08:24:01.180;48539871',
                'type': 'list'}
            payment = payment_facade.list({
                'status': 'succeeded',
                'limit': 1
            })

            self.assertIsInstance(payment, PaymentListResponse)
            self.assertIsInstance(payment.items, list)

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            Payment().find_one('')

        with self.assertRaises(TypeError):
            Payment().create('invalid params')

        with self.assertRaises(ValueError):
            Payment().capture(111)

        with self.assertRaises(ValueError):
            Payment().cancel('')
