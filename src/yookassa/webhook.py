# -*- coding: utf-8 -*-
import uuid

from yookassa.client import ApiClient
from yookassa.domain.common.http_verb import HttpVerb
from yookassa.domain.request.webhook_request import WebhookRequest
from yookassa.domain.response.webhook_response import WebhookResponse, WebhookList


class Webhook:
    base_path = '/webhooks'

    def __init__(self):
        self.client = ApiClient()

    """
    Get list of installed webhooks
    
    :return: WebhookList
    """
    @classmethod
    def list(cls):
        instance = cls()
        path = cls.base_path

        response = instance.client.request(HttpVerb.GET, path)
        return WebhookList(response)

    """
    Add webhook

    :param params: data passed to API
    :param idempotency_key:
    :return: WebhookResponse
    """
    @classmethod
    def add(cls, params, idempotency_key=None):
        instance = cls()
        path = cls.base_path
        if not idempotency_key:
            idempotency_key = uuid.uuid4()
        headers = {
            'Idempotence-Key': str(idempotency_key)
        }

        if isinstance(params, dict):
            params_object = WebhookRequest(params)
        elif isinstance(params, WebhookRequest):
            params_object = params
        else:
            raise TypeError('Invalid params value type')

        response = instance.client.request(HttpVerb.POST, path, None, headers, params_object)
        return WebhookResponse(response)

    """
    Remove webhook

    :param webhook_id: 
    :param idempotency_key:
    :return: WebhookResponse
    """
    @classmethod
    def remove(cls, webhook_id, idempotency_key=None):
        instance = cls()
        path = cls.base_path + '/' + webhook_id
        if not idempotency_key:
            idempotency_key = uuid.uuid4()
        headers = {
            'Idempotence-Key': str(idempotency_key)
        }

        response = instance.client.request(HttpVerb.DELETE, path, None, headers)
        return WebhookResponse(response)
