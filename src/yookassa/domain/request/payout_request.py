# -*- coding: utf-8 -*-
from yookassa.domain.common.request_object import RequestObject
from yookassa.domain.models.amount import Amount
from yookassa.domain.models.deal import PayoutDealInfo
from yookassa.domain.models.payout_data.payout_destination import PayoutDestination
from yookassa.domain.models.payout_data.payout_destination_factory import PayoutDestinationFactory

DESCRIPTION_MAX_LENGTH = 128


class PayoutRequest(RequestObject):
    """
    Class representing PayoutRequest values enum
    """

    __amount = None

    __description = None

    __payout_destination_data = None

    __payout_token = None

    __deal = None

    __metadata = None

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

    @property
    def payout_destination_data(self):
        return self.__payout_destination_data

    @payout_destination_data.setter
    def payout_destination_data(self, value):
        if isinstance(value, dict):
            self.__payout_destination_data = PayoutDestinationFactory().create(value, self.context())
        elif isinstance(value, PayoutDestination):
            self.__payout_destination_data = value
        else:
            raise TypeError('Invalid payout_destination_data type')

    @property
    def payout_token(self):
        return self.__payout_token

    @payout_token.setter
    def payout_token(self, value):
        cast_value = str(value)
        if cast_value:
            self.__payout_token = cast_value
        else:
            raise TypeError('Invalid payout_token value')

    @description.setter
    def description(self, value):
        cast_value = str(value)
        if cast_value:
            if len(cast_value) <= DESCRIPTION_MAX_LENGTH:
                self.__description = cast_value
            else:
                raise ValueError('The value of the description parameter is too long. Max length is {}'.format(
                    DESCRIPTION_MAX_LENGTH))
        else:
            raise ValueError('Invalid description value')

    @property
    def deal(self):
        return self.__deal

    @deal.setter
    def deal(self, value):
        if isinstance(value, dict):
            self.__deal = PayoutDealInfo(value)
        elif isinstance(value, PayoutDealInfo):
            self.__deal = value
        else:
            raise TypeError('Invalid deal type')

    @property
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        if type(value) is dict:
            self.__metadata = value

    def validate(self):
        amount = self.amount
        if amount is None:
            self.__set_validation_error('Payout amount not specified')

        if amount.value <= 0.0:
            self.__set_validation_error('Invalid payout amount value: ' + str(amount.value))

        if self.payout_token:
            if self.payout_destination_data:
                self.__set_validation_error('Both payout_token and payout_destination_data values are specified')

        elif self.payout_token is None:
            if self.payout_destination_data is None:
                self.__set_validation_error('Both payout_token and payout_destination_data values are not specified')

    def __set_validation_error(self, message):
        raise ValueError(message)
