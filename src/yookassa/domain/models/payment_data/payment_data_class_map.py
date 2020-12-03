# -*- coding: utf-8 -*-
from yookassa.domain.common.data_context import DataContext
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.payment_data.request.payment_data_alfabank import \
    PaymentDataAlfabank as RequestPaymentDataAlfabank
from yookassa.domain.models.payment_data.request.payment_data_applepay import \
    PaymentDataApplepay as RequestPaymentDataApplepay
from yookassa.domain.models.payment_data.request.payment_data_b2b_sberbank import \
    PaymentDataB2bSberbank as RequestPaymentDataB2bSberbank
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
from yookassa.domain.models.payment_data.request.payment_data_tinkoff_bank import \
    PaymentDataTinkoffBank as RequestPaymentDataTinkoffBank
from yookassa.domain.models.payment_data.request.payment_data_webmoney import \
    PaymentDataWebmoney as RequestPaymentDataWebmoney
from yookassa.domain.models.payment_data.request.payment_data_wechat import \
    PaymentDataWechat as RequestPaymentDataWechat
from yookassa.domain.models.payment_data.request.payment_data_yoomoney_wallet import \
    PaymentDataYooMoneyWallet as RequestPaymentDataYooMoneyWallet
from yookassa.domain.models.payment_data.response.payment_data_alfabank import \
    PaymentDataAlfabank as ResponsePaymentDataAlfabank
from yookassa.domain.models.payment_data.response.payment_data_applepay import \
    PaymentDataApplepay as ResponsePaymentDataApplepay
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
from yookassa.domain.models.payment_data.response.payment_data_tinkoff_bank import \
    PaymentDataTinkoffBank as ResponsePaymentDataTinkoffBank
from yookassa.domain.models.payment_data.response.payment_data_webmoney import \
    PaymentDataWebmoney as ResponsePaymentDataWebmoney
from yookassa.domain.models.payment_data.response.payment_data_wechat import \
    PaymentDataWechat as ResponsePaymentDataWechat
from yookassa.domain.models.payment_data.response.payment_data_yoomoney_wallet import \
    PaymentDataYooMoneyWallet as ResponsePaymentDataYooMoneyWallet


class PaymentDataClassMap(DataContext):
    def __init__(self):
        super(PaymentDataClassMap, self).__init__(('request', 'response'))

    @property
    def request(self):
        return {
            PaymentMethodType.ALFABANK: RequestPaymentDataAlfabank,
            PaymentMethodType.BANK_CARD: RequestPaymentDataBankCard,
            PaymentMethodType.CASH: RequestPaymentDataCash,
            PaymentMethodType.MOBILE_BALANCE: RequestPaymentDataMobileBalance,
            PaymentMethodType.SBERBANK: RequestPaymentDataSberbank,
            PaymentMethodType.YOO_MONEY: RequestPaymentDataYooMoneyWallet,
            PaymentMethodType.QIWI: RequestPaymentDataQiwi,
            PaymentMethodType.WEBMONEY: RequestPaymentDataWebmoney,
            PaymentMethodType.APPLEPAY: RequestPaymentDataApplepay,
            PaymentMethodType.GOOGLE_PAY: RequestPaymentDataGooglePay,
            PaymentMethodType.INSTALMENTS: RequestPaymentDataInstallments,
            PaymentMethodType.B2B_SBERBANK: RequestPaymentDataB2bSberbank,
            PaymentMethodType.TINKOFF_BANK: RequestPaymentDataTinkoffBank,
            PaymentMethodType.WECHAT: RequestPaymentDataWechat,
        }

    @property
    def response(self):
        return {
            PaymentMethodType.ALFABANK: ResponsePaymentDataAlfabank,
            PaymentMethodType.BANK_CARD: ResponsePaymentDataBankCard,
            PaymentMethodType.CASH: ResponsePaymentDataCash,
            PaymentMethodType.MOBILE_BALANCE: ResponsePaymentDataMobileBalance,
            PaymentMethodType.SBERBANK: ResponsePaymentDataSberbank,
            PaymentMethodType.YOO_MONEY: ResponsePaymentDataYooMoneyWallet,
            PaymentMethodType.PSB: ResponsePaymentDataPsb,
            PaymentMethodType.QIWI: ResponsePaymentDataQiwi,
            PaymentMethodType.WEBMONEY: ResponsePaymentDataWebmoney,
            PaymentMethodType.APPLEPAY: ResponsePaymentDataApplepay,
            PaymentMethodType.GOOGLE_PAY: ResponsePaymentDataGooglePay,
            PaymentMethodType.INSTALMENTS: ResponsePaymentDataInstallments,
            PaymentMethodType.B2B_SBERBANK: ResponsePaymentDataB2bSberbank,
            PaymentMethodType.TINKOFF_BANK: ResponsePaymentDataTinkoffBank,
            PaymentMethodType.WECHAT: ResponsePaymentDataWechat,
        }
