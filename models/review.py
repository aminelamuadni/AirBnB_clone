#!/usr/bin/python3
"""
review.py
Module that defines the Review class.
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    """
    place_id = ""
    user_id = ""
    text = ""
