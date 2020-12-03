# -*- coding: utf-8 -*-
from yookassa.domain.common.context import Context


class TypeFactory(object):
    """
    Base factory class for object that has type property.
    """
    def __init__(self, context):
        if isinstance(context, Context):
            self.__context = context
        else:
            TypeError('Parameter context should be Context instance')

    def create(self, data, context):
        """
        Create instance from value and context

        :param data: dictionary that has type key
        :param context: data context
        :return: Typed object instance
        """
        if isinstance(data, dict) and 'type' in data:
            return self.__get_instance(data, context)

    def __get_instance(self, data, context):
        class_object = self.__get_class_object(data, context)
        return class_object(data)

    def __get_class_object(self, data, context):
        class_object = self.__class_map(context).get(data['type'])
        return class_object

    def __class_map(self, context):
        return self.__context.get_context_data(context)
