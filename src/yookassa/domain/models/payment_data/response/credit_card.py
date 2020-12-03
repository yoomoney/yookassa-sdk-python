# -*- coding: utf-8 -*-
import re

from yookassa.domain.common import BaseObject


class CreditCard(BaseObject):
    # Первые 6 цифр номера карты (BIN).
    __first6 = None
    # Последние 4 цифры номера карты.
    __last4 = None
    # Срок действия, год, YYYY.
    __expiry_year = None
    # Срок действия, месяц, MM.
    __expiry_month = None
    # Тип банковской карты. Возможные значения:
    # ~`MasterCard` (для карт Mastercard и Maestro), ~`Visa` (для карт Visa и Visa Electron),
    # ~`Mir`, ~`UnionPay`, ~`JCB`, ~`AmericanExpress`, ~`DinersClub` и ~`Unknown`.
    __card_type = None
    # Код страны, в которой выпущена карта.
    # Передается в формате [ISO-3166 alpha-2](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en).
    # Пример: RU.
    __issuer_country = None
    # Наименование банка, выпустившего карту.
    __issuer_name = None
    # Источник данных банковской карты.
    # Возможные значения: ~`apple_pay`, ~`google_pay`.
    # Присутствует, если пользователь при оплате выбрал карту, сохраненную в Apple Pay или Google Pay.
    __source = None

    @property
    def first6(self):
        return self.__first6

    @first6.setter
    def first6(self, value):
        cast_value = str(value)
        if re.match('^[0-9]{6}$', cast_value):
            self.__first6 = cast_value
        else:
            raise ValueError('Invalid first6 value')

    @property
    def last4(self):
        return self.__last4

    @last4.setter
    def last4(self, value):
        cast_value = str(value)
        if re.match(r'^[\d]{4}$', cast_value):
            self.__last4 = cast_value
        else:
            raise ValueError('Invalid last4 value')

    @property
    def expiry_year(self):
        return self.__expiry_year

    @expiry_year.setter
    def expiry_year(self, value):
        cast_value = str(value)
        if re.match(r'^\d\d\d\d$', cast_value) and 2000 < int(cast_value) < 2200:
            self.__expiry_year = cast_value
        else:
            raise ValueError('Invalid card expiry year value')

    @property
    def expiry_month(self):
        return self.__expiry_month

    @expiry_month.setter
    def expiry_month(self, value):
        cast_value = str(value)
        if re.match(r'^\d\d$', cast_value) and 0 < int(cast_value) <= 12:
            self.__expiry_month = cast_value
        else:
            raise ValueError('Invalid card expiry month value')

    @property
    def card_type(self):
        return self.__card_type

    @card_type.setter
    def card_type(self, value):
        self.__card_type = value

    @property
    def issuer_country(self):
        return self.__issuer_country

    @issuer_country.setter
    def issuer_country(self, value):
        cast_value = str(value)
        if len(cast_value) == 2:
            self.__issuer_country = cast_value
        else:
            raise ValueError('Invalid card issuer country value')

    @property
    def issuer_name(self):
        return self.__issuer_name

    @issuer_name.setter
    def issuer_name(self, value):
        self.__issuer_name = str(value)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        self.__source = str(value)
