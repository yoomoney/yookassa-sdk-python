# -*- coding: utf-8 -*-
from yookassa.domain.request.receipt_request import ReceiptRequest


class ReceiptRequestBuilder(object):
    def __init__(self):
        self.__request = ReceiptRequest()

    def set_type(self, value):
        self.__request.type = value
        return self

    def set_send(self, value):
        self.__request.send = value
        return self

    def set_customer(self, value):
        self.__request.customer = value
        return self

    def set_tax_system_code(self, value):
        self.__request.tax_system_code = value
        return self

    def set_items(self, value):
        self.__request.items = value
        return self

    def set_settlements(self, value):
        self.__request.settlements = value
        return self

    def set_payment_id(self, value):
        self.__request.payment_id = value
        return self

    def set_refund_id(self, value):
        self.__request.refund_id = value
        return self

    def set_on_behalf_of(self, value):
        self.__request.on_behalf_of = value
        return self

    def build(self):
        return self.__request
