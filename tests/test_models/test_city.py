#!/usr/bin/python3
"""
test_city.py
Module that tests the City class.
"""


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def setUp(self):
        """Set up for the tests."""
        self.city = City()
        self.city.state_id = "state_id_example"
        self.city.name = "San Francisco"

    def test_instance(self):
        """Test if city is an instance of City."""
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        """Test if attributes exist and correspond."""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.state_id, "state_id_example")
        self.assertEqual(self.city.name, "San Francisco")


if __name__ == "__main__":
    unittest.main()
