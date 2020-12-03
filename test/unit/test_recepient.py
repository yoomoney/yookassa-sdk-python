# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models.recipient import Recipient


class TestRecipient(unittest.TestCase):
    def test_recipient_cast(self):
        recipient = Recipient()
        recipient.account_id = '213'
        recipient.gateway_id = '123'

        self.assertEqual({
            'account_id': '213',
            'gateway_id': '123'
        }, dict(recipient))
