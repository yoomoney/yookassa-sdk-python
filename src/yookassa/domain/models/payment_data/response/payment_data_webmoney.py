# -*- coding: utf-8 -*-
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.payment_data.payment_data import ResponsePaymentData


class PaymentDataWebmoney(ResponsePaymentData):
    def __init__(self, *args, **kwargs):
        super(PaymentDataWebmoney, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.WEBMONEY:
            self.type = PaymentMethodType.WEBMONEY
