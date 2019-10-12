from unittest.mock import patch, MagicMock, Mock
from django.test import TestCase
from ATC.models import Airline, Plane


class TestAirlineGetPlanes(TestCase):

    def test_assert(self):
        def filter_mock_1(**kwargs):
            return [Plane(identifier="plane1")]

        def filter_mock_2(**kwargs):
            return [Plane(identifier="plane1"), Plane(identifier="plane2")]

        airline = Airline(name="BJUAir")
        with patch.object(Plane.objects, 'filter', side_effect=filter_mock_1) as mock_method:
            self.assertEqual(len(airline.getPlanes()), 1)
        with patch.object(Plane.objects, 'filter', side_effect=filter_mock_2) as mock_method:
            self.assertEqual(len(airline.getPlanes()), 2)
