#!/usr/bin/python3
"""
test_base_model.py
Module that contains the tests for the BaseModel class in the AirBnB clone
project.

These tests validate the functionality of the BaseModel class, ensuring correct
behavior of its initialization, serialization, and attribute management.
"""


import time
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test suite for the BaseModel class.
    """

    def test_id_creation(self):
        """
        Test for checking the creation of a unique ID.
        """
        model = BaseModel()
        self.assertIsNotNone(model.id)

    def test_created_updated_times(self):
        """
        Test to ensure created_at and updated_at times are equal upon creation.
        """
        model = BaseModel()
        self.assertEqual(model.created_at, model.updated_at)

    def test_str_representation(self):
        """
        Test to check the string representation of BaseModel.
        """
        model = BaseModel()
        expected = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(expected, model.__str__())

    def test_save_method(self):
        """
        Test the save method to ensure updated_at is modified.
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        time.sleep(0.01)
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        """
        Test to_dict method to ensure it returns a dictionary with the correct
        keys.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('id', model_dict)


if __name__ == '__main__':
    unittest.main()
