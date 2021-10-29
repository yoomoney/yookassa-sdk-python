# -*- coding: utf-8 -*-


class ConfirmationType:
    """
    Constants representing confirmation types. Available values are:

    * yookassa.domain.common.ConfirmationType.EXTERNAL
    * yookassa.domain.common.ConfirmationType.REDIRECT
    * yookassa.domain.common.ConfirmationType.EMBEDDED
    * yookassa.domain.common.ConfirmationType.QR
    * yookassa.domain.common.ConfirmationType.MOBILE_APPLICATION
    """
    EMBEDDED = 'embedded'
    EXTERNAL = 'external'
    REDIRECT = 'redirect'
    QR = 'qr'
    MOBILE_APPLICATION = 'mobile_application'
