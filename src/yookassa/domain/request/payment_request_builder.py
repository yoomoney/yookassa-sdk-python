# -*- coding: utf-8 -*-
from yookassa.domain.request.payment_request import PaymentRequest


class PaymentRequestBuilder(object):
    def __init__(self):
        self.__request = PaymentRequest()

    def set_recipient(self, value):
        self.__request.recipient = value
        return self

    def set_amount(self, value):
        self.__request.amount = value
        return self

    def set_description(self, value):
        self.__request.description = value
        return self

    def set_receipt(self, value):
        self.__request.receipt = value
        return self

    def set_payment_token(self, value):
        self.__request.payment_token = value
        return self

    def set_payment_method_id(self, value):
        self.__request.payment_method_id = value
        return self

    def set_payment_method_data(self, value):
        self.__request.payment_method_data = value
        return self

    def set_confirmation(self, value):
        self.__request.confirmation = value
        return self

    def set_save_payment_method(self, value):
        self.__request.save_payment_method = value
        return self

    def set_capture(self, value):
        self.__request.capture = value
        return self

    def set_client_ip(self, value):
        self.__request.client_ip = value
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
