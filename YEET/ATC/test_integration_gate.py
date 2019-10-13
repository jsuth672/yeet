from django.test import Client, TestCase
from ATC.models import Gate, Airport


class TestGate(TestCase):

    def test_gatecreate(self):
        c = Client()  # instantiate the Django test client

        response = c.get('/ATC/new')
        self.assertEqual(response.status_code, 200)
        air = Airport(name='sc', x=0, y=0)
        response = c.post('/ATC/gate/new', {'identifier': 'gate1', 'size': 's', 'airport': air.id})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/gate/new', {'identifier': 'gate1', 'size': 's', 'airport': air.id})
        self.assertGreater(response.status_code, 399)

        Gate.objects.filter(identifier="gate1").delete()
        Airport.objects.filter(identifier="sc").delete()

    def test_gateDelete(self):
        c = Client()
        air = Airport(name='sc', x=0, y=0)
        response = c.post('/ATC/gate/new', {'identifier': 'gate1', 'size': 's', 'airport': air.id})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/gate/delete', {'identifier': 'gate1', 'id': air.id})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/gate/new', {'identifier': 'sc', 'x': '100', 'y': '100'})
        self.assertGreater(response.status_code, 302)

        Gate.objects.filter(identifier="GateAgent").delete()
        Airport.objects.filter(identifier="sc").delete()

