# -*- coding: utf-8 -*-
import unittest

from yookassa.configuration import Configuration, ConfigurationError


class TestConfiguration(unittest.TestCase):
    def test_configuration(self):
        Configuration.configure(account_id='test_account', secret_key='test_key', timeout=1000, max_attempts=2)
        configuration = Configuration.instantiate()

        self.assertEqual(configuration.account_id, 'test_account')
        self.assertEqual(configuration.secret_key, 'test_key')
        self.assertEqual(configuration.timeout, 1000)
        self.assertEqual(configuration.max_attempts, 2)

    def test_empty_credentials(self):
        with self.assertRaises(ConfigurationError):
            Configuration.configure(account_id=None, secret_key=None)
            configuration = Configuration.instantiate()
