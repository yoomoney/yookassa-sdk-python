# -*- coding: utf-8 -*-
from yookassa.domain.common import BaseObject
from yookassa.domain.models.amount import Amount


class Settlement(BaseObject):
    """
    Class representing receipt settlement data wrapper object

    Used in Receipt
    """
    __type = None

    __amount = None

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = str(value)

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


class SettlementType(object):
    """
    Class representing SettlementType values enum
    """
    CASHLESS = 'cashless'
    PREPAYMENT = 'prepayment'
    POSTPAYMENT = 'postpayment'
    CONSIDERATION = 'consideration'


class SettlementPayoutType(object):
    """
    Class representing SettlementPayoutType values enum
    """
    PAYOUT = 'payout'
