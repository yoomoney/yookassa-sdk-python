# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models import Airline, Passenger, Leg


class TestAirline(unittest.TestCase):
    def test_setters_inline_data(self):
        airline = Airline()
        airline.booking_reference = '123123'
        airline.ticket_number = '5551238432721'
        airline.passengers = [
            {
                'first_name': 'Joe',
                'last_name': 'Doe'
            }
        ]
        airline.legs = [
            {
                'departure_airport': 'IVA',
                'destination_airport': 'NYC',
                'departure_date': '2017-01-02'
            }
        ]

        self.assertEqual({
            'booking_reference': '123123',
            'ticket_number': '5551238432721',
            'passengers': [
                {
                    'first_name': 'Joe',
                    'last_name': 'Doe'
                }
            ],
            'legs': [
                {
                    'departure_airport': 'IVA',
                    'destination_airport': 'NYC',
                    'departure_date': '2017-01-02'
                }
            ]
        }, dict(airline))

    def test_setters_objects_data(self):
        airline = Airline()
        airline.booking_reference = '123123'
        airline.ticket_number = '5551238432721'
        joe = Passenger()
        joe.first_name = 'Joe'
        joe.last_name = 'Doe'

        airline.passengers = [
            joe
        ]

        leg = Leg()
        leg.departure_airport = 'IVA'
        leg.destination_airport = 'NYC'
        leg.departure_date = '2017-01-02'

        airline.legs = [
            leg
        ]

        self.assertEqual({
            'booking_reference': '123123',
            'ticket_number': '5551238432721',
            'passengers': [
                {
                    'first_name': 'Joe',
                    'last_name': 'Doe'
                }
            ],
            'legs': [
                {
                    'departure_airport': 'IVA',
                    'destination_airport': 'NYC',
                    'departure_date': '2017-01-02'
                }
            ]
        }, dict(airline))
