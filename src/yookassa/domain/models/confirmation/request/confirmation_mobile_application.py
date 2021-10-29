# -*- coding: utf-8 -*-
from yookassa.domain.common.confirmation_type import ConfirmationType
from yookassa.domain.models.confirmation.request.confirmation_request import ConfirmationRequest


class ConfirmationMobileApplication(ConfirmationRequest):
    """
    Class representing mobile_application confirmation data object
    """
    __return_url = None

    def __init__(self, *args, **kwargs):
        super(ConfirmationMobileApplication, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not ConfirmationType.MOBILE_APPLICATION:
            self.type = ConfirmationType.MOBILE_APPLICATION

    @property
    def return_url(self):
        return self.__return_url

    @return_url.setter
    def return_url(self, value):
        cast_value = str(value)
        if cast_value:
            self.__return_url = cast_value
        else:
            raise ValueError('Invalid returnUrl value')
