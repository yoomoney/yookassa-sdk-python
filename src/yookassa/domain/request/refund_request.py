# -*- coding: utf-8 -*-
from yookassa.domain.common.request_object import RequestObject
from yookassa.domain.models.amount import Amount
from yookassa.domain.models.receipt import Receipt
from yookassa.domain.models.refund_source import RefundSource


class RefundRequest(RequestObject):

    __payment_id = None

    __amount = None

    __description = None

    __receipt = None

    __sources = []

    @property
    def payment_id(self):
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        cast_value = str(value)
        if len(cast_value) == 36:
            self.__payment_id = cast_value
        else:
            raise ValueError('Invalid payment id value')

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
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        cast_value = str(value)
        if cast_value and len(cast_value) < 256:
            self.__description = cast_value
        else:
            raise ValueError('Invalid commend value')

    @property
    def sources(self):
        return self.__sources

    @sources.setter
    def sources(self, value):
        if isinstance(value, list):
            self.__sources = [RefundSource(item) for item in value]
        elif value is None:
            self.__sources = []
        else:
            raise TypeError('Invalid sources data type in refund_request.sources')

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

    def validate(self):
        if not self.payment_id:
            self.__set_validation_error('Payment id not specified')

        if not self.amount:
            self.__set_validation_error('Amount not specified')

        if self.amount.value <= 0.0:
            self.__set_validation_error('Invalid amount value: ' + str(self.amount.value))

        if self.receipt and self.receipt.has_items():
            email = self.receipt.email
            phone = self.receipt.phone
            if not email and not phone:
                self.__set_validation_error('Both email and phone values are empty in receipt')

            if not self.receipt.tax_system_code and any(not item.vat_code for item in self.receipt.items):
                self.__set_validation_error('Item vat_id and receipt tax_system_id not specified')

    def __set_validation_error(self, message):
        raise ValueError(message)
