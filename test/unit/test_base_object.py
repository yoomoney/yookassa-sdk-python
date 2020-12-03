# -*- coding: utf-8 -*-
import json
import unittest

from yookassa.domain.common import BaseObject


class MyBaseObject(BaseObject):
    __test = None
    __int_value = None
    __float_value = None
    __base_object = None
    __values_list = None
    __base_objects_list = None

    @property
    def test(self):
        return self.__test

    @test.setter
    def test(self, value):
        self.__test = value

    @property
    def int_value(self):
        return self.__int_value

    @int_value.setter
    def int_value(self, value):
        self.__int_value = value

    @property
    def float_value(self):
        return self.__float_value

    @float_value.setter
    def float_value(self, value):
        self.__float_value = value

    @property
    def base_object(self):
        return self.__base_object

    @base_object.setter
    def base_object(self, value):
        self.__base_object = MyBaseObject(value)

    @property
    def values_list(self):
        return self.__values_list

    @values_list.setter
    def values_list(self, value):
        self.__values_list = value

    @property
    def base_objects_list(self):
        return self.__base_objects_list

    @base_objects_list.setter
    def base_objects_list(self, value):
        self.__base_objects_list = [MyBaseObject(item) for item in value]


class TestBaseObject(unittest.TestCase):
    def setUp(self):
        self.fixture_args = {
            'test': 'test',
            'int_value': 123,
            'float_value': 1.01,
            'base_object': {
                'test': 'test'
            },
            'values_list': [1, 2, 3],
            'base_objects_list': [{'test': 'test'}, {'test': 'test'}, {'test': 'test'}]
        }

    def test_cas_to_dict_args(self):
        base_object = MyBaseObject(self.fixture_args)
        self.assertIsInstance(base_object.base_object, MyBaseObject)
        for item in base_object.base_objects_list:
            self.assertIsInstance(item, MyBaseObject)
        self.assertEqual(self.fixture_args, dict(base_object))

    def test_cas_to_dict_kwargs(self):
        base_object = MyBaseObject(**self.fixture_args)
        self.assertIsInstance(base_object.base_object, MyBaseObject)
        for item in base_object.base_objects_list:
            self.assertIsInstance(item, MyBaseObject)
        self.assertEqual(self.fixture_args, dict(base_object))

    def test_json(self):
        base_object = MyBaseObject(**self.fixture_args)
        my_json = base_object.json()

        self.assertIsInstance(my_json, str)
        self.assertEqual(dict(base_object), dict(json.loads(my_json)))
