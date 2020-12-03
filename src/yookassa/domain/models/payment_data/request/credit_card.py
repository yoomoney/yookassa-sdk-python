# -*- coding: utf-8 -*-
import re

from yookassa.domain.common import BaseObject


class CreditCard(BaseObject):
    __number = None

    __expiry_year = None

    __expiry_month = None

    __csc = None

    __cardholder = None

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        cast_value = str(value)
        if re.match(r'^[0-9]{12,19}$', cast_value):
            self.__number = cast_value
        else:
            raise ValueError('Invalid card number value')

    @property
    def expiry_year(self):
        return self.__expiry_year

    @expiry_year.setter
    def expiry_year(self, value):
        cast_value = str(value)
        if re.match(r'^\d\d\d\d$', cast_value) and 2000 < int(cast_value) < 2200:
            self.__expiry_year = cast_value
        else:
            raise ValueError('Invalid card expiry year value')

    @property
    def expiry_month(self):
        return self.__expiry_month

    @expiry_month.setter
    def expiry_month(self, value):
        cast_value = str(value)
        if re.match(r'^\d\d$', cast_value) and 0 < int(cast_value) <= 12:
            self.__expiry_month = cast_value
        else:
            raise ValueError('Invalid card expiry month value')

    @property
    def csc(self):
        return self.__csc

    @csc.setter
    def csc(self, value):
        cast_value = str(value)
        if re.match(r'^\d{3,4}$', cast_value):
            self.__csc = cast_value
        else:
            raise ValueError('Invalid card CSC code value')

    @property
    def cardholder(self):
        return self.__cardholder

    @cardholder.setter
    def cardholder(self, value):
        cast_value = str(value)
        if re.match(r'^[a-zA-Z\s]{1,26}$', cast_value):
            self.__cardholder = cast_value
        else:
            raise ValueError('Invalid card holder value')
