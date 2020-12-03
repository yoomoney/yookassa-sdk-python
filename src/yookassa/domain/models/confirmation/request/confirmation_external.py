# -*- coding: utf-8 -*-
from yookassa.domain.common.confirmation_type import ConfirmationType
from yookassa.domain.models.confirmation.request.confirmation_request import ConfirmationRequest


class ConfirmationExternal(ConfirmationRequest):
    """
    Class representing external confirmation data object
    """

    def __init__(self, *args, **kwargs):
        super(ConfirmationExternal, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not ConfirmationType.EXTERNAL:
            self.type = ConfirmationType.EXTERNAL
