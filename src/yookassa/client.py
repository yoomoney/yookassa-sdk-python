# -*- coding: utf-8 -*-
import typing
import httpx
import time
from requests.auth import _basic_auth_str

from yookassa import Configuration
from yookassa.domain.common import RequestObject, UserAgent
from yookassa.domain.exceptions import ApiError, BadRequestError, ForbiddenError, NotFoundError, \
    ResponseProcessingError, TooManyRequestsError, UnauthorizedError


class RetryTransport(httpx.HTTPTransport):
    """ Адаптация urllib3.Retry для HTTPX """

    def __init__(self, *args, total: int = 3, backoff_factor: float = 1, method_whitelist: typing.Optional[list] = None, status_forcelist: typing.Optional[list] = None, **kwargs):
        super(RetryTransport, self).__init__(*args, **kwargs)
        self.total = total
        self.backoff_factor = backoff_factor
        self.method_whitelist = method_whitelist
        self.status_forcelist = status_forcelist

    def handle_request(
            self,
            request: httpx.Request,
    ) -> httpx.Response:
        retry = 0
        resp = None
        retry_active = not self.method_whitelist or request.method in self.method_whitelist
        while retry < self.total:
            retry += 1
            if retry > 2:
                time.sleep(self.backoff_factor)
            try:
                if resp is not None:
                    resp.close()
                resp = super().handle_request(request)
            except Exception:
                if not retry_active:
                    raise
                continue
            if self.status_forcelist and resp.status_code in self.status_forcelist:
                continue
            break
        return resp


class ApiClient:
    endpoint = Configuration.api_endpoint()

    def __init__(self):
        self.configuration = Configuration.instantiate()
        self.shop_id = self.configuration.account_id
        self.shop_password = self.configuration.secret_key
        self.auth_token = self.configuration.auth_token
        self.timeout = self.configuration.timeout
        self.max_attempts = self.configuration.max_attempts

        self.user_agent = UserAgent()
        if self.configuration.agent_framework:
            self.user_agent.framework = self.configuration.agent_framework
        if self.configuration.agent_cms:
            self.user_agent.cms = self.configuration.agent_cms
        if self.configuration.agent_module:
            self.user_agent.module = self.configuration.agent_module

    async def request(self, method="", path="", query_params=None, headers=None, body=None):
        if isinstance(body, RequestObject):
            body.validate()
            body = dict(body)

        request_headers = self.prepare_request_headers(headers)
        raw_response = await self.execute(body, method, path, query_params, request_headers)

        if raw_response.status_code != 200:
            self.__handle_error(raw_response)

        return raw_response.json()

    async def execute(self, body, method, path, query_params, request_headers):
        session = self.get_session()
        raw_response = session.request(method,
                                       f'{self.endpoint}{path}',
                                       params=query_params,
                                       headers=request_headers,
                                       json=body,
                                       timeout=None)
        return raw_response

    def get_session(self) -> httpx.Client:
        session = httpx.Client(
            timeout=httpx.Timeout(self.timeout / 1000, connect=self.timeout / 1000),
            transport=RetryTransport()
        )
        return session

    def prepare_request_headers(self, headers):
        request_headers = {'Content-type': 'application/json'}
        if self.auth_token is not None:
            auth_headers = {"Authorization": "Bearer " + self.auth_token}
        else:
            auth_headers = {"Authorization": _basic_auth_str(self.shop_id, self.shop_password)}

        request_headers.update(auth_headers)

        request_headers.update({"YM-User-Agent": self.user_agent.get_header_string()})

        if isinstance(headers, dict):
            request_headers.update(headers)
        return request_headers

    def __handle_error(self, raw_response):
        http_code = raw_response.status_code
        if http_code == BadRequestError.HTTP_CODE:
            raise BadRequestError(raw_response.json())
        elif http_code == ForbiddenError.HTTP_CODE:
            raise ForbiddenError(raw_response.json())
        elif http_code == NotFoundError.HTTP_CODE:
            raise NotFoundError(raw_response.json())
        elif http_code == TooManyRequestsError.HTTP_CODE:
            raise TooManyRequestsError(raw_response.json())
        elif http_code == UnauthorizedError.HTTP_CODE:
            raise UnauthorizedError(raw_response.json())
        elif http_code == ResponseProcessingError.HTTP_CODE:
            raise ResponseProcessingError(raw_response.json())
        else:
            raise ApiError(raw_response.text)
