# -*- coding: utf-8 -*-
import re

from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.payment_data.payment_data import ResponsePaymentData


class PaymentDataCash(ResponsePaymentData):
    __phone = None

    def __init__(self, *args, **kwargs):
        super(PaymentDataCash, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.CASH:
            self.type = PaymentMethodType.CASH

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        cast_value = str(value)
        if re.match('^[0-9]{4,15}$', cast_value):
            self.__phone = cast_value
        else:
            raise ValueError('Invalid phone value type')
