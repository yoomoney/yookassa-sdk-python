# -*- coding: utf-8 -*-
from yookassa.domain.common.confirmation_type import ConfirmationType
from yookassa.domain.models.confirmation.confirmation import Confirmation


class ConfirmationEmbedded(Confirmation):
    """
    Class representing embedded confirmation data object
    """
    __confirmation_token = None

    def __init__(self, *args, **kwargs):
        super(ConfirmationEmbedded, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not ConfirmationType.EMBEDDED:
            self.type = ConfirmationType.EMBEDDED

    @property
    def confirmation_token(self):
        return self.__confirmation_token

    @confirmation_token.setter
    def confirmation_token(self, value):
        cast_value = str(value)
        if cast_value:
            self.__confirmation_token = cast_value
        else:
            raise ValueError('Invalid confirmation_token value')
