# -*- coding: utf-8 -*-
import re

from yookassa.domain.common import BaseObject


class ReceiptCustomer(BaseObject):
    """
    Class representing receipt customer data wrapper object

    Used in Receipt
    """
    __full_name = None

    __inn = None

    __email = None

    __phone = None

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = str(value)

    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value):
        self.__inn = str(value)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        cast_value = str(value)
        if re.match(r"^[^@]+@[^@]+\.[^@]+$", cast_value):
            self.__email = cast_value
        else:
            raise ValueError('Invalid email value type')

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = str(value)

