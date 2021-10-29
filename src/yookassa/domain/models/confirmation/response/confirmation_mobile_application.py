# -*- coding: utf-8 -*-
from yookassa.domain.common.confirmation_type import ConfirmationType
from yookassa.domain.models.confirmation.confirmation import Confirmation


class ConfirmationMobileApplication(Confirmation):
    """
    Class representing mobile_application confirmation data object
    """
    __confirmation_url = None

    def __init__(self, *args, **kwargs):
        super(ConfirmationMobileApplication, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not ConfirmationType.MOBILE_APPLICATION:
            self.type = ConfirmationType.MOBILE_APPLICATION

    @property
    def confirmation_url(self):
        return self.__confirmation_url

    @confirmation_url.setter
    def confirmation_url(self, value):
        self.__confirmation_url = value
