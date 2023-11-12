#!/usr/bin/python3
"""
test_console.py
Module that tests the console module.
"""

import unittest
from unittest.mock import patch, create_autospec
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class."""

    def setUp(self):
        """Set up the test case environment."""
        self.cli = HBNBCommand()

    def tearDown(self):
        """Clean up after test case."""
        pass

    def test_quit(self):
        """Test quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.cli.onecmd("quit"))

    def test_EOF(self):
        """Test EOF command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.cli.onecmd("EOF"))

    def test_emptyline(self):
        """Test empty line input."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.cli.onecmd(""))

    def test_create(self):
        """Test create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_show(self):
        """Test show command."""
        obj = BaseModel()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f"show BaseModel {obj.id}")
            output = f.getvalue().strip()
            self.assertIn(obj.id, output)

    def test_destroy(self):
        """Test destroy command."""
        obj = BaseModel()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f"destroy BaseModel {obj.id}")
            self.assertNotIn(obj.id, storage.all())

    def test_all(self):
        """Test all command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output)

    @patch('models.storage')
    def test_update(self, mock_storage):
        """Test the update command."""
        model = BaseModel()
        model.save()

        with patch('sys.stdout', new=StringIO()):
            HBNBCommand().onecmd(f"update BaseModel {model.id} name \"Test\"")

        updated_model = storage.all().get(f"BaseModel.{model.id}", None)

        self.assertIsNotNone(updated_model)
        self.assertEqual(getattr(updated_model, "name", ""), 'Test')


if __name__ == "__main__":
    unittest.main()
