from django.test import Client, TestCase
from ATC.models import Airport, Role, User

# Noah Mansfield
class TestAirport(TestCase):

    global office, user
    office = Role.objects.create(name="ATC", isATC=True)
    user = User.objects.create(name="admin", password="hello_dark", role=office)

    def test_airportcreate(self):
        c = Client()  # instantiate the Django test client
        global user
        response = c.get('/ATC/new')
        self.assertEqual(response.status_code, 200)

        response = c.post('/ATC/airport/new', {'name': 'sc', 'x': '100', 'y': '100', 'user':str(user.id)})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/airport/new', {'name': 'sc', 'x': '100', 'y': '100', 'user':str(user.id)})
        self.assertGreater(response.status_code, 399)
        Airport.objects.filter(name="sc").delete()
    def test_airportDelete(self):
        c = Client()
        global user
        response = c.post('/ATC/airport/new', {'name': 'sc', 'x': '100', 'y': '100', 'user':str(user.id)})
        self.assertEqual(response.status_code, 302)

        air = Airport.objects.get(name='sc')

        response = c.post('/ATC/airport/delete', {'id': str(air.id), 'user':str(user.id)})
        self.assertEqual(response.status_code, 302)
        response = c.post('/ATC/airport/new', {'name': 'sc', 'x': '100', 'y': '100', 'user':str(user.id)})
        self.assertGreater(response.status_code, 302)

        Airport.objects.filter(name="sc").delete()

    def testbreakdown(self):
        global office, user
        office.delete()
        user.delete()

