from django.test import Client, TestCase
from ATC.models import Gate, Airport, Role, User

# Noah Mansfield
class TestGate(TestCase):

    global office, user
    office = Role.objects.create(name="ATC", isATC=True)
    user = User.objects.create(name="admin", password="hello_dark", role=office)

    def test_gatecreate(self):
        global user
        c = Client()  # instantiate the Django test client
        response = c.get('/ATC/new')
        self.assertEqual(response.status_code, 200)
        air = Airport(name='sc', x=0, y=0)
        response = c.post('/ATC/gate/new', {'identifier': 'gate1', 'size': 's', 'airport': str(air.id), 'user':str(user.id)})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/gate/new', {'identifier': 'gate1', 'size': 's', 'airport': str(air.id), 'user':str(user.id)})
        self.assertGreater(response.status_code, 399)

        Gate.objects.filter(identifier="gate1").delete()
        Airport.objects.filter(identifier="sc").delete()

    def test_gateDelete(self):
        c = Client()
        global user
        air = Airport(name='sc', x=0, y=0)
        response = c.post('/ATC/gate/new', {'identifier': 'gate1', 'size': 's', 'airport': str(air.id), 'user':str(user.id)})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/gate/delete', {'identifier': 'gate1', 'id': str(air.id), 'user':str(user.id)})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/gate/new', {'identifier': 'sc', 'x': '100', 'y': '100', 'user':str(user.id)})
        self.assertGreater(response.status_code, 302)

        Gate.objects.filter(identifier="GateAgent").delete()
        Airport.objects.filter(identifier="sc").delete()


    def testbreakdown(self):
        global office, user
        office.delete()
        user.delete()
