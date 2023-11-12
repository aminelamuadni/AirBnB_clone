#!/usr/bin/python3
"""
test_amenity.py
Module that tests the Amenity class.
"""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def setUp(self):
        """Set up for the tests."""
        self.amenity = Amenity()
        self.amenity.name = "Pool"

    def test_instance(self):
        """Test if amenity is an instance of Amenity."""
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        """Test if attributes exist and correspond."""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "Pool")


if __name__ == "__main__":
    unittest.main()
