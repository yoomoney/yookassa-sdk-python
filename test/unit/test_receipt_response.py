# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models import Currency
from yookassa.domain.models.receipt_item import PaymentMode, PaymentSubject
from yookassa.domain.models.settlement import Settlement, SettlementType
from yookassa.domain.response.receipt_item_response import ReceiptItemResponse
from yookassa.domain.response.receipt_response import ReceiptResponse


class TestReceiptResponse(unittest.TestCase):

    def test_response_cast_payment(self):
        response = ReceiptResponse({
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
        })

        self.assertIsInstance(response.items, list)
        self.assertIsInstance(response.items[0], ReceiptItemResponse)
        self.assertIsInstance(response.settlements, list)

        self.assertEqual(response.id, 'rt_1da5c87d-0984-50e8-a7f3-8de646dd9ec9')
        self.assertEqual(response.type, 'payment')
        self.assertEqual(response.payment_id, '215d8da0-000f-50be-b000-0003308c89be')
        self.assertEqual(response.status, 'succeeded')
        self.assertEqual(response.receipt_registration, 'succeeded')
        self.assertEqual(response.fiscal_document_number, '3986')
        self.assertEqual(response.fiscal_storage_number, '9288000100115785')
        self.assertEqual(response.fiscal_attribute, '2617603921')
        self.assertEqual(response.registered_at, '2019-05-13T17:56:00.000+03:00')
        self.assertEqual(response.tax_system_code, 1)
        self.assertEqual(response.fiscal_provider_id, 'fd9e9404-eaca-4000-8ec9-dc228ead2345')

        self.assertEqual(response.items[0].description, 'Capybara')
        self.assertEqual(response.items[0].quantity, 5.0)
        self.assertEqual(response.items[0].amount.value, 2500.50)
        self.assertEqual(response.items[0].amount.currency, 'RUB')
        self.assertEqual(response.items[0].vat_code, 2)
        self.assertEqual(response.items[0].payment_mode, PaymentMode.FULL_PAYMENT)
        self.assertEqual(response.items[0].payment_subject, PaymentSubject.COMMODITY)

        self.assertIsNone(response.on_behalf_of)

        self.assertEqual(response.settlements.count(Settlement), 0)

    def test_response_cast_refund(self):
        response = ReceiptResponse({
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
        })

        self.assertIsInstance(response.items, list)
        self.assertIsInstance(response.settlements, list)
        self.assertIsInstance(response.settlements[0], Settlement)

        self.assertEqual(response.id, 'rt_1da5c87d-0984-50e8-a7f3-8de646dd9ec9')
        self.assertEqual(response.type, 'refund')
        self.assertEqual(response.refund_id, '215d8da0-000f-50be-b000-0003308c89be')
        self.assertEqual(response.status, 'succeeded')
        self.assertEqual(response.receipt_registration, 'succeeded')
        self.assertEqual(response.fiscal_document_number, '3986')
        self.assertEqual(response.fiscal_storage_number, '9288000100115785')
        self.assertEqual(response.fiscal_attribute, '2617603921')
        self.assertEqual(response.registered_at, '2019-05-13T17:56:00.000+03:00')
        self.assertEqual(response.tax_system_code, 1)
        self.assertEqual(response.fiscal_provider_id, 'fd9e9404-eaca-4000-8ec9-dc228ead2345')
        self.assertEqual(response.on_behalf_of, 'string')

        self.assertEqual(response.items.count(ReceiptItemResponse), 0)

        self.assertEqual(response.settlements[0].type, SettlementType.CASHLESS)
        self.assertEqual(float(response.settlements[0].amount.value), 45.67)
        self.assertEqual(response.settlements[0].amount.currency, Currency.RUB)
