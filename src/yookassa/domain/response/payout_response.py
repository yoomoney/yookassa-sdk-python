# -*- coding: utf-8 -*-
from yookassa.domain.common import ResponseObject
from yookassa.domain.models import Amount, CancellationDetails
from yookassa.domain.models.deal import PayoutDealInfo
from yookassa.domain.models.payout_data.payout_destination_factory import PayoutDestinationFactory


class PayoutResponse(ResponseObject):
    """
    Class representing response object.

    Contains data
    """
    __id = None

    __amount = None

    __status = None

    __payout_destination = None

    __description = None

    __created_at = None

    __deal = None

    __cancellation_details = None

    __metadata = None

    __test = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = Amount(value)

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def payout_destination(self):
        return self.__payout_destination

    @payout_destination.setter
    def payout_destination(self, value):
        self.__payout_destination = PayoutDestinationFactory().create(value, self.context())

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value

    @property
    def deal(self):
        return self.__deal

    @deal.setter
    def deal(self, value):
        self.__deal = PayoutDealInfo(value)

    @property
    def cancellation_details(self):
        return self.__cancellation_details

    @cancellation_details.setter
    def cancellation_details(self, value):
        self.__cancellation_details = CancellationDetails(value)

    @property
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value

    @property
    def test(self):
        return self.__test

    @test.setter
    def test(self, value):
        self.__test = bool(value)
