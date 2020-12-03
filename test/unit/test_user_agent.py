# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common import UserAgent


class TestUserAgent(unittest.TestCase):
    def test_create_version(self):
        agent = UserAgent()

        agent.set_framework('Django', '1.2.3').set_module('Payment Gateway', '0.1.2')

        self.assertEqual(str(agent.framework), 'Django/1.2.3')
        self.assertEqual(str(agent.module), 'Payment.Gateway/0.1.2')

        self.assertIsNone(agent.cms)

        agent.set_cms('Word/Press', '1 2 3')
        self.assertEqual(str(agent.cms), 'Word.Press/1.2.3')
