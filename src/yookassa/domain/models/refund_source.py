# -*- coding: utf-8 -*-
from yookassa.domain.common import BaseObject
from yookassa.domain.models.amount import Amount


class RefundSource(BaseObject):
    """
    Class representing refund source wrapper object

    Used in Refund
    """
    __account_id = None

    __amount = None

    __platform_fee_amount = None

    @property
    def account_id(self):
        return self.__account_id

    @account_id.setter
    def account_id(self, value):
        self.__account_id = str(value)

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

    @property
    def platform_fee_amount(self):
        return self.__platform_fee_amount

    @platform_fee_amount.setter
    def platform_fee_amount(self, value):
        if isinstance(value, dict):
            self.__platform_fee_amount = Amount(value)
        elif isinstance(value, Amount):
            self.__platform_fee_amount = value
        else:
            raise TypeError('Invalid platform_fee_amount value type')
