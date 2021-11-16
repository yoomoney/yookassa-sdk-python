# -*- coding: utf-8 -*-
from yookassa.domain.common import ResponseObject
from yookassa.domain.models import Amount


class DealResponse(ResponseObject):
    """
    Class representing response object.

    Contains data
    """
    __id = None

    __type = None

    __status = None

    __balance = None

    __payout_balance = None

    __description = None

    __fee_moment = None

    __created_at = None

    __expires_at = None

    __test = None

    __metadata = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = Amount(value)

    @property
    def payout_balance(self):
        return self.__payout_balance

    @payout_balance.setter
    def payout_balance(self, value):
        self.__payout_balance = Amount(value)

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def fee_moment(self):
        return self.__fee_moment

    @fee_moment.setter
    def fee_moment(self, value):
        self.__fee_moment = str(value)

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value

    @property
    def expires_at(self):
        return self.__expires_at

    @expires_at.setter
    def expires_at(self, value):
        self.__expires_at = value

    @property
    def test(self):
        return self.__test

    @test.setter
    def test(self, value):
        self.__test = bool(value)

    @property
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
