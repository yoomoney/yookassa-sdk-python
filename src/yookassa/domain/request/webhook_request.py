# -*- coding: utf-8 -*-
from yookassa.domain.common.request_object import RequestObject


class WebhookRequest(RequestObject):
    __event = None

    __url = None

    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, value):
        cast_value = str(value)
        self.__event = cast_value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        cast_value = str(value)
        self.__url = cast_value
