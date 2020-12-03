# -*- coding: utf-8 -*-
from yookassa.domain.common.response_object import ResponseObject
from yookassa.domain.response.refund_response import RefundResponse


class RefundListResponse(ResponseObject):

    __type = None

    __next_cursor = None

    __items = None

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def next_cursor(self):
        return self.__next_cursor

    @next_cursor.setter
    def next_cursor(self, value):
        self.__next_cursor = value

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self.__items = [RefundResponse(refund) for refund in value]
        else:
            self.__items = value
