# -*- coding: utf-8 -*-


class Context(object):
    """
    Base context class.
    """
    def __init__(self, contexts):
        self.__contexts = contexts

    def get_context_data(self, context):
        """
        Return context data
        :param context: mixed
        :return: mixed
        """
        if context in self.__contexts:
            return getattr(self, context)
