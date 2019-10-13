from django.test import TestCase
from ATC.models import User, Role


class TestUserHasATCPerm(TestCase):

    # written by Ryan Longacre
    def test_assert(self):
        user_with_perm = User(name="Joe", password="secure password", role=Role(isATC=True))
        self.assertEqual(user_with_perm.hasATCPerm(), True)
        user_without_perm = User(name="Not Joe", password="more secure password", role=Role(isATC=False))
        self.assertEqual(user_without_perm.hasATCPerm(), False)


class TestUserHasGatePerm(TestCase):

    # written by Ryan Longacre
    def test_assert(self):
        user_with_perm = User(name="Joe", password="secure password", role=Role(isGate=True))
        self.assertEqual(user_with_perm.hasGatePerm(), True)
        user_without_perm = User(name="Not Joe", password="more secure password", role=Role(isGate=False))
        self.assertEqual(user_without_perm.hasGatePerm(), False)
