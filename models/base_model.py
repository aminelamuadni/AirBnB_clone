#!/usr/bin/python3
"""
base_model.py
Module that defines the BaseModel class for the AirBnB clone project.

The BaseModel class serves as a base class for other models in the application,
providing common attributes and methods such as ID generation and datetime
tracking.
"""


import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class that defines all common attributes
    and methods for other classes.
    """

    def __init__(self):
        """
        Initializes a new instance of BaseModel.
        Attributes:
            id (str): unique id for each instance, generated using uuid.
            created_at (datetime): current datetime when an instance is
            created.
            updated_at (datetime): current datetime when an instance is created
            and will be updated on each object change.
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        String representation of the BaseModel instance.
        Returns:
            str: string representation of the instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id, self.__dict__
        )

    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance.
        Adds the class name to the dictionary and converts datetime objects to
        ISO format strings.
        Returns:
            dict: a dictionary representation of the instance.
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
