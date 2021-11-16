# -*- coding: utf-8 -*-
from yookassa.domain.request import PayoutRequest


class PayoutRequestBuilder(object):
    def __init__(self):
        self.__request = PayoutRequest()

    def set_amount(self, value):
        self.__request.amount = value
        return self

    def set_description(self, value):
        self.__request.description = value
        return self

    def set_payout_token(self, value):
        self.__request.payout_token = value
        return self

    def set_payout_destination_data(self, value):
        self.__request.payout_destination_data = value
        return self

    def set_deal(self, value):
        self.__request.deal = value
        return self

    def set_metadata(self, value):
        self.__request.metadata = value
        return self

    def build(self):
        return self.__request
