# -*- coding: utf-8 -*-
from yookassa.domain.common.response_object import ResponseObject
from yookassa.domain.models.amount import Amount
from yookassa.domain.models.refund_source import RefundSource


class RefundResponse(ResponseObject):
    __id = None

    __payment_id = None

    __status = None

    __created_at = None

    __amount = None

    __receipt_registration = None

    __comment = None

    __sources = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def payment_id(self):
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = Amount(value)

    @property
    def receipt_registration(self):
        return self.__receipt_registration

    @receipt_registration.setter
    def receipt_registration(self, value):
        self.__receipt_registration = value

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, value):
        self.__comment = value

    @property
    def sources(self):
        return self.__sources

    @sources.setter
    def sources(self, value):
        if isinstance(value, list):
            self.__sources = [RefundSource(item) for item in value]
        else:
            self.__sources = value
