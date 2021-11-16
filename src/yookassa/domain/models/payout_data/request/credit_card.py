# -*- coding: utf-8 -*-
import re

from yookassa.domain.common import BaseObject


class CreditCard(BaseObject):

    __number = None

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
