# -*- coding: utf-8 -*-
from yookassa.domain.common import BaseObject


class PaymentData(BaseObject):
    """
    Base class for Payment data objects
    """
    __type = None

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = str(value)


class ResponsePaymentData(PaymentData):
    __id = None

    __saved = None

    __title = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = str(value)

    @property
    def saved(self):
        return self.__saved

    @saved.setter
    def saved(self, value):
        self.__saved = bool(value)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = str(value)

