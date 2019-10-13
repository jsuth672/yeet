from django.test import Client, TestCase
from ATC.models import Plane, Role, User


class TestPlane(TestCase):

    def test_plane_create(self):
        c = Client()
        # two users, one ATC, one not
        atc_role = Role.objects.create(isATC=True)
        not_atc_role = Role.objects.create(isATC=False)
        atc = User.objects.create(name="atc", role=atc_role)
        not_atc = User.objects.create(name="not atc", role=not_atc_role)
        # try creating a plane on not_atc
        response = c.post("ATC/plane/new", {'name': 'plane', 'user': not_atc.id})
        self.assertGreater(response.status_code, 399)
        # create a plane with an atc user
        response = c.post("ATC/plane/new", {'name': 'plane', 'user': atc.id})
        self.assertEqual(response.status_code, 200)
        # try to create a plane with the same name
        response = c.post("ATC/plane/new", {'name': 'plane', 'user': atc.id})
        self.assertGreater(response.status_code, 399)
        # delete records from database
        not_atc_role.delete()
        atc_role.delete()
        Plane.objects.filter(name='plane1').delete()
        atc.delete()
        not_atc.delete()

    def test_plane_delete(self):
        c = Client()
        # create two planes
        plane1 = Plane.objects.create(identifier="plane1", currentPassengerCount=0, maxPassengerCount=1)
        # two users, one ATC, one not
        atc_role = Role.objects.create(isATC=True)
        not_atc_role = Role.objects.create(isATC=False)
        atc = User.objects.create(name="atc", role=atc_role)
        not_atc = User.objects.create(name="not atc", role=not_atc_role)
        # make sure the not_atc cannot delete the airline
        response = c.post("ATC/plane/delete", {'name': plane1.identifier, 'user': not_atc.id})
        self.assertGreater(response.status_code, 399)
        # make sure that the atc can delete the airline
        response = c.post("ATC/plane/delete", {'name': plane1.identifier, 'user': atc.id})
        self.assertEqual(len(Plane.objects.filter(identifier=plane1)), 0)
        # delete the records from the database
        not_atc_role.delete()
        atc_role.delete()
        Plane.objects.filter(identifier=plane1).delete()
        atc.delete()
        not_atc.delete()

