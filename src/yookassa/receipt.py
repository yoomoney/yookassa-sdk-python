# -*- coding: utf-8 -*-
import uuid

from yookassa.client import ApiClient
from yookassa.domain.common.http_verb import HttpVerb
from yookassa.domain.request.receipt_request import ReceiptRequest
from yookassa.domain.response.receipt_list_response import ReceiptListResponse
from yookassa.domain.response.receipt_response import ReceiptResponse


class Receipt:
    base_path = '/receipts'

    def __init__(self):
        self.client = ApiClient()

    @classmethod
    def find_one(cls, receipt_id):
        """
        Get receipt information

        :param receipt_id:
        :return: ReceiptResponse
        """
        instance = cls()
        if not isinstance(receipt_id, str) or not receipt_id:
            raise ValueError('Invalid payment_id value')

        path = instance.base_path + '/' + receipt_id
        response = instance.client.request(HttpVerb.GET, path)
        return ReceiptResponse(response)

    @classmethod
    def create(cls, params, idempotency_key=None):
        """
        Create receipt

        :param params: data passed to API
        :param idempotency_key:
        :return: ReceiptResponse
        """
        instance = cls()
        path = cls.base_path

        if not idempotency_key:
            idempotency_key = uuid.uuid4()

        headers = {
            'Idempotence-Key': str(idempotency_key)
        }

        if isinstance(params, dict):
            params_object = ReceiptRequest(params)
        elif isinstance(params, ReceiptRequest):
            params_object = params
        else:
            raise TypeError('Invalid params value type')

        response = instance.client.request(HttpVerb.POST, path, None, headers, params_object)
        return ReceiptResponse(response)

    @classmethod
    def list(cls, params):
        instance = cls()
        path = cls.base_path

        response = instance.client.request(HttpVerb.GET, path, params)
        return ReceiptListResponse(response)
