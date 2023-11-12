#!/usr/bin/python3
"""
test_user.py
Module that defines unittests for the User class in the AirBnB clone project.
"""


import time
import unittest
import os
from models.user import User
from datetime import datetime
from models import storage


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up method for each test."""
        self.user = User()
        self.user.email = "test@example.com"
        self.user.password = "password"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

    def tearDown(self):
        """Tear down method for each test."""
        del self.user
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance_creation(self):
        """Test instantiation of User object."""
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """Test if User has the correct attributes."""
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_types(self):
        """Test the type of User attributes."""
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_str_representation(self):
        """Test the string representation of a User instance."""
        user_str = self.user.__str__()
        self.assertIn("[User] ({})".format(self.user.id), user_str)

    def test_save(self):
        """Test the save method of User."""
        old_updated_at = self.user.updated_at
        time.sleep(1)
        self.user.save()
        self.assertNotEqual(old_updated_at, self.user.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of User."""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], 'test@example.com')
        self.assertEqual(user_dict['password'], 'password')
        self.assertEqual(user_dict['first_name'], 'John')
        self.assertEqual(user_dict['last_name'], 'Doe')

    def test_storage(self):
        """Test if the User is correctly stored in FileStorage."""
        self.user.save()
        storage.reload()
        obj = storage.all()["User.{}".format(self.user.id)]
        self.assertEqual(obj.id, self.user.id)


if __name__ == "__main__":
    unittest.main()
