# -*- coding: utf-8 -*-
from yookassa.domain.exceptions.api_error import ApiError


class ForbiddenError(ApiError):
    HTTP_CODE = 403

