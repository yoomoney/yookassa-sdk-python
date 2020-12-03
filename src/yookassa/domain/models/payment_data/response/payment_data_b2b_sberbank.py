# -*- coding: utf-8 -*-
from yookassa.domain.common import BaseObject
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.payment_data.payment_data import ResponsePaymentData
from yookassa.domain.models.payment_data.request.payment_data_b2b_sberbank import VatData


class PaymentDataB2bSberbank(ResponsePaymentData):
    __payment_purpose = None

    __vat_data = None

    __payer_bank_details = None

    def __init__(self, *args, **kwargs):
        super(PaymentDataB2bSberbank, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.B2B_SBERBANK:
            self.type = PaymentMethodType.B2B_SBERBANK

    @property
    def payment_purpose(self):
        return self.__payment_purpose

    @payment_purpose.setter
    def payment_purpose(self, value):
        self.__payment_purpose = str(value)

    @property
    def vat_data(self):
        return self.__vat_data

    @vat_data.setter
    def vat_data(self, value):
        if isinstance(value, dict):
            self.__vat_data = VatData(value)
        elif isinstance(value, VatData):
            self.__vat_data = value
        else:
            raise TypeError('Invalid vat_data value type in PaymentDataB2bSberbank')

    @property
    def payer_bank_details(self):
        return self.__payer_bank_details

    @payer_bank_details.setter
    def payer_bank_details(self, value):
        if isinstance(value, dict):
            self.__payer_bank_details = PayerBankDetails(value)
        elif isinstance(value, PayerBankDetails):
            self.__payer_bank_details = value
        else:
            raise TypeError('Invalid payer_bank_details value type in PaymentDataB2bSberbank')


class PayerBankDetails(BaseObject):
    __full_name = None

    __short_name = None

    __address = None

    __inn = None

    __kpp = None

    __bank_name = None

    __bank_branch = None

    __bank_bik = None

    __account = None

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = str(value)

    @property
    def short_name(self):
        return self.__short_name

    @short_name.setter
    def short_name(self, value):
        self.__short_name = str(value)

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = str(value)

    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value):
        self.__inn = str(value)

    @property
    def kpp(self):
        return self.__inn

    @kpp.setter
    def kpp(self, value):
        self.__inn = str(value)

    @property
    def bank_name(self):
        return self.__bank_name

    @bank_name.setter
    def bank_name(self, value):
        self.__bank_name = str(value)

    @property
    def bank_branch(self):
        return self.__bank_branch

    @bank_branch.setter
    def bank_branch(self, value):
        self.__bank_branch = str(value)

    @property
    def bank_bik(self):
        return self.__bank_bik

    @bank_bik.setter
    def bank_bik(self, value):
        self.__bank_bik = str(value)

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value):
        self.__account = str(value)
