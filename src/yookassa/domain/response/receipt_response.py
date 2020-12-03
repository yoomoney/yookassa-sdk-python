# -*- coding: utf-8 -*-
from yookassa.domain.common import ResponseObject
from yookassa.domain.models import Settlement
from yookassa.domain.response import ReceiptItemResponse


class ReceiptResponse(ResponseObject):
    """
    Class representing response object.

    Contains data
    """
    __id = None

    __type = None

    __refund_id = None

    __payment_id = None

    __status = None

    __fiscal_document_number = None

    __fiscal_storage_number = None

    __fiscal_attribute = None

    __registered_at = None

    __fiscal_provider_id = None

    __tax_system_code = None

    __items = []

    __settlements = []

    __on_behalf_of = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = str(value)

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = str(value)

    @property
    def payment_id(self):
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = str(value)

    @property
    def refund_id(self):
        return self.__refund_id

    @refund_id.setter
    def refund_id(self, value):
        self.__refund_id = str(value)

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = str(value)

    @property
    def receipt_registration(self):
        return self.status

    @receipt_registration.setter
    def receipt_registration(self, value):
        self.status = value

    @property
    def fiscal_document_number(self):
        return self.__fiscal_document_number

    @fiscal_document_number.setter
    def fiscal_document_number(self, value):
        self.__fiscal_document_number = str(value)

    @property
    def fiscal_storage_number(self):
        return self.__fiscal_storage_number

    @fiscal_storage_number.setter
    def fiscal_storage_number(self, value):
        self.__fiscal_storage_number = str(value)

    @property
    def fiscal_attribute(self):
        return self.__fiscal_attribute

    @fiscal_attribute.setter
    def fiscal_attribute(self, value):
        self.__fiscal_attribute = str(value)

    @property
    def registered_at(self):
        return self.__registered_at

    @registered_at.setter
    def registered_at(self, value):
        self.__registered_at = value

    @property
    def fiscal_provider_id(self):
        return self.__fiscal_provider_id

    @fiscal_provider_id.setter
    def fiscal_provider_id(self, value):
        self.__fiscal_provider_id = str(value)

    @property
    def tax_system_code(self):
        return self.__tax_system_code

    @tax_system_code.setter
    def tax_system_code(self, value):
        self.__tax_system_code = int(value)

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self.__items = [ReceiptItemResponse(item) for item in value]
        else:
            self.__items = []

    @property
    def settlements(self):
        return self.__settlements

    @settlements.setter
    def settlements(self, value):
        if isinstance(value, list):
            self.__settlements = [Settlement(item) for item in value]
        else:
            self.__settlements = []

    @property
    def on_behalf_of(self):
        return self.__on_behalf_of

    @on_behalf_of.setter
    def on_behalf_of(self, value):
        self.__on_behalf_of = str(value)
