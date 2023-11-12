#!/usr/bin/python3
"""
test_state.py
Module that tests the State class.
"""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def setUp(self):
        """Set up for the tests."""
        self.state = State()
        self.state.name = "California"

    def test_instance(self):
        """Test if state is an instance of State."""
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        """Test if attributes exist and correspond."""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "California")


if __name__ == "__main__":
    unittest.main()
