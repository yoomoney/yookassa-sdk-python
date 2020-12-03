# -*- coding: utf-8 -*-
from yookassa.domain.common.request_object import RequestObject
from yookassa.domain.models.airline import Airline
from yookassa.domain.models.amount import Amount
from yookassa.domain.models.receipt import Receipt
from yookassa.domain.models.transfer import Transfer


class CapturePaymentRequest(RequestObject):

    __amount = None

    __receipt = None

    __airline = None

    __transfers = []

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, dict):
            self.__amount = Amount(value)
        elif isinstance(value, Amount):
            self.__amount = value
        else:
            raise TypeError('Invalid amount value type')

    @property
    def receipt(self):
        return self.__receipt

    @receipt.setter
    def receipt(self, value):
        if isinstance(value, dict):
            self.__receipt = Receipt(value)
        elif isinstance(value, Receipt):
            self.__receipt = value
        else:
            raise TypeError('Invalid receipt value type')

    @property
    def airline(self):
        return self.__airline

    @airline.setter
    def airline(self, value):
        if isinstance(value, dict):
            self.__airline = Airline(value)
        elif isinstance(value, Airline):
            self.__airline = value
        else:
            raise TypeError('Invalid airline type')

    @property
    def transfers(self):
        return self.__transfers

    @transfers.setter
    def transfers(self, value):
        if isinstance(value, list):
            self.__transfers = [Transfer(item) for item in value]
        elif value is None:
            self.__transfers = []
        else:
            raise TypeError('Invalid transfers data type in capture_payment_request.transfers')

    def validate(self):
        if self.amount:
            value = self.amount.value
            if not value or value <= 0.0:
                self.__set_validation_error('Invalid amount value: ' + str(value))
        if self.receipt is not None and self.receipt.has_items:
            email = self.receipt.email
            phone = self.receipt.phone
            if not email and not phone:
                self.__set_validation_error('Both email and phone values are empty in receipt')

            if not self.receipt.tax_system_code and any(not item.vat_code for item in self.receipt.items):
                self.__set_validation_error('Item vat_id and receipt tax_system_id not specified')

    def __set_validation_error(self, message):
        raise ValueError(message)
