# -*- coding: utf-8 -*-
from yookassa.domain.exceptions.api_error import ApiError


class NotFoundError(ApiError):
    HTTP_CODE = 404
