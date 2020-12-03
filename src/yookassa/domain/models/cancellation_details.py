# -*- coding: utf-8 -*-
from yookassa.domain.common import BaseObject


class CancellationDetails(BaseObject):
    """
    Class representing cancellation details data wrapper object
    """
    __party = None

    __reason = None

    @property
    def party(self):
        return self.__party

    @party.setter
    def party(self, value):
        self.__party = str(value)

    @property
    def reason(self):
        return self.__reason

    @reason.setter
    def reason(self, value):
        self.__reason = str(value)


class CancellationDetailsPartyCode(object):
    MERCHANT = 'merchant'
    YOO_KASSA = 'yoo_kassa'
    PAYMENT_NETWORK = 'payment_network'


class CancellationDetailsReasonCode(object):
    THREE_D_SECURE_FAILED = '3d_secure_failed'
    CALL_ISSUER = 'call_issuer'
    CARD_EXPIRED = 'card_expired'
    COUNTRY_FORBIDDEN = 'country_forbidden'
    FRAUD_SUSPECTED = 'fraud_suspected'
    GENERAL_DECLINE = 'general_decline'
    IDENTIFICATION_REQUIRED = 'identification_required'
    INSUFFICIENT_FUNDS = 'insufficient_funds'
    INVALID_CARD_NUMBER = 'invalid_card_number'
    INVALID_CSC = 'invalid_csc'
    ISSUER_UNAVAILABLE = 'issuer_unavailable'
    PAYMENT_METHOD_LIMIT_EXCEEDED = 'payment_method_limit_exceeded'
    PAYMENT_METHOD_RESTRICTED = 'payment_method_restricted'
    PERMISSION_REVOKED = 'permission_revoked'
    INTERNAL_TIMEOUT = 'internal_timeout'
    CANCELED_BY_MERCHANT = 'canceled_by_merchant'
    PAYMENT_EXPIRED = 'payment_expired'
    EXPIRED_ON_CONFIRMATION = 'expired_on_confirmation'
    EXPIRED_ON_CAPTURE = 'expired_on_capture'
