# -*- coding: utf-8 -*-


class ConfirmationType:
    """
    Constants representing confirmation types. Available values are:

    * yookassa.domain.common.ConfirmationType.EXTERNAL
    * yookassa.domain.common.ConfirmationType.REDIRECT
    * yookassa.domain.common.ConfirmationType.EMBEDDED
    * yookassa.domain.common.ConfirmationType.QR
    """
    EMBEDDED = 'embedded'
    EXTERNAL = 'external'
    REDIRECT = 'redirect'
    QR = 'qr'
