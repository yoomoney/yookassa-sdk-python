# -*- coding: utf-8 -*-
from yookassa.domain.common import BaseObject
from yookassa.domain.models import Settlement


class PaymentDealInfo(BaseObject):
    """
    Class representing PaymentDeal data wrapper object
    """
    __id = None

    __settlements = []

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def settlements(self):
        return self.__settlements

    @settlements.setter
    def settlements(self, value):
        if isinstance(value, list):
            settlements = []
            for item in value:
                if isinstance(item, dict):
                    settlements.append(Settlement(item))
                elif isinstance(item, Settlement):
                    settlements.append(item)
                else:
                    raise TypeError('Invalid item type in deal.settlements')

            self.__settlements = settlements
        elif value is None:
            self.__settlements = []
        else:
            raise TypeError('Invalid settlements value type in PaymentDealInfo')


class PayoutDealInfo(BaseObject):
    """
    Class representing PayoutDeal data wrapper object
    """
    __id = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value


class RefundDealInfo(BaseObject):
    """
    Class representing PaymentDeal data wrapper object
    """
    __id = None

    __refund_settlements = []

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def refund_settlements(self):
        return self.__refund_settlements

    @refund_settlements.setter
    def refund_settlements(self, value):
        if isinstance(value, list):
            settlements = []
            for item in value:
                if isinstance(item, dict):
                    settlements.append(Settlement(item))
                elif isinstance(item, Settlement):
                    settlements.append(item)
                else:
                    raise TypeError('Invalid item type in deal.refund_settlements')

            self.__refund_settlements = settlements
        elif value is None:
            self.__refund_settlements = []
        else:
            raise TypeError('Invalid refund_settlements value type in RefundDealInfo')


class RefundDealData(BaseObject):
    """
    Class representing PaymentDeal data wrapper object
    """
    __refund_settlements = []

    @property
    def refund_settlements(self):
        return self.__refund_settlements

    @refund_settlements.setter
    def refund_settlements(self, value):
        if isinstance(value, list):
            settlements = []
            for item in value:
                if isinstance(item, dict):
                    settlements.append(Settlement(item))
                elif isinstance(item, Settlement):
                    settlements.append(item)
                else:
                    raise TypeError('Invalid item type in deal.refund_settlements')

            self.__refund_settlements = settlements
        elif value is None:
            self.__refund_settlements = []
        else:
            raise TypeError('Invalid refund_settlements value type in RefundDealData')


class DealType:
    """
    Constants representing deal types. Available values are:
    """
    SAFE_DEAL = 'safe_deal'


class DealStatus:
    """
    Constants representing deal statuses. Available values are:
    """
    OPENED = 'opened'
    CLOSED = 'closed'


class FeeMoment:
    """
    Constants representing fee moment types. Available values are:
    """
    PAYMENT_SUCCEEDED = 'payment_succeeded'
    DEAL_CLOSED = 'deal_closed'
