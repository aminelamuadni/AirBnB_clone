#!/usr/bin/python3
"""
review.py
Module that defines the Review class.
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.

    Attributes:
        place_id (str): The Place.id of the place the review is for.
        user_id (str): The User.id of the user who wrote the review.
        text (str): The text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
