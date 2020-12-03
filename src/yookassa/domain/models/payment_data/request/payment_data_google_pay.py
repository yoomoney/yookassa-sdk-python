# -*- coding: utf-8 -*-
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.payment_data.payment_data import PaymentData


class PaymentDataGooglePay(PaymentData):
    __payment_method_token = None

    __google_transaction_id = None

    def __init__(self, *args, **kwargs):
        super(PaymentDataGooglePay, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.GOOGLE_PAY:
            self.type = PaymentMethodType.GOOGLE_PAY

    @property
    def payment_method_token(self):
        return self.__payment_method_token

    @payment_method_token.setter
    def payment_method_token(self, value):
        self.__payment_method_token = str(value)

    @property
    def google_transaction_id(self):
        return self.__google_transaction_id

    @google_transaction_id.setter
    def google_transaction_id(self, value):
        self.__google_transaction_id = str(value)
