from django.test import Client, TestCase
from ATC.models import Runway, Airport


class TestRunway(TestCase):

    def test_runwaycreate(self):
        c = Client()  # instantiate the Django test client

        response = c.get('/ATC/new')
        self.assertEqual(response.status_code, 200)
        air = Airport(name='sc', x=0, y=0)
        response = c.post('/ATC/runway/new', {'identifier': 'runway1', 'size': 's', 'airport': str(air.id)})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/runway/new', {'identifier': 'runway1', 'size': 's', 'airport': str(air.id)})
        self.assertGreater(response.status_code, 399)

        Runway.objects.filter(identifier="runway1").delete()
        Airport.objects.filter(identifier="sc").delete()

    def test_runwayDelete(self):
        c = Client()
        air = Airport(name='sc', x=0, y=0)
        response = c.post('/ATC/runway/new', {'identifier': 'runway1', 'size': 's', 'airport': str(air.id)})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/runway/delete', {'identifier': 'runway1', 'id': str(air.id)})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/runway/new', {'identifier': 'sc', 'x': '100', 'y': '100'})
        self.assertGreater(response.status_code, 302)

        Runway.objects.filter(identifier="RunwayAgent").delete()
        Airport.objects.filter(identifier="sc").delete()

    def testbreakdown(self):
        global office, user
        office.delete()
        user.delete()
