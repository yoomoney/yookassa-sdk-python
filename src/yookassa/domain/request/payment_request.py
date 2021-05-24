# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.common.request_object import RequestObject
from yookassa.domain.models.airline import Airline
from yookassa.domain.models.amount import Amount
from yookassa.domain.models.confirmation.confirmation import Confirmation
from yookassa.domain.models.confirmation.confirmation_factory import ConfirmationFactory
from yookassa.domain.models.payment_data.payment_data import PaymentData
from yookassa.domain.models.payment_data.payment_data_factory import PaymentDataFactory
from yookassa.domain.models.receipt import Receipt
from yookassa.domain.models.recipient import Recipient
from yookassa.domain.models.transfer import Transfer

DESCRIPTION_MAX_LENGTH = 128


class PaymentRequest(RequestObject):
    __recipient = None

    __amount = None

    __description = None

    __receipt = None

    __payment_token = None

    __payment_method_id = None

    __payment_method_data = None

    __confirmation = None

    __save_payment_method = None

    __capture = None

    __client_ip = None

    __airline = None

    __metadata = None

    __transfers = []

    @property
    def recipient(self):
        return self.__recipient

    @recipient.setter
    def recipient(self, value):
        if isinstance(value, dict):
            self.__recipient = Recipient(value)
        elif isinstance(value, Recipient):
            self.__recipient = value
        else:
            raise TypeError('Invalid recipient value type')

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
        if cast_value:
            if len(cast_value) <= DESCRIPTION_MAX_LENGTH:
                self.__description = cast_value
            else:
                raise ValueError('The value of the description parameter is too long. Max length is {}'.format(DESCRIPTION_MAX_LENGTH))
        else:
            raise ValueError('Invalid description value')

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
            raise TypeError('Invalid receipt_request value type')

    @property
    def payment_token(self):
        return self.__payment_token

    @payment_token.setter
    def payment_token(self, value):
        cast_value = str(value)
        if cast_value:
            self.__payment_token = cast_value
        else:
            raise TypeError('Invalid payment_token value')

    @property
    def payment_method_id(self):
        return self.__payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, value):
        cast_value = str(value)
        if cast_value:
            self.__payment_method_id = cast_value

    @property
    def payment_method_data(self):
        return self.__payment_method_data

    @payment_method_data.setter
    def payment_method_data(self, value):
        if isinstance(value, dict):
            self.__payment_method_data = PaymentDataFactory().create(value, self.context())
        elif isinstance(value, PaymentData):
            self.__payment_method_data = value
        else:
            raise TypeError('Invalid payment_method_data type')

    @property
    def confirmation(self):
        return self.__confirmation

    @confirmation.setter
    def confirmation(self, value):
        if isinstance(value, dict):
            self.__confirmation = ConfirmationFactory().create(value, self.context())
        elif isinstance(value, Confirmation):
            self.__confirmation = value
        else:
            raise TypeError('Invalid confirmation type')

    @property
    def save_payment_method(self):
        return self.__save_payment_method

    @save_payment_method.setter
    def save_payment_method(self, value):
        self.__save_payment_method = bool(value)

    @property
    def capture(self):
        return self.__capture

    @capture.setter
    def capture(self, value):
        self.__capture = bool(value)

    @property
    def client_ip(self):
        return self.__client_ip

    @client_ip.setter
    def client_ip(self, value):
        self.__client_ip = str(value)

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
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        if type(value) is dict:
            self.__metadata = value

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
            raise TypeError('Invalid transfers data type in payment_request.transfers')

    def validate(self):
        amount = self.amount
        if amount is None:
            self.__set_validation_error('Payment amount not specified')

        if amount.value <= 0.0:
            self.__set_validation_error('Invalid payment amount value: ' + str(amount.value))

        if self.receipt is not None and self.receipt.has_items:
            email = self.receipt.email
            phone = self.receipt.phone
            if not email and not phone:
                self.__set_validation_error('Both email and phone values are empty in receipt')

            if self.receipt.tax_system_code is None:
                for item in self.receipt.items:
                    if item.vat_code is None:
                        self.__set_validation_error('Item vat_code and receipt tax_system_id not specified')

        if self.payment_token:
            if self.payment_method_id:
                self.__set_validation_error('Both payment_token and payment_method_id values are specified')

            if self.payment_method_data:
                self.__set_validation_error('Both payment_token and payment_data values are specified')

        elif self.payment_method_id:
            if self.payment_method_data:
                self.__set_validation_error('Both payment_method_id and payment_data values are specified')

        if self.payment_method_data and self.payment_method_data.type == PaymentMethodType.BANK_CARD \
                and self.payment_method_data.card is not None:
            # Get current date with an offset.
            # Why? Because expiration is relative to the transaction
            # processor's timezone, which we don't know. 1 day allowance will
            # prevent any sorts of false negatives, leaving a small
            # less-than-day window for the unlikely false positives.
            # Account for GMT-12 to GMT+14 difference
            # + DST: https://www.timeanddate.com/time/dst/
            date_now = datetime.now() - timedelta(hours=26 + 1)

            # Expiry date is "valid thru", meaning it is valid until the last
            # second of the last day of the month in the date.
            date_expiry = datetime(
                year=int(self.payment_method_data.card.expiry_year),
                month=int(self.payment_method_data.card.expiry_month),
                day=1
            )
            # A little trick to add a month
            date_expiry += timedelta(days=31)
            date_expiry -= timedelta(days=date_expiry.day - 1)

            if date_now >= date_expiry:
                self.__set_validation_error('Card expired')

    def __set_validation_error(self, message):
        raise ValueError(message)
