from django.test import TestCase
from ATC.models import Gate, Airport, Plane


class TestGateGetPlane(TestCase):

    # written by Ryan Longacre
    def test_assert(self):
        gate = Gate(identifier="big gate", size="big", plane=Plane(identifier="small plane"))
        self.assertEqual(gate.getPlane().identifier, "small plane")


class TestGateGetAirport(TestCase):

    # written by Ryan Longacre
    def test_assert(self):
        gate = Gate(identifier="small gate", size="small", airport=Airport(name="big airport"))
        self.assertEqual(gate.getAirport().name, "big airport")
