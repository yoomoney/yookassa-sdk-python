# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common import SecurityHelper


class TestSecurityHelper(unittest.TestCase):

    def test_check_ip(self):
        sh = SecurityHelper()

        self.assertTrue(sh.is_ip_trusted('77.75.153.75'))
        self.assertTrue(sh.is_ip_trusted('2a02:5180:0:2669::2a:dc6a'))

        self.assertFalse(sh.is_ip_trusted('192.168.1.1'))
        self.assertFalse(sh.is_ip_trusted('2a02:4180:0:2969::2a:006a'))
