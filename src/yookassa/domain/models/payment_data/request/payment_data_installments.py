# -*- coding: utf-8 -*-
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.payment_data.payment_data import PaymentData


class PaymentDataInstallments(PaymentData):
    def __init__(self, *args, **kwargs):
        super(PaymentDataInstallments, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.INSTALMENTS:
            self.type = PaymentMethodType.INSTALMENTS
