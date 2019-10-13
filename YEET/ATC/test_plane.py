from django.test import TestCase
from ATC.models import Plane, Airline, Gate, Runway, Airport

# written by Justin Sutherland edited by Noah Mansfield

class TestPlaneGetAirline(TestCase):
    def test_assert(self):
        plane = Plane(identifier="Airplane 1", size ="l", currentPassengerCount = 174, maxPassengerCount = 200, airline = Airline(name = "Airline 1"))
        self.assertEqual(plane.getAirline().name, "Airline 1")

class TestPlaneGetGate(TestCase):

    def test_assert(self):
        plane = Plane(identifier="Airplane 1", size ="l", currentPassengerCount = 174, maxPassengerCount = 200, gate = Gate( identifier = "A1", size = "l", airport = Airport(name = "GSA", x = 45, y = 3) ))
        self.assertEqual(plane.getGate().identifier, "A1")


class TestPlaneGetRunway(TestCase):
    def test_assert(self):
        plane  = Plane(identifier="Airplane 1", size ="l", currentPassengerCount = 174, maxPassengerCount = 200, runway = Runway(identifier = "C1", size = "m", airport = Airport(name = "GSA", x = 45, y = 3)))
        self.assertEqual(plane.getRunway().identifier, "C1")