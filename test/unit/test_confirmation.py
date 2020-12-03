# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common.confirmation_type import ConfirmationType
from yookassa.domain.models.confirmation.request.confirmation_redirect import \
    ConfirmationRedirect as RequestConfirmationRedirect
from yookassa.domain.models.confirmation.response.confirmation_qr import \
    ConfirmationQr as ResponseConfirmationQr
from yookassa.domain.models.confirmation.response.confirmation_redirect import \
    ConfirmationRedirect as ResponseConfirmationRedirect


class TestConfirmation(unittest.TestCase):
    def test_confirmation_request(self):
        confirmation = RequestConfirmationRedirect()
        confirmation.type = ConfirmationType.REDIRECT
        confirmation.locale = 'ru_RU'
        confirmation.enforce = True
        confirmation.return_url = 'return.url'

        self.assertEqual(confirmation.type, ConfirmationType.REDIRECT)
        self.assertTrue(confirmation.enforce)
        self.assertEqual(
            {'type': ConfirmationType.REDIRECT, 'locale': 'ru_RU', 'enforce': True, 'return_url': 'return.url'},
            dict(confirmation)
        )

        with self.assertRaises(ValueError):
            confirmation.return_url = ''

    def test_confirmation_response(self):
        confirmation = ResponseConfirmationRedirect()
        confirmation.type = ConfirmationType.REDIRECT
        confirmation.enforce = True
        confirmation.return_url = 'return.url'
        confirmation.confirmation_url = 'confirmation.url'
        self.assertEqual(confirmation.type, ConfirmationType.REDIRECT)
        self.assertTrue(confirmation.enforce)
        self.assertEqual(
            {
                'type': ConfirmationType.REDIRECT,
                'enforce': True,
                'return_url': 'return.url',
                'confirmation_url': 'confirmation.url'
            },
            dict(confirmation)
        )

        with self.assertRaises(ValueError):
            confirmation.return_url = ''

    def test_confirmation_response_qr(self):
        confirmation = ResponseConfirmationQr()
        confirmation.type = ConfirmationType.QR
        confirmation.confirmation_data = 'confirmation.url'
        self.assertEqual(confirmation.type, ConfirmationType.QR)
        self.assertEqual(
            {
                'type': ConfirmationType.QR,
                'confirmation_data': 'confirmation.url'
            },
            dict(confirmation)
        )

        with self.assertRaises(ValueError):
            confirmation.confirmation_data = ''
