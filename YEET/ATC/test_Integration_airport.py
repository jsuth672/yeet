from django.test import Client, TestCase
from .models import Airport


class test_Airport(TestCase):
    def test_airportcreate(self):
        c = Client()  # instantiate the Django test client

        response = c.get('/ATC/new')
        self.assertEqual(response.status_code, 200)

        response = c.post('/ATC/airport/new', {'name': 'sc', 'x': '100', 'y': '100'})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/airport/new', {'name': 'sc', 'x': '100', 'y': '100'})
        self.assertGreater(response.status_code, 399)
        Airport.objects.filter(name="sc").delete()
    def test_airportDelete(self):
        c = Client()
        response = c.post('/ATC/airport/new', {'name': 'sc', 'x': '100', 'y': '100'})
        self.assertEqual(response.status_code, 302)

        Air = Airport.objects.get(name='sc')

        repsonse = c.post('/ATC/ariport/delete', {'id': Air.id})

        response = c.post('/ATC/airport/new', {'name': 'sc', 'x': '100', 'y': '100'})
        self.assertGreater(response.status_code, 302)

        Airport.objects.filter(name="sc").delete()


