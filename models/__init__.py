#!/usr/bin/python3
"""
__init__.py for models directory
Initializes the package and sets up the storage system for the AirBnB clone
project.

This module creates an instance of FileStorage and loads previously saved
objects, making them available across the application.
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
