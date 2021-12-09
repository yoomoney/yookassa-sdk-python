# -*- coding: utf-8 -*-
from yookassa.domain.common import BaseObject


class AuthorizationDetails(BaseObject):
    """
       Class representing authorization details data wrapper object
       """
    __rrn = None

    __auth_code = None

    __three_d_secure = None

    @property
    def rrn(self):
        return self.__rrn

    @rrn.setter
    def rrn(self, value):
        self.__rrn = str(value)

    @property
    def auth_code(self):
        return self.__auth_code

    @auth_code.setter
    def auth_code(self, value):
        self.__auth_code = str(value)

    @property
    def three_d_secure(self):
        return self.__three_d_secure

    @three_d_secure.setter
    def three_d_secure(self, value):
        if isinstance(value, dict):
            self.__three_d_secure = ThreeDSecure(value)
        elif isinstance(value, ThreeDSecure):
            self.__three_d_secure = value
        else:
            raise TypeError('Invalid three_d_secure value type')


class ThreeDSecure(BaseObject):
    """
    Class representing 3‑D Secure user authentication details data wrapper object
    """
    __applied = None

    @property
    def applied(self):
        return self.__applied

    @applied.setter
    def applied(self, value):
        self.__applied = bool(value)
