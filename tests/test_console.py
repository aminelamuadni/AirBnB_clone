#!/usr/bin/python3
"""
test_console.py
Tests for the console (command interpreter) of the AirBnB clone project.
"""


import unittest
from unittest.mock import patch
from io import StringIO
import uuid
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class."""

    def create_test_model(self):
        """Create and return a test BaseModel instance."""
        model = BaseModel()
        model.save()
        return model

    def test_quit(self):
        """Test the quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), '')

    def test_EOF(self):
        """Test the EOF command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), '\n')

    def test_help(self):
        """Test the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertTrue(len(f.getvalue()) > 0)

    @patch('models.storage')
    def test_create(self, mock_storage):
        """Test the create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            uuid_obj = uuid.UUID(output, version=4)
            self.assertEqual(str(uuid_obj), output)

    @patch('models.storage')
    def test_all(self, mock_storage):
        """Test the all command."""
        mock_storage.all.return_value = {}
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertEqual(f.getvalue().strip(), "[]")

    @patch('models.storage')
    def test_destroy(self, mock_storage):
        """Test the destroy command."""
        model = self.create_test_model()
        with patch('sys.stdout', new=StringIO()):
            HBNBCommand().onecmd(f"destroy BaseModel {model.id}")
            self.assertNotIn(f"BaseModel.{model.id}", mock_storage.all())

    @patch('models.storage')
    def test_update(self, mock_storage):
        """Test the update command."""
        model = self.create_test_model()
        with patch('sys.stdout', new=StringIO()):
            HBNBCommand().onecmd(f"update BaseModel {model.id} name 'Test'")
            updated_model = storage.all()[f"BaseModel.{model.id}"]
            self.assertEqual(updated_model.name.strip("'\""), 'Test')


if __name__ == '__main__':
    unittest.main()
