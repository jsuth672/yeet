from django.test import Client, TestCase
from ATC.models import Role,User

# Noah Mansfield
class TestRole(TestCase):

    global office, user
    office = Role.objects.create(name="ATC", isATC=True)
    user = User.objects.create(name="admin", password="hello_dark", role=office)

    def test_rolecreate(self):
        c = Client()  # instantiate the Django test client
        global user
        response = c.get('/ATC/new')
        self.assertEqual(response.status_code, 200)

        response = c.post('/ATC/role/new', {'name': 'GateAgent', 'isGate': 'True', 'user':str(user.id)})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/role/new', {'name': 'GateAgent', 'isGate': 'True', 'user':str(user.id)})
        self.assertGreater(response.status_code, 399)
        Role.objects.filter(name="GateAgent").delete()

    def test_roleDelete(self):
        c = Client()
        global user
        response = c.post('/ATC/role/new', {'name': 'GateAgent', 'isGate': 'True', 'user':str(user.id)})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/role/delete', {'name': 'GateAgent', 'user':str(user.id)})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/role/new', {'name': 'sc', 'x': '100', 'y': '100', 'user':str(user.id)})
        self.assertGreater(response.status_code, 302)

        Role.objects.filter(name="GateAgent").delete()



    def testbreakdown(self):
        global office, user
        office.delete()
        user.delete()