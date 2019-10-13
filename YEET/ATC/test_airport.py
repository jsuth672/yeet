from django.test import TestCase
from ATC.models import *
from unittest.mock import patch, MagicMock, Mock


class TestAirportGetRunways(TestCase):

    def test_assert(self):
        # assert statements here
        airport = Airport(name="sc", x=4, y=20)

        r1 = Runway(identifier="west",size="s", airport=airport)
        r2 = Runway(identifier="east", size="m", airport=Airport(name="notsc",x=4,y=20))
        r3 = Runway(identifier="south", size="l", airport=airport)

        all_runways = [r1,r2,r3]

        def my_filter(*args, **kwargs):
            return[x for x in all_runways if x.airport == kwargs["airport"]]
        with patch.object(Runway.objects, 'filter', side_effect=my_filter) as mock_method:
            self.assertEqual(len(airport.getRunways()), 2)
            all_runways[1].airport = airport
            self.assertEqual(len(airport.getRunways()), 3)


class TestAirportGetGates(TestCase):

    def test_assert(self):
        airport = Airport(name="sc", x=4, y=20)

        g1 = Gate(identifier="west", size="s", airport=airport)
        g2 = Gate(identifier="east", size="m", airport=Airport(name="notsc", x=4, y=20))
        g3 = Gate(identifier="south", size="l", airport=airport)

        all_gates = [g1, g2, g3]

        def my_filter(*args, **kwargs):
            return [x for x in all_gates if x.airport == kwargs["airport"]]

        with patch.object(Gate.objects, 'filter', side_effect=my_filter) as mock_method:
            self.assertEqual(len(airport.getGate()), 2)
            all_gates[1].airport = airport
            self.assertEqual(len(airport.getGate()), 3)


class TestAirportGetAirlines(TestCase):

    def test_assert(self):
        airport = Airport(name="sc", x=4, y=20)

        def my_filter(*args, **kwargs):
            return [Airline(name="west"),Airline(name="east")]

        with patch.object(Airline.objects, 'filter', side_effect=my_filter) as mock_method:
            self.assertEqual(len(airport.getAirlines()), 2)
