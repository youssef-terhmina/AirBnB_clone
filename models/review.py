#!/usr/bin/python3
<<<<<<< HEAD
"""This module creates a Review class"""

=======
"""Defines the Review class."""
>>>>>>> 582ae440d83f3959770d62eb40a3bc635c39bddb
from models.base_model import BaseModel


class Review(BaseModel):
<<<<<<< HEAD
    """This is the class for managing review objects"""
=======
    """Represent a review.
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """
>>>>>>> 582ae440d83f3959770d62eb40a3bc635c39bddb

    place_id = ""
    user_id = ""
    text = ""
