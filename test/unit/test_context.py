# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.common.context import Context


class MyContext(Context):
    @property
    def property1(self):
        return 'property1'

    @property
    def property2(self):
        return 'property2'


class TestContext(unittest.TestCase):
    def test_get_context_data(self):
        context = MyContext(contexts=('property1', 'property2'))
        self.assertEqual('property1', context.get_context_data('property1'))
        self.assertEqual('property2', context.get_context_data('property2'))
