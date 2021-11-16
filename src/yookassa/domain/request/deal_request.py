# -*- coding: utf-8 -*-
from yookassa.domain.common.request_object import RequestObject

DESCRIPTION_MAX_LENGTH = 128


class DealRequest(RequestObject):

    __type = None

    __fee_moment = None

    __description = None

    __metadata = None

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = str(value)

    @property
    def fee_moment(self):
        return self.__fee_moment

    @fee_moment.setter
    def fee_moment(self, value):
        self.__fee_moment = str(value)

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
                raise ValueError('The value of the description parameter is too long. Max length is {}'.format(
                    DESCRIPTION_MAX_LENGTH))
        else:
            raise ValueError('Invalid description value')

    @property
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        if type(value) is dict:
            self.__metadata = value

    def validate(self):
        if self.type is None:
            self.__set_validation_error('Deal type not specified')

        if self.fee_moment is None:
            self.__set_validation_error('Deal fee_moment not specified')

    def __set_validation_error(self, message):
        raise ValueError(message)
