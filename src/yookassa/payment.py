# -*- coding: utf-8 -*-
import uuid

from yookassa.client import ApiClient
from yookassa.domain.common import HttpVerb
from yookassa.domain.request import CapturePaymentRequest, PaymentRequest
from yookassa.domain.response import PaymentListResponse, PaymentResponse


class Payment:
    base_path = '/payments'

    def __init__(self):
        self.client = ApiClient()

    @classmethod
    def find_one(cls, payment_id):
        """
        Get information about payment

        :param payment_id:
        :return: PaymentResponse
        """
        instance = cls()
        if not isinstance(payment_id, str) or not payment_id:
            raise ValueError('Invalid payment_id value')

        path = instance.base_path + '/' + payment_id
        response = instance.client.request(HttpVerb.GET, path)
        return PaymentResponse(response)

    @classmethod
    def create(cls, params, idempotency_key=None):
        """
        Create payment

        :param params: data passed to API
        :param idempotency_key:
        :return: PaymentResponse
        """
        instance = cls()
        path = cls.base_path

        if not idempotency_key:
            idempotency_key = uuid.uuid4()

        headers = {
            'Idempotence-Key': str(idempotency_key)
        }

        if isinstance(params, dict):
            params_object = PaymentRequest(params)
        elif isinstance(params, PaymentRequest):
            params_object = params
        else:
            raise TypeError('Invalid params value type')

        response = instance.client.request(HttpVerb.POST, path, None, headers, params_object)
        return PaymentResponse(response)

    @classmethod
    def capture(cls, payment_id, params=None, idempotency_key=None):
        """
        Capture payment

        :param payment_id:
        :param params: data passed to capture payment
        :param idempotency_key:
        :return: PaymentResponse
        """
        instance = cls()
        if not isinstance(payment_id, str) or not payment_id:
            raise ValueError('Invalid payment_id value')

        path = instance.base_path + '/' + payment_id + '/capture'

        if not idempotency_key:
            idempotency_key = uuid.uuid4()

        headers = {
            'Idempotence-Key': str(idempotency_key)
        }

        if isinstance(params, dict):
            params_object = CapturePaymentRequest(params)
        elif isinstance(params, CapturePaymentRequest):
            params_object = params
        else:
            params_object = None

        response = instance.client.request(HttpVerb.POST, path, None, headers, params_object)
        return PaymentResponse(response)

    @classmethod
    def cancel(cls, payment_id, idempotency_key=None):
        """
        Cancel payment

        :param payment_id:
        :param idempotency_key:
        :return: PaymentResponse
        """
        instance = cls()
        if not isinstance(payment_id, str) or not payment_id:
            raise ValueError('Invalid payment_id value')

        if not idempotency_key:
            idempotency_key = uuid.uuid4()

        path = instance.base_path + '/' + payment_id + '/cancel'
        headers = {
            'Idempotence-Key': str(idempotency_key)
        }
        response = instance.client.request(HttpVerb.POST, path, None, headers)
        return PaymentResponse(response)

    @classmethod
    def list(cls, params):
        instance = cls()
        path = cls.base_path

        response = instance.client.request(HttpVerb.GET, path, params)
        return PaymentListResponse(response)
