# -*- coding: utf-8 -*-
import uuid

from yookassa.client import ApiClient
from yookassa.domain.common.http_verb import HttpVerb
from yookassa.domain.request import PayoutRequest
from yookassa.domain.response import PayoutResponse


class Payout:
    base_path = '/payouts'

    def __init__(self):
        self.client = ApiClient()

    @classmethod
    def find_one(cls, payout_id):
        """
        Get receipt information

        :param payout_id:
        :return: PayoutResponse
        """
        instance = cls()
        if not isinstance(payout_id, str) or not payout_id:
            raise ValueError('Invalid payment_id value')

        path = instance.base_path + '/' + payout_id
        response = instance.client.request(HttpVerb.GET, path)
        return PayoutResponse(response)

    @classmethod
    def create(cls, params, idempotency_key=None):
        """
        Create receipt

        :param params: data passed to API
        :param idempotency_key:
        :return: PayoutResponse
        """
        instance = cls()
        path = cls.base_path

        if not idempotency_key:
            idempotency_key = uuid.uuid4()

        headers = {
            'Idempotence-Key': str(idempotency_key)
        }

        if isinstance(params, dict):
            params_object = PayoutRequest(params)
        elif isinstance(params, PayoutRequest):
            params_object = params
        else:
            raise TypeError('Invalid params value type')

        response = instance.client.request(HttpVerb.POST, path, None, headers, params_object)
        return PayoutResponse(response)
