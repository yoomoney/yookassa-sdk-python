# -*- coding: utf-8 -*-
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.payment_data.payment_data import PaymentData


class PaymentDataTinkoffBank(PaymentData):
    def __init__(self, *args, **kwargs):
        super(PaymentDataTinkoffBank, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.TINKOFF_BANK:
            self.type = PaymentMethodType.TINKOFF_BANK
