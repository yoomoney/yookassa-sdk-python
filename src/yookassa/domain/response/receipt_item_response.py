# -*- coding: utf-8 -*-
from decimal import Decimal

from yookassa.domain.common import ResponseObject
from yookassa.domain.models import Amount, ReceiptItemSupplier


class ReceiptItemResponse(ResponseObject):

    __description = None

    __quantity = None

    __amount = None

    __vat_code = None

    __payment_subject = None

    __payment_mode = None

    __supplier = None

    __agent_type = None

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def quantity(self):
        """
        :return Decimal:
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = Decimal(str(float(value)))

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = Amount(value)

    @property
    def vat_code(self):
        return self.__vat_code

    @vat_code.setter
    def vat_code(self, value):
        self.__vat_code = int(value)

    @property
    def payment_subject(self):
        return self.__payment_subject

    @payment_subject.setter
    def payment_subject(self, value):
        self.__payment_subject = str(value)

    @property
    def payment_mode(self):
        return self.__payment_mode

    @payment_mode.setter
    def payment_mode(self, value):
        self.__payment_mode = str(value)

    @property
    def supplier(self):
        return self.__supplier

    @supplier.setter
    def supplier(self, value):
        if isinstance(value, dict):
            self.__supplier = ReceiptItemSupplier(value)
        elif isinstance(value, ReceiptItemSupplier):
            self.__supplier = value
        else:
            raise TypeError('Invalid supplier value type')

    @property
    def agent_type(self):
        return self.__agent_type

    @agent_type.setter
    def agent_type(self, value):
        self.__agent_type = str(value)
