#!/usr/bin/python3
"""
file_storage.py
Module that defines the FileStorage class for the AirBnB clone project.

This class handles the serialization and deserialization of the BaseModel
instances to and from a JSON formatted file.
"""


import json
import os


class FileStorage:
    """
    Class for serializing instances to a JSON file and deserializing JSON file
    to instances.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds an object to the __objects dictionary."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {
            obj: FileStorage.__objects[obj].to_dict()
            for obj in FileStorage.__objects
        }
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                json_objects = json.load(f)

            for key, value in json_objects.items():
                cls_name = value['__class__']
                if cls_name == 'BaseModel':
                    from models.base_model import BaseModel
                    self.__objects[key] = BaseModel(**value)
                elif cls_name == 'User':
                    from models.user import User
                    self.__objects[key] = User(**value)
