# -*- coding: utf-8 -*-
import sys
import unittest

from requests import Response

from yookassa.domain.common.user_agent import Version

if sys.version_info >= (3, 3):
    from unittest.mock import patch
else:
    from mock import patch

from yookassa.client import ApiClient
from yookassa.configuration import Configuration
from yookassa.domain.common.http_verb import HttpVerb
from yookassa.domain.common.request_object import RequestObject


class TestClient(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        Configuration.configure(account_id='test_account_id', secret_key='test_secret_key')
        Configuration.agent_framework = Version('YooMoney.Framework', '0.0.1')
        Configuration.agent_cms = Version('YooMoney.Cms', '0.0.2')
        Configuration.agent_module = Version('YooMoney.Module', '0.0.3')

    async def test_request(self):
        client = ApiClient()
        with patch('yookassa.client.ApiClient.request') as request_mock:
            request_mock.return_value = {
                'amount': {'currency': 'RUB', 'value': 1.0},
                'created_at': '2017-11-30T15:45:31.130Z',
                'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
                'metadata': {'float_value': '123.32', 'key': 'data'},
                'paid': False,
                'payment_method': {'type': 'bank_card'},
                'recipient': {'account_id': '156833', 'gateway_id': '468284'},
                'status': 'canceled'
            }

            await client.request(HttpVerb.POST, '/path', RequestObject(), {'header': 'header'})

    async def test_execute(self):
        client = ApiClient()
        with patch('yookassa.client.ApiClient.execute') as request_mock:
            res = Response()
            res.status_code = 200
            res._content = b"{}"
            request_mock.return_value = res

            await client.request(HttpVerb.POST, '/path', RequestObject({"param": "param"}), {'header': 'header'})
