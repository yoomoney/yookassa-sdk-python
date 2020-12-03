# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models import Amount
from yookassa.domain.models import Currency


class TestAmount(unittest.TestCase):

    def test_amount_cast(self):
        amount = Amount()
        amount.value = 0.1
        amount.currency = Currency.RUB

        self.assertEqual({'value': 0.1, 'currency': Currency.RUB}, dict(amount))
        self.assertEqual(0.1, amount.value)

    def test_amount_value(self):
        amount = Amount({
            "value": '100.01',
            "currency": Currency.RUB
        })

        self.assertEqual({"value": 100.01, "currency": Currency.RUB}, dict(amount))
        self.assertEqual(amount.value, 100.01)
