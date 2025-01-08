from django.test import TestCase, TransactionTestCase

from accounts.models import CustomUser

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.db import transaction

class UserModelTestCase(TestCase):
    """
    Tests the custom user model
        Tests if we can succesfully create a user and a superuser
        Tests if you can create a user with a username that already exisits
        Tests if you can create users with the same first and last names 
        Tests for default role assignments for a regular user and an admin user
        Tests that the role for a user can be set after creation and during creation
        Tests for email validity method
        Tests for str method
        test that account deletion sets status to false(inactive)
        Tests that deleted at field is updated on account delettion
        
    """
    @classmethod
    def setUpTestData(cls):
        cls.user1 = CustomUser.objects.create_user(
            username='Testboy1',
            email='testboy@email.com',
            bio='Hello my name is Testboy1 nice to meet you all'
        )

        cls.admin = CustomUser.objects.create_superuser(
            username='root',
            email='root@testcase.com',
            bio='Hello guys, I am root your admin'
        )


    def test_users_creation(self):

        queryset = "<QuerySet [<CustomUser: testboy1>, <CustomUser: root>]>"
        self.assertEqual(str(CustomUser.objects.all()), queryset)

        self.assertEqual(self.user1.username, 'Testboy1')
        self.assertEqual(self.admin.username, 'root')

        self.assertFalse(self.user1.is_staff)
        self.assertTrue(self.admin.is_staff)

    def test_unique_username_already_exist_caseinsensitive(self):

        # Test for IntegrityError for a case-insensitive duplicate username
        with self.assertRaises(IntegrityError):
            with transaction.atomic():  # Isolate this operation
                user2 = CustomUser.objects.create_user(
                    username='testboy1',  # Same as 'testboy1' but case-insensitive
                    email='another@email.com',
                    password='secret12345'
                )

        # Test for IntegrityError for a case-insensitive duplicate superuser username
        with self.assertRaises(IntegrityError):
            with transaction.atomic():  # Isolate this operation
                user3 = CustomUser.objects.create_superuser(
                    username='RooT',  # Same as 'root' but case-insensitive
                    email='testboy@email.com',
                    password='secret12345'
                )

    def test_email_validity(self):
        pass

    def test_password_hashed(self):
        pass

    def test_membership_status(self):
        pass

    def test_permissions(self):
        pass
    