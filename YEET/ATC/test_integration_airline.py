from django.test import Client, TestCase
from ATC.models import Airline, User, Role


class TestAirline(TestCase):

    def test_airline_read(self):
        c = Client()
        # create airline
        airline = Airline.objects.create(name="BJUAir")
        # two users, one ATC, one not
        atc_role = Role.objects.create(isATC=True)
        not_atc_role = Role.objects.create(isATC=False)
        atc = User.objects.create(name="atc", role=atc_role)
        not_atc = User.objects.create(name="not atc", role=not_atc_role)
        # atc user should be able to access the airline
        response = c.post("ATC/airline/get", {'name': airline.name, 'user': atc.id})
        self.assertEqual(response.status_code, 200)
        # not_atc should not be able to access the airline
        response = c.post("ATC/airline/get", {'name': airline.name, 'user': not_atc.id})
        self.assertEqual(response.status_code, 403)
        # delete from test database
        atc_role.delete()
        not_atc_role.delete()
        airline.delete()
        atc.delete()
        not_atc.delete()

    def test_airline_update(self):
        c = Client()
        # create airlines
        airline1 = Airline.objects.create(name="BJUAir")
        airline2 = Airline.objects.create(name="PCCAir")
        # two users, one ATC, one not
        atc_role = Role.objects.create(isATC=True)
        not_atc_role = Role.objects.create(isATC=False)
        atc = User.objects.create(name="atc", role=atc_role)
        not_atc = User.objects.create(name="not atc", role=not_atc_role)
        # make sure the not_atc cannot rename the airline
        response = c.post("ATC/airline/edit", {'name': airline1.name, 'user': not_atc.id, 'new_name': "AirBRUINS"})
        self.assertGreater(response.status_code, 399)
        # make sure atc can rename an airline
        response = c.post("ATC/airline/edit", {'name': airline1.name, 'user': atc.id, 'new_name': "AirBRUINS"})
        self.assertEqual(response.status_code, 200)
        # make sure atc cannot rename to a name that is already in use
        response = c.post("ATC/airline/edit", {'name': "AirBRUINS", 'user': atc.id, 'new_name': airline2.name})
        self.assertGreater(response.status_code, 399)
        # delete from test database
        atc_role.delete()
        not_atc_role.delete()
        airline1.delete()
        airline2.delete()
        atc.delete()
        not_atc.delete()



