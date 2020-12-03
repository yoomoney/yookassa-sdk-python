# -*- coding: utf-8 -*-
from yookassa.domain.exceptions.api_error import ApiError


class TooManyRequestsError(ApiError):
    HTTP_CODE = 429
