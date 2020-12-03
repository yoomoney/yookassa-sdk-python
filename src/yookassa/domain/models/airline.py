# -*- coding: utf-8 -*-
import datetime
import re

from yookassa.domain.common import BaseObject


class Airline(BaseObject):
    """
    Class representing airline addendum data
    """
    __booking_reference = None

    __ticket_number = None

    __passengers = None

    __legs = None

    @property
    def booking_reference(self):
        return self.__booking_reference

    @booking_reference.setter
    def booking_reference(self, value):
        cast_value = str(value)
        if cast_value and len(cast_value) <= 20:
            self.__booking_reference = cast_value
        else:
            raise ValueError('Invalid booking_reference value')

    @property
    def ticket_number(self):
        return self.__ticket_number

    @ticket_number.setter
    def ticket_number(self, value):
        cast_value = str(value)
        if re.match('^[0-9]{1,150}$', cast_value):
            self.__ticket_number = cast_value
        else:
            raise ValueError('Invalid ticket_number value')

    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self, value):
        if isinstance(value, list):
            passengers = []
            for passengerData in value:
                if isinstance(passengerData, dict):
                    passengers.append(Passenger(passengerData))
                elif isinstance(passengerData, Passenger):
                    passengers.append(passengerData)
                else:
                    raise TypeError('Invalid passengers data type in airline.passengers')

            self.__passengers = passengers
        else:
            raise TypeError('Invalid passengers value type in airline')

    @property
    def legs(self):
        return self.__legs

    @legs.setter
    def legs(self, value):
        if isinstance(value, list):
            legs = []
            for legData in value:
                if isinstance(legData, dict):
                    legs.append(Leg(legData))
                elif isinstance(legData, Leg):
                    legs.append(legData)
                else:
                    raise TypeError('Invalid legs data type in airline.passengers')

            self.__legs = legs
        else:
            raise TypeError('Invalid legs value type in airline')


class Passenger(BaseObject):
    __first_name = None

    __last_name = None

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        cast_value = str(value)
        if cast_value and len(cast_value) <= 64:
            self.__first_name = cast_value
        else:
            raise ValueError('Invalid passengers first_name value')

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        cast_value = str(value)
        if cast_value and len(cast_value) <= 64:
            self.__last_name = cast_value
        else:
            raise ValueError('Invalid passengers last_name value')


class Leg(BaseObject):
    __departure_airport = None

    __destination_airport = None

    __departure_date = None

    @property
    def departure_airport(self):
        return self.__departure_airport

    @departure_airport.setter
    def departure_airport(self, value):
        if re.match('^[A-Z]{3}$', value):
            self.__departure_airport = value
        else:
            raise ValueError('Invalid departure_airport value')

    @property
    def destination_airport(self):
        return self.__destination_airport

    @destination_airport.setter
    def destination_airport(self, value):
        if re.match('^[A-Z]{3}$', value):
            self.__destination_airport = value
        else:
            raise ValueError('Invalid destination_airport value')

    @property
    def departure_date(self):
        return self.__departure_date

    @departure_date.setter
    def departure_date(self, value):
        try:
            datetime.datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

        self.__departure_date = value
