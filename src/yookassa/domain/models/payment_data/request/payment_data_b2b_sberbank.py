# -*- coding: utf-8 -*-
from yookassa.domain.common import BaseObject
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.amount import Amount
from yookassa.domain.models.payment_data.payment_data import PaymentData


class PaymentDataB2bSberbank(PaymentData):
    __payment_purpose = None

    __vat_data = None

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
            raise TypeError('Invalid vat_data value type')


class VatData(BaseObject):
    __type = None

    __rate = None

    __amount = None

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if value in VatDataType.__dict__.values():
            self.__type = str(value)
        else:
            raise ValueError('Invalid type value')

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, value):
        if value in VatDataRate.__dict__.values():
            self.__rate = int(value)
        else:
            raise ValueError('Invalid rate value')

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, dict):
            self.__amount = Amount(value)
        elif isinstance(value, Amount):
            self.__amount = value
        else:
            raise TypeError('Invalid amount value type')


class VatDataType:
    CALCULATED = 'calculated'
    MIXED = 'mixed'
    UNTAXED = 'untaxed'


class VatDataRate:
    """
        Class representing rates available types enum
    """
    RATE_7 = 7
    RATE_10 = 10
    RATE_18 = 18
    RATE_20 = 20
