# -*- coding: utf-8 -*-
from yookassa.domain.common.context import Context


class DataContext(Context):
    """
    Constants representing context data types. Available values are:

    * yookassa.domain.common.DataContext.REQUEST
    * yookassa.domain.common.DataContext.RESPONSE
    """
    REQUEST = 'request'
    RESPONSE = 'response'
