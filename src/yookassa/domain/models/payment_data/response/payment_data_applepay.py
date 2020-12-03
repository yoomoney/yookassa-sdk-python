# -*- coding: utf-8 -*-
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.payment_data.payment_data import ResponsePaymentData


class PaymentDataApplepay(ResponsePaymentData):
    def __init__(self, *args, **kwargs):
        super(PaymentDataApplepay, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.APPLEPAY:
            self.type = PaymentMethodType.APPLEPAY
