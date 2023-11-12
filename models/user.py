#!/usr/bin/python3
"""
user.py
Module that defines the User class for the AirBnB clone project.

The User class inherits from BaseModel and adds additional attributes
specific to a user, such as email, password, first_name, and last_name.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User in the AirBnB clone project."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
