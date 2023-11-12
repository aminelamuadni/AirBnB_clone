#!/usr/bin/python3
"""
test_file_storage.py
Test suite for the FileStorage class in the AirBnB clone project.

This class tests the functionality of FileStorage, including serialization,
deserialization, and file storage operations.
"""


import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """Set up method for each test."""
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path

    def tearDown(self):
        """Clean up (delete file) after each test."""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test new() method of FileStorage class."""
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test save() method saves objects to a file."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        self.assertIn('{}.{}'.format('BaseModel', obj.id), data)

    def test_reload(self):
        """Test reload() method for FileStorage class."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
