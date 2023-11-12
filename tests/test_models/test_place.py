#!/usr/bin/python3
"""
test_place.py
Module that tests the Place class.
"""


import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def setUp(self):
        """Set up for the tests."""
        self.place = Place()
        self.place.name = "My place"
        self.place.description = "A cozy house"
        # Set other attributes as needed

    def test_instance(self):
        """Test if place is an instance of Place."""
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        """Test if attributes exist and correspond."""
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        # Test other attributes
        self.assertEqual(self.place.name, "My place")
        self.assertEqual(self.place.description, "A cozy house")


if __name__ == "__main__":
    unittest.main()
