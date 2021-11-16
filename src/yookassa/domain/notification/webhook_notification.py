# -*- coding: utf-8 -*-
from yookassa.domain.common import BaseObject
from yookassa.domain.notification.webhook_notification_types import WebhookNotificationType, \
    WebhookNotificationEventType
from yookassa.domain.response import DealResponse
from yookassa.domain.response.payment_response import PaymentResponse
from yookassa.domain.response.payout_response import PayoutResponse
from yookassa.domain.response.refund_response import RefundResponse


class WebhookNotification(BaseObject):

    __type = None

    __event = None

    __object = None

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, value):
        self.__event = value

    @property
    def object(self):
        return self.__object

    @object.setter
    def object(self, value):
        if isinstance(value, dict) and value:
            self.__object = PaymentResponse(value)
        elif not value:
            raise ValueError('Parameter object is empty')
        else:
            raise TypeError('Invalid object type')


class PaymentWebhookNotification(WebhookNotification):
    pass


class RefundWebhookNotification(WebhookNotification):

    @property
    def object(self):
        return self.__object

    @object.setter
    def object(self, value):
        if isinstance(value, dict) and value:
            self.__object = RefundResponse(value)
        elif not value:
            raise ValueError('Parameter object is empty')
        else:
            raise TypeError('Invalid object type')


class DealWebhookNotification(WebhookNotification):

    @property
    def object(self):
        return self.__object

    @object.setter
    def object(self, value):
        if isinstance(value, dict) and value:
            self.__object = DealResponse(value)
        elif not value:
            raise ValueError('Parameter object is empty')
        else:
            raise TypeError('Invalid object type')


class PayoutWebhookNotification(WebhookNotification):

    @property
    def object(self):
        return self.__object

    @object.setter
    def object(self, value):
        if isinstance(value, dict) and value:
            self.__object = PayoutResponse(value)
        elif not value:
            raise ValueError('Parameter object is empty')
        else:
            raise TypeError('Invalid object type')


class WebhookNotificationFactory(object):
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
            if 'type' in data and 'event' in data:
                return self.__get_instance(data)
            else:
                raise ValueError('Parameter "data" should contain "type" and "event" fields')
        else:
            raise TypeError('Parameter "data" should be "dict"')

    def __get_instance(self, data):
        class_object = self.__get_class_object(data)
        return class_object(data)

    @staticmethod
    def __get_class_object(data):
        if data['type'] == WebhookNotificationType.NOTIFICATION:
            if data['event'] == WebhookNotificationEventType.REFUND_SUCCEEDED:
                return RefundWebhookNotification
            elif data['event'] == WebhookNotificationEventType.DEAL_CLOSED:
                return DealWebhookNotification
            elif data['event'] == WebhookNotificationEventType.PAYOUT_SUCCEEDED or \
                    data['event'] == WebhookNotificationEventType.PAYOUT_CANCELED:
                return PayoutWebhookNotification
            else:
                return WebhookNotification
        else:
            raise TypeError('Parameter "data" should contain "type" field')
