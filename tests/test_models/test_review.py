#!/usr/bin/python3
"""
test_review.py
Module that tests the Review class.
"""


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def setUp(self):
        """Set up for the tests."""
        self.review = Review()
        self.review.text = "Great place!"

    def test_instance(self):
        """Test if review is an instance of Review."""
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        """Test if attributes exist and correspond."""
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.text, "Great place!")


if __name__ == "__main__":
    unittest.main()
