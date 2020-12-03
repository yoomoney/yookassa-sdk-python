# -*- coding: utf-8 -*-
from deprecated import deprecated

from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.payment_data.payment_data import PaymentData


@deprecated("This class will be removed in one of future versions")
class PaymentDataWechat(PaymentData):
    def __init__(self, *args, **kwargs):
        super(PaymentDataWechat, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.WECHAT:
            self.type = PaymentMethodType.WECHAT
