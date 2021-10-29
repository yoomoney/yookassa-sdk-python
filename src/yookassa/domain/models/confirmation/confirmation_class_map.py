# -*- coding: utf-8 -*-
from yookassa.domain.common.confirmation_type import ConfirmationType
from yookassa.domain.common.data_context import DataContext
from yookassa.domain.models.confirmation.request.confirmation_embedded import \
    ConfirmationEmbedded as RequestConfirmationEmbedded
from yookassa.domain.models.confirmation.request.confirmation_external import \
    ConfirmationExternal as RequestConfirmationExternal
from yookassa.domain.models.confirmation.request.confirmation_qr import \
    ConfirmationQr as RequestConfirmationQr
from yookassa.domain.models.confirmation.request.confirmation_redirect import \
    ConfirmationRedirect as RequestConfirmationRedirect
from yookassa.domain.models.confirmation.request.confirmation_mobile_application import \
    ConfirmationMobileApplication as RequestConfirmationMobileApplication
from yookassa.domain.models.confirmation.response.confirmation_embedded import \
    ConfirmationEmbedded as ResponseConfirmationEmbedded
from yookassa.domain.models.confirmation.response.confirmation_external import \
    ConfirmationExternal as ResponseConfirmationExternal
from yookassa.domain.models.confirmation.response.confirmation_qr import \
    ConfirmationQr as ResponseConfirmationQr
from yookassa.domain.models.confirmation.response.confirmation_redirect import \
    ConfirmationRedirect as ResponseConfirmationRedirect
from yookassa.domain.models.confirmation.response.confirmation_mobile_application import \
    ConfirmationMobileApplication as ResponseConfirmationMobileApplication


class ConfirmationClassMap(DataContext):
    def __init__(self):
        super(ConfirmationClassMap, self).__init__(('request', 'response'))

    @property
    def request(self):
        return {
            ConfirmationType.REDIRECT: RequestConfirmationRedirect,
            ConfirmationType.EXTERNAL: RequestConfirmationExternal,
            ConfirmationType.EMBEDDED: RequestConfirmationEmbedded,
            ConfirmationType.QR: RequestConfirmationQr,
            ConfirmationType.MOBILE_APPLICATION: RequestConfirmationMobileApplication
        }

    @property
    def response(self):
        return {
            ConfirmationType.REDIRECT: ResponseConfirmationRedirect,
            ConfirmationType.EXTERNAL: ResponseConfirmationExternal,
            ConfirmationType.EMBEDDED: ResponseConfirmationEmbedded,
            ConfirmationType.QR: ResponseConfirmationQr,
            ConfirmationType.MOBILE_APPLICATION: ResponseConfirmationMobileApplication
        }
