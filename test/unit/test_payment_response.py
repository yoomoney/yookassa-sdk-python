# -*- coding: utf-8 -*-
import unittest
from decimal import Decimal

from yookassa.domain.models.amount import Amount
from yookassa.domain.models.authorization_details import AuthorizationDetails
from yookassa.domain.models.cancellation_details import CancellationDetails
from yookassa.domain.models.confirmation.confirmation import Confirmation
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.payment_data.response.payment_data_bank_card import PaymentDataBankCard
from yookassa.domain.models.recipient import Recipient
from yookassa.domain.models.requestor import RequestorMerchant, RequestorType
from yookassa.domain.response.payment_response import PaymentResponse
from yookassa.domain.response.transfer_response import TransferStatus


class TestPaymentResponse(unittest.TestCase):

    def test_response_cast(self):
        self.maxDiff = None
        response = PaymentResponse({
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
                "party": "yookassa",
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
                    "platform_fee_amount": {
                        "value": 10.01,
                        "currency": Currency.RUB
                    },
                    "status": "succeeded",
                    "metadata": {
                        "meta1": 'metatest 1',
                        "meta2": 'metatest 2'
                    }
                }
            ],
            "income_amount": {
                "value": "990.00",
                "currency": "RUB"
            }
        })

        self.assertIsInstance(response.amount, Amount)
        self.assertIsInstance(response.recipient, Recipient)
        self.assertIsInstance(response.requestor, RequestorMerchant)
        self.assertIsInstance(response.payment_method, PaymentDataBankCard)
        self.assertIsInstance(response.confirmation, Confirmation)
        self.assertIsInstance(response.cancellation_details, CancellationDetails)
        self.assertIsInstance(response.authorization_details, AuthorizationDetails)
        self.assertIsInstance(response.transfers, list)
        self.assertIsInstance(response.income_amount, Amount)

        self.assertEqual(response.metadata, {
            "float_value": "123.32",
            "key": "data"
        })
        self.assertFalse(response.paid)
        self.assertFalse(response.refundable)
        self.assertFalse(response.test)
        self.assertEqual(response.id, "21b23365-000f-500b-9000-070fa3554403")
        self.assertEqual(response.status, "pending")
        self.assertEqual(response.amount.value, 1000.00)

        self.assertEqual(response.recipient.account_id, "67192")
        self.assertEqual(response.requestor.type, RequestorType.MERCHANT)
        self.assertEqual(response.requestor.account_id, "67192")

        self.assertEqual(response.description, "Заказ №72")
        self.assertEqual(response.created_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.expires_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.captured_at, "2017-11-30T15:11:33+00:00")
        self.assertEqual(response.receipt_registration, "pending")
        self.assertEqual(dict(response.refunded_amount), {
            "value": Decimal("1000.00"),
            "currency": "RUB"
        })
        self.assertEqual(response.refunded_amount.value, 1000.00)

        self.assertEqual(dict(response.income_amount), {
            "value": Decimal("990.00"),
            "currency": "RUB"
        })
        self.assertEqual(response.income_amount.value, 990.00)

        self.assertEqual(dict(response.transfers[0]), dict({
            "account_id": "79990000000",
            "amount": {
                "value": 100.01,
                "currency": Currency.RUB
            },
            "platform_fee_amount": {
                "value": 10.01,
                "currency": Currency.RUB
            },
            "status": TransferStatus.SUCCEEDED,
            "metadata": {
                "meta1": 'metatest 1',
                "meta2": 'metatest 2'
            }
        }))

        response.transfers = None
        self.assertEqual(response.transfers, None)

        with self.assertRaises(TypeError):
            response.transfers = {}
