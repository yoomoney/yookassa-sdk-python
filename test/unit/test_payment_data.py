# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common import PaymentMethodType
from yookassa.domain.models import Currency
from yookassa.domain.models.payment_data.card_type import CardType
from yookassa.domain.models.payment_data.request.credit_card import CreditCard as RequestCreditCard
from yookassa.domain.models.payment_data.request.payment_data_alfabank import \
    PaymentDataAlfabank as RequestPaymentDataAlfabank
from yookassa.domain.models.payment_data.request.payment_data_applepay import \
    PaymentDataApplepay as RequestPaymentDataApplepay
from yookassa.domain.models.payment_data.request.payment_data_b2b_sberbank import \
    PaymentDataB2bSberbank as RequestPaymentDataB2bSberbank, VatDataType, VatDataRate
from yookassa.domain.models.payment_data.request.payment_data_bank_card import \
    PaymentDataBankCard as RequestPaymentDataBankCard
from yookassa.domain.models.payment_data.request.payment_data_cash import \
    PaymentDataCash as RequestPaymentDataCash
from yookassa.domain.models.payment_data.request.payment_data_google_pay import \
    PaymentDataGooglePay as RequestPaymentDataGooglePay
from yookassa.domain.models.payment_data.request.payment_data_installments import \
    PaymentDataInstallments as RequestPaymentDataInstallments
from yookassa.domain.models.payment_data.request.payment_data_mobile_balance import \
    PaymentDataMobileBalance as RequestPaymentDataMobileBalance
from yookassa.domain.models.payment_data.request.payment_data_qiwi import \
    PaymentDataQiwi as RequestPaymentDataQiwi
from yookassa.domain.models.payment_data.request.payment_data_sberbank import \
    PaymentDataSberbank as RequestPaymentDataSberbank
from yookassa.domain.models.payment_data.response.credit_card import CreditCard as ResponseCreditCard
from yookassa.domain.models.payment_data.response.payment_data_alfabank import \
    PaymentDataAlfabank as ResponsePaymentDataAlfabank
from yookassa.domain.models.payment_data.response.payment_data_applepay import \
    PaymentDataApplepay as ResponsePaymentdataApplepay
from yookassa.domain.models.payment_data.response.payment_data_b2b_sberbank import \
    PaymentDataB2bSberbank as ResponsePaymentDataB2bSberbank
from yookassa.domain.models.payment_data.response.payment_data_bank_card import \
    PaymentDataBankCard as ResponsePaymentDataBankCard
from yookassa.domain.models.payment_data.response.payment_data_cash import \
    PaymentDataCash as ResponsePaymentDataCash
from yookassa.domain.models.payment_data.response.payment_data_google_pay import \
    PaymentDataGooglePay as ResponsePaymentDataGooglePay
from yookassa.domain.models.payment_data.response.payment_data_installments import \
    PaymentDataInstallments as ResponsePaymentDataInstallments
from yookassa.domain.models.payment_data.response.payment_data_mobile_balance import \
    PaymentDataMobileBalance as ResponsePaymentDataMobileBalance
from yookassa.domain.models.payment_data.response.payment_data_psb import \
    PaymentDataPsb as ResponsePaymentDataPsb
from yookassa.domain.models.payment_data.response.payment_data_qiwi import \
    PaymentDataQiwi as ResponsePaymentDataQiwi
from yookassa.domain.models.payment_data.response.payment_data_sberbank import \
    PaymentDataSberbank as ResponsePaymentDataSberbank


class TestPaymentData(unittest.TestCase):
    def test_alfabank_cast(self):
        payment_data = RequestPaymentDataAlfabank()
        payment_data.type = PaymentMethodType.ALFABANK
        payment_data.login = 'login'

        self.assertEqual({'type': PaymentMethodType.ALFABANK, 'login': 'login'}, dict(payment_data))

        payment_data = ResponsePaymentDataAlfabank()

        payment_data.type = PaymentMethodType.ALFABANK
        payment_data.login = 'login'

        self.assertEqual({'type': PaymentMethodType.ALFABANK, 'login': 'login'}, dict(payment_data))

    def test_bank_card_cast(self):
        payment_data = RequestPaymentDataBankCard()
        payment_data.type = PaymentMethodType.BANK_CARD
        payment_data.card = RequestCreditCard({
            'number': '8888888888880000',
            'expiry_year': '2018',
            'expiry_month': '10',
            'csc': '111',
            'cardholder': 'test'
        })

        self.assertEqual({'type': PaymentMethodType.BANK_CARD, 'card': {
            'number': '8888888888880000',
            'expiry_year': '2018',
            'expiry_month': '10',
            'csc': '111',
            'cardholder': 'test'
        }}, dict(payment_data))

        payment_data.card = {
            'number': '0000000000008888',
            'expiry_year': '2018',
            'expiry_month': '10',
            'csc': '111',
            'cardholder': 'test'
        }

        self.assertEqual({'type': PaymentMethodType.BANK_CARD, 'card': {
            'number': '0000000000008888',
            'expiry_year': '2018',
            'expiry_month': '10',
            'csc': '111',
            'cardholder': 'test'
        }}, dict(payment_data))

        with self.assertRaises(TypeError):
            payment_data.card = 'invalid type'

        payment_data = ResponsePaymentDataBankCard()
        payment_data.type = PaymentMethodType.BANK_CARD
        payment_data.card = ResponseCreditCard({
            'last4': '0000',
            'expiry_year': '2010',
            'expiry_month': '02',
            'card_type': CardType.VISA
        })

        self.assertEqual({'type': PaymentMethodType.BANK_CARD, 'card': {
            'last4': '0000',
            'expiry_year': '2010',
            'expiry_month': '02',
            'card_type': CardType.VISA
        }}, dict(payment_data))

        payment_data.card = {
            'last4': '0000',
            'expiry_year': '2010',
            'expiry_month': '02',
            'card_type': CardType.VISA
        }

        self.assertEqual({'type': PaymentMethodType.BANK_CARD, 'card': {
            'last4': '0000',
            'expiry_year': '2010',
            'expiry_month': '02',
            'card_type': CardType.VISA
        }}, dict(payment_data))

        with self.assertRaises(TypeError):
            payment_data.card = 'invalid type'

    def test_cash_cast(self):
        payment_data = RequestPaymentDataCash()
        payment_data.type = PaymentMethodType.CASH
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.CASH, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

        payment_data = ResponsePaymentDataCash()
        payment_data.type = PaymentMethodType.CASH
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.CASH, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

    def test_mobile_balance_cast(self):
        payment_data = RequestPaymentDataMobileBalance()
        payment_data.type = PaymentMethodType.MOBILE_BALANCE
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.MOBILE_BALANCE, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

        payment_data = ResponsePaymentDataMobileBalance()
        payment_data.type = PaymentMethodType.MOBILE_BALANCE
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.MOBILE_BALANCE, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

    def test_qiwi_cast(self):
        payment_data = RequestPaymentDataQiwi()
        payment_data.type = PaymentMethodType.QIWI
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.QIWI, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

        payment_data = ResponsePaymentDataQiwi()
        payment_data.type = PaymentMethodType.QIWI
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.QIWI, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

    def test_sberbank_cast(self):
        payment_data = RequestPaymentDataSberbank()
        payment_data.type = PaymentMethodType.SBERBANK
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.SBERBANK, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

        payment_data = ResponsePaymentDataSberbank()
        payment_data.type = PaymentMethodType.SBERBANK
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.SBERBANK, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

    def test_b2b_sberbank_cast(self):
        payment_data = RequestPaymentDataB2bSberbank()
        payment_data.type = PaymentMethodType.B2B_SBERBANK
        payment_data.payment_purpose = 'Test test test'
        payment_data.vat_data = {
            'type': VatDataType.MIXED,
            'rate': VatDataRate.RATE_20,
            'amount': {'value': 10, 'currency': Currency.RUB}
        }

        self.assertEqual({
            'type': PaymentMethodType.B2B_SBERBANK,
            'payment_purpose': 'Test test test',
            'vat_data': {
                'type': VatDataType.MIXED,
                'rate': VatDataRate.RATE_20,
                'amount': {'value': 10.0, 'currency': Currency.RUB}
            }
        }, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.vat_data.type = 'VatDataType.MIXED'

        with self.assertRaises(ValueError):
            payment_data.vat_data.rate = 9

        payment_data = ResponsePaymentDataB2bSberbank()
        payment_data.type = PaymentMethodType.B2B_SBERBANK
        payment_data.payment_purpose = 'Test test test'
        payment_data.vat_data = {
            'type': VatDataType.MIXED,
            'rate': VatDataRate.RATE_20,
            'amount': {'value': 10, 'currency': Currency.RUB}
        }

        self.assertEqual({
            'type': PaymentMethodType.B2B_SBERBANK,
            'payment_purpose': 'Test test test',
            'vat_data': {
                'type': VatDataType.MIXED,
                'rate': VatDataRate.RATE_20,
                'amount': {'value': 10.0, 'currency': Currency.RUB}
            }
        }, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.vat_data = {
                'type': VatDataType.MIXED,
                'rate': 'invalid rate'
            }

        with self.assertRaises(ValueError):
            payment_data.vat_data = {
                'type': 'invalid type',
                'rate': VatDataRate.RATE_20
            }

    def test_applepay_cast(self):
        payment_data = RequestPaymentDataApplepay()
        payment_data.payment_data = 'sampletoken'

        self.assertEqual({'type': PaymentMethodType.APPLEPAY, 'payment_data': 'sampletoken'}, dict(payment_data))

        payment_data = ResponsePaymentdataApplepay()

        self.assertEqual({'type': PaymentMethodType.APPLEPAY}, dict(payment_data))

    def test_google_pay_cast(self):
        payment_data = RequestPaymentDataGooglePay()
        payment_data.payment_method_token = 'sampletoken'
        payment_data.google_transaction_id = 'sampleid'

        self.assertEqual({
            'type': PaymentMethodType.GOOGLE_PAY,
            'payment_method_token': 'sampletoken',
            'google_transaction_id': 'sampleid',
        }, dict(payment_data))

        payment_data = ResponsePaymentDataGooglePay()

        self.assertEqual({'type': PaymentMethodType.GOOGLE_PAY}, dict(payment_data))

    def test_installments_cast(self):
        payment_data = RequestPaymentDataInstallments()
        self.assertEqual({'type': PaymentMethodType.INSTALMENTS}, dict(payment_data))

        payment_data = ResponsePaymentDataInstallments()
        self.assertEqual({'type': PaymentMethodType.INSTALMENTS}, dict(payment_data))

    def test_psb_cast(self):
        payment_data = ResponsePaymentDataPsb()
        self.assertEqual({'type': PaymentMethodType.PSB}, dict(payment_data))
