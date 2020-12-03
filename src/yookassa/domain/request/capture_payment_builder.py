# -*- coding: utf-8 -*-
from yookassa.domain.request.capture_payment_request import CapturePaymentRequest


class CapturePaymentBuilder(object):

    def __init__(self):
        self.__request = CapturePaymentRequest()

    def set_amount(self, value):
        self.__request.amount = value
        return self

    def set_receipt(self, value):
        self.__request.receipt = value
        return self

    def set_airline(self, value):
        self.__request.airline = value
        return self

    def set_metadata(self, value):
        self.__request.metadata = value
        return self

    def set_transfers(self, value):
        self.__request.transfers = value
        return self

    def build(self):
        return self.__request
