from django.test import Client, TestCase
from ATC.models import User, Role


class test_User(TestCase):

    def test_usercreate(self):
        c = Client()  # instantiate the Django test client

        response = c.get('/ATC/new')
        self.assertEqual(response.status_code, 200)

        response = c.post('/ATC/user/new', {'name': 'Noah Mansfield', 'password': 'hello_darkness'})
        self.assertEqual(response.status_code, 302)

        response = c.post('/ATC/user/new', {'name': 'Noah Mansfield', 'password': 'hello_darkness'})
        self.assertGreater(response.status_code, 399)
        User.objects.filter(name="Noah Mansfield").delete()

    def test_userupdate(self):
        c = Client()
        response = c.post('/ATC/user/new', {'name': 'Noah Mansfield', 'password': 'hello_darkness'})
        self.assertEqual(response.status_code, 302)

        role = Role(name='ATC',isATC=True).save()
        user = User.objects.get(name="Noah Mansfield")
        response = c.post('/ATC/user/update', {'id': user.id, 'role': role.id })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.get(id=user.id).hasATCPerm(),True)

        User.objects.filter(name="Noah Mansfield").delete()
        Role.objects.filter(id=role.id).delete()



