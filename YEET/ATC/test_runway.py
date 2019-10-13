from django.test import TestCase
from ATC.models import Runway, Airport, Plane
# Jake Mincy with tons of help from Noah


class TestGetAirport(TestCase):
    def test_assert(self):
        airport = Airport(name="LGA")
        runway = Runway(identifier="Runway 1", size ="L", airport=airport)
        self.assertEqual(runway.getAirport().name, "LGA")


class TestGetPlane(TestCase):
    def test_assert(self):
        airport = Airport(name="LGA")
        plane = Plane(identifier="747", size=1, currentPassengerCount=15, maxPassengerCount=67)
        runway = Runway(identifier="Runway 1", size ="L", airport=airport, plane=plane)
        self.assertEqual(runway.getPlane().identifier, "747")