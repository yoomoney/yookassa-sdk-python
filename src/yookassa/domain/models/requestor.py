# -*- coding: utf-8 -*-
from yookassa.domain.common import BaseObject


class RequestorType:
    MERCHANT = "merchant"
    THIRD_PARTY_CLIENT = "third_party_client"


class Requestor(BaseObject):
    """
    Class representing requestor data wrapper object
    """
    __type = None

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = str(value)


class RequestorMerchant(Requestor):
    """
    Class representing requestor_merchant data wrapper object
    """
    __type = RequestorType.MERCHANT

    __account_id = None

    @property
    def account_id(self):
        return self.__account_id

    @account_id.setter
    def account_id(self, value):
        self.__account_id = str(value)


class RequestorThirdPartyClient(Requestor):
    """
    Class representing requestor_third_party_client data wrapper object
    """
    __type = RequestorType.THIRD_PARTY_CLIENT

    __client_id = None

    __client_name = None

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        self.__client_id = str(value)

    @property
    def client_name(self):
        return self.__client_name

    @client_name.setter
    def client_name(self, value):
        self.__client_name = str(value)


class RequestorFactory(object):
    """
    Base factory class for object that has type property.
    """

    def create(self, data):
        """
        Create instance from value

        :param data: dictionary that has type key
        :return: Typed object instance
        """
        if isinstance(data, dict):
            if 'type' in data:
                return self.__get_instance(data)
            else:
                raise ValueError('Parameter "data" should contain "type" field')
        else:
            raise TypeError('Parameter "data" should be "dict"')

    def __get_instance(self, data):
        class_object = self.__get_class_object(data)
        return class_object(data)

    @staticmethod
    def __get_class_object(data):
        if data['type'] == RequestorType.MERCHANT:
            return RequestorMerchant
        elif data['type'] == RequestorType.THIRD_PARTY_CLIENT:
            return RequestorThirdPartyClient
        else:
            raise TypeError('Parameter "data" should contain "type" field')
