# -*- coding: utf-8 -*-
from yookassa.domain.common import BaseObject
from yookassa.domain.common.data_context import DataContext


class ResponseObject(BaseObject):
    """
    Base class for request objects
    """
    @staticmethod
    def context():
        return DataContext.RESPONSE
