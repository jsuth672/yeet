from django.test import Client, TestCase
from ATC.models import Plane, Role, User


class TestPlane(TestCase):

    def test_plane_create(self):
        c = Client()
        # two users, one ATC, one not
        atc = User.objects.create(name="atc", role=Role(isATC=True))
        not_atc = User.objects.create(name="not atc", role=Role(isATC=False))
        # try creating a plane on not_atc
        response = c.post("ATC/plane/new", {'name': 'plane', 'user': not_atc.id})
        self.assertGreater(response.status_code, 399)
        # create a plane with an atc user
        response = c.post("ATC/plane/new", {'name': 'plane', 'user': atc.id})
        self.assertGreater(response.status_code, 399)

    def test_plane_delete(self):
        c = Client()
        # create two planes
        plane1 = Plane.objects.create(identifier="plane1")
        # two users, one ATC, one not
        atc = User.objects.create(name="atc", role=Role(isATC=True))
        not_atc = User.objects.create(name="not atc", role=Role(isATC=False))
        # make sure the not_atc cannot delete the airline
        response = c.post("ATC/plane/delete", {'name': plane1.identifier, 'user': not_atc.id})
        self.assertGreater(response.status_code, 399)
        # make sure that the atc can delete the airline
        response = c.post("ATC/plane/delete", {'name': plane1.identifier, 'user': atc.id})
        self.assertEqual(len(Plane.objects.filter(name=plane1)), 0)
        # delete the records from the database
        Plane.objects.filter(name=plane1).delete()
        atc.delete()
        not_atc.delete()

