# -*- coding: utf-8 -*-
from yookassa.domain.common.confirmation_type import ConfirmationType
from yookassa.domain.models.confirmation.confirmation import Confirmation


class ConfirmationQr(Confirmation):
    """
    Class representing qr confirmation data object
    """
    __confirmation_data = None

    def __init__(self, *args, **kwargs):
        super(ConfirmationQr, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not ConfirmationType.QR:
            self.type = ConfirmationType.QR

    @property
    def confirmation_data(self):
        return self.__confirmation_data

    @confirmation_data.setter
    def confirmation_data(self, value):
        cast_value = str(value)
        if cast_value:
            self.__confirmation_data = cast_value
        else:
            raise ValueError('Invalid confirmation_data value')
