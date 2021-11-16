# -*- coding: utf-8 -*-
import uuid

from yookassa.client import ApiClient
from yookassa.domain.common.http_verb import HttpVerb
from yookassa.domain.request import DealRequest
from yookassa.domain.response import DealResponse, DealListResponse


class Deal:
    base_path = '/deals'

    def __init__(self):
        self.client = ApiClient()

    @classmethod
    def find_one(cls, deal_id):
        """
        Get receipt information

        :param deal_id:
        :return: DealResponse
        """
        instance = cls()
        if not isinstance(deal_id, str) or not deal_id:
            raise ValueError('Invalid payment_id value')

        path = instance.base_path + '/' + deal_id
        response = instance.client.request(HttpVerb.GET, path)
        return DealResponse(response)

    @classmethod
    def create(cls, params, idempotency_key=None):
        """
        Create receipt

        :param params: data passed to API
        :param idempotency_key:
        :return: DealResponse
        """
        instance = cls()
        path = cls.base_path

        if not idempotency_key:
            idempotency_key = uuid.uuid4()

        headers = {
            'Idempotence-Key': str(idempotency_key)
        }

        if isinstance(params, dict):
            params_object = DealRequest(params)
        elif isinstance(params, DealRequest):
            params_object = params
        else:
            raise TypeError('Invalid params value type')

        response = instance.client.request(HttpVerb.POST, path, None, headers, params_object)
        return DealResponse(response)

    @classmethod
    def list(cls, params):
        instance = cls()
        path = cls.base_path

        response = instance.client.request(HttpVerb.GET, path, params)
        return DealListResponse(response)
