#!/usr/bin/python3
"""
user.py
Module that defines the User class for the AirBnB clone project.

The User class inherits from BaseModel and adds additional attributes
specific to a user, such as email, password, first_name, and last_name.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a User in the AirBnB clone project.

    Attributes:
        email (str): Email address of the user.
        password (str): Password for the user account.
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
