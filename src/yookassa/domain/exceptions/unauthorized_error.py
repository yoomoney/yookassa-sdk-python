# -*- coding: utf-8 -*-
from yookassa.domain.exceptions.api_error import ApiError


class UnauthorizedError(ApiError):
    HTTP_CODE = 401
