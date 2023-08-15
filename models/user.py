#!/usr/bin/python3
<<<<<<< HEAD
"""This module creates a User class"""
=======
"""Defines the User class."""
>>>>>>> 582ae440d83f3959770d62eb40a3bc635c39bddb
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """This is the class for managing user objects"""
=======
    """Represent a User.
    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
>>>>>>> 582ae440d83f3959770d62eb40a3bc635c39bddb

    email = ""
    password = ""
    first_name = ""
    last_name = ""
