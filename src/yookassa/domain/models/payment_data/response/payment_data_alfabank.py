# -*- coding: utf-8 -*-
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.payment_data.payment_data import ResponsePaymentData


class PaymentDataAlfabank(ResponsePaymentData):
    __login = None

    def __init__(self, *args, **kwargs):
        super(PaymentDataAlfabank, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.ALFABANK:
            self.type = PaymentMethodType.ALFABANK

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        self.__login = str(value)
