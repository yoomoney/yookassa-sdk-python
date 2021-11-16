# -*- coding: utf-8 -*-
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.payout_data.payout_destination import PayoutDestination


class PayoutDestinationYooMoneyWallet(PayoutDestination):

    __account_number = None

    def __init__(self, *args, **kwargs):
        super(PayoutDestinationYooMoneyWallet, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.YOO_MONEY:
            self.type = PaymentMethodType.YOO_MONEY

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, value):
        self.__account_number = str(value)
