# -*- coding: utf-8 -*-
from yookassa.domain.common import BaseObject


class Recipient(BaseObject):
    """
    Class representing recipient data wrapper object
    """
    __account_id = None

    __gateway_id = None

    @property
    def account_id(self):
        return self.__account_id

    @account_id.setter
    def account_id(self, value):
        self.__account_id = str(value)

    @property
    def gateway_id(self):
        return self.__gateway_id

    @gateway_id.setter
    def gateway_id(self, value):
        self.__gateway_id = str(value)
