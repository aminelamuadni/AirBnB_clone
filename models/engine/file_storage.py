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

    Attributes:
        __file_path (str): The path to the JSON file that stores the serialized
        data.
        __objects (dict): A dictionary to store all objects by <class name>.id.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds an object to the __objects dictionary.

        Args:
            obj (BaseModel): The object to be added to the storage.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
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
        """
        Deserializes the JSON file to __objects if __file_path exists.
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                json_objects = json.load(f)

            for key, value in json_objects.items():
                cls_name = value['__class__']
                self.deserialize_object(cls_name, key, value)

    def deserialize_object(self, cls_name, key, value):
        """
        Helper method to deserialize an object based on class name.

        Args:
            cls_name (str): The name of the class.
            key (str): The key in the __objects dictionary.
            value (dict): The dictionary representation of the object to
            deserialize.
        """
        if cls_name == 'BaseModel':
            from models.base_model import BaseModel
            self.__objects[key] = BaseModel(**value)
        elif cls_name == 'User':
            from models.user import User
            self.__objects[key] = User(**value)
        elif cls_name == 'State':
            from models.state import State
            self.__objects[key] = State(**value)
        elif cls_name == 'City':
            from models.city import City
            self.__objects[key] = City(**value)
        elif cls_name == 'Amenity':
            from models.amenity import Amenity
            self.__objects[key] = Amenity(**value)
        elif cls_name == 'Place':
            from models.place import Place
            self.__objects[key] = Place(**value)
        elif cls_name == 'Review':
            from models.review import Review
            self.__objects[key] = Review(**value)
