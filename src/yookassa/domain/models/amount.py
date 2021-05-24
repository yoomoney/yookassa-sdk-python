# -*- coding: utf-8 -*-
from decimal import Decimal, ROUND_HALF_UP

from yookassa.domain.common import BaseObject


class Amount(BaseObject):
    """
    Class representing amount data wrapper object
    """
    __value = None

    __currency = None

    @property
    def value(self):
        """
        :return Decimal:
        """
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = Decimal(str(float(value))).quantize(Decimal('1.11'), rounding=ROUND_HALF_UP)

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = str(value)
