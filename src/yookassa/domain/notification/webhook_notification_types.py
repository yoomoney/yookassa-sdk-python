# -*- coding: utf-8 -*-


class WebhookNotificationType:
    """
    """
    NOTIFICATION = 'notification'


class WebhookNotificationEventType:
    """
    """
    PAYMENT_WAITING_FOR_CAPTURE = 'payment.waiting_for_capture'
    PAYMENT_SUCCEEDED = 'payment.succeeded'
    PAYMENT_CANCELED = 'payment.canceled'
    REFUND_SUCCEEDED = 'refund.succeeded'
