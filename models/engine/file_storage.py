#!/usr/bin/python3
<<<<<<< HEAD
"""Module for FileStorage class."""
import datetime
import json
import os


class FileStorage:

    """This is the class for storing and retrieving data"""
=======
""" FileStorage class """
import json
from models.base_model import BaseModel
import datetime
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file
    to instances.
    ATTRIBUTES:
    __file_pathh is a private class attribute (str) path to the JSON file
    __objects is a private class attribute (dict) that is empty but will
    store all objects by <class name>.id ex: to store a BaseModel object
    with id=12121212, the key will be BaseModel.12121212)
    PUBLIC INSTANCE METHODS
    all():
    new(obj):
    save():
    reload():
    """
>>>>>>> 582ae440d83f3959770d62eb40a3bc635c39bddb
    __file_path = "file.json"
    __objects = {}

    def all(self):
<<<<<<< HEAD
        """This returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """This sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """This serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def classes(self):
        """This returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """This reloads the stored objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            # TODO: should this overwrite or insert?
            FileStorage.__objects = obj_dict

    def attributes(self):
        """This returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
=======
        """ all method that returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ new method sets in __objects the obj with
        key <obj class name>.id """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """ save method serializes __objects to the JSON file
        (path: __file_path) """
        with open(FileStorage.__file_path, encoding='utf-8', mode='w') as file:
            new_d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(new_d, file)

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesnt exist,
        no exception should be raised) """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except Exception:
            pass
>>>>>>> 582ae440d83f3959770d62eb40a3bc635c39bddb
