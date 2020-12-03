# -*- coding: utf-8 -*-
from yookassa.domain.common.type_factory import TypeFactory
from yookassa.domain.models.confirmation.confirmation_class_map import ConfirmationClassMap


class ConfirmationFactory(TypeFactory):
    def __init__(self):
        super(ConfirmationFactory, self).__init__(ConfirmationClassMap())
