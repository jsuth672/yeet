from django.test import Client, TestCase
from ATC.models import Role


class TestRole(TestCase):

    def test_rolecreate(self):
        c = Client()  # instantiate the Django test client

        response = c.get('/ATC/new')
        self.assertEqual(response.status_code, 200)

        response = c.post('/ATC/role/new', {'name': 'GateAgent', 'isGate': 'True'})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/role/new', {'name': 'GateAgent', 'isGate': 'True'})
        self.assertGreater(response.status_code, 399)
        Role.objects.filter(name="GateAgent").delete()

    def test_roleDelete(self):
        c = Client()
        response = c.post('/ATC/role/new', {'name': 'GateAgent', 'isGate': 'True'})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/role/delete', {'name': 'GateAgent'})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/role/new', {'name': 'sc', 'x': '100', 'y': '100'})
        self.assertGreater(response.status_code, 302)

        Role.objects.filter(name="GateAgent").delete()


