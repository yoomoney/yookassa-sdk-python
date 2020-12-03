# -*- coding: utf-8 -*-
from yookassa.domain.common.response_object import ResponseObject


class WebhookResponse(ResponseObject):
    __id = None

    __url = None

    __event = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, value):
        self.__event = value

    @property
    def url(self):
        return self.__event

    @url.setter
    def url(self, value):
        self.__url = value


class WebhookList(ResponseObject):
    __type = None

    __items = None

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self.__items = [WebhookResponse(webhook) for webhook in value]
        else:
            self.__items = value



