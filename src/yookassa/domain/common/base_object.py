# -*- coding: utf-8 -*-
import json
from decimal import Decimal


class BaseObject(object):
    """
    Base class for data objects.
    A class provides cast to dictionary functionality and set up attributes from dictionary.
    """

    def __init__(self, *args, **kwargs):
        for dictionary in args:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __iter__(self):
        property_names = [prop for prop in dir(self.__class__) if isinstance(getattr(self.__class__, prop), property)]
        properties = dict((value, getattr(self, value)) for value in property_names if getattr(self, value) is not None)
        for prop_name, prop_value in properties.items():
            if isinstance(prop_value, BaseObject):
                yield prop_name, dict(prop_value)
            elif isinstance(prop_value, list):
                list_value = []
                for value in prop_value:
                    if isinstance(value, BaseObject):
                        list_value.append(dict(value))
                    else:
                        list_value.append(value)
                yield prop_name, list_value
            elif isinstance(prop_value, Decimal):
                yield prop_name, float(prop_value)
            else:
                yield prop_name, prop_value

    def json(self):
        return json.dumps(dict(self), default=str, ensure_ascii=False)
