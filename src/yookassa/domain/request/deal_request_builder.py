# -*- coding: utf-8 -*-
from yookassa.domain.request import DealRequest


class DealRequestBuilder(object):
    def __init__(self):
        self.__request = DealRequest()

    def set_type(self, value):
        self.__request.type = value
        return self

    def set_fee_moment(self, value):
        self.__request.fee_moment = value
        return self

    def set_description(self, value):
        self.__request.description = value
        return self

    def set_metadata(self, value):
        self.__request.metadata = value
        return self

    def build(self):
        return self.__request
