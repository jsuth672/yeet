from django.test import Client, TestCase
from ATC.models import User, Role

# Noah Mansfield
class test_User(TestCase):
    global office, user
    office = Role.objects.create(name="ATC", isATC=True)
    user = User.objects.create(name="admin", password="hello_dark", role=office)



    def test_usercreate(self):
        c = Client()  # instantiate the Django test client
        global user
        response = c.get('/ATC/new')
        self.assertEqual(response.status_code, 200)

        response = c.post('/ATC/user/new', {'name': 'Noah Mansfield', 'password': 'hello_darkness', 'user': str(user.id)})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/user/new', {'name': 'Noah Mansfield', 'password': 'hello_darkness', 'user': str(user.id)})
        self.assertGreater(response.status_code, 399)
        User.objects.filter(name="Noah Mansfield").delete()

    def test_userupdate(self):
        c = Client()
        global user
        response = c.post('/ATC/user/new', {'name': 'Noah Mansfield', 'password': 'hello_darkness', 'user': str(user.id)})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/role/new', {'name': 'ATC', 'isATC': 'True', 'user': str(user.id)})
        self.assertEqual(response.status_code, 302)
        role = Role.objects.get(name="ATC")

        user2 = User.objects.get(name="Noah Mansfield")
        response = c.post('/ATC/user/update', {'id': str(user2.id), 'role': str(role.id), 'user': str(user.id)})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.get(id=user2.id).hasATCPerm(), True)

        User.objects.filter(name="Noah Mansfield").delete()
        Role.objects.filter(id=role.id).delete()


    def testbreakdown(self):
        global office, user
        office.delete()
        user.delete()
