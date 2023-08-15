#!/usr/bin/python3
<<<<<<< HEAD
"""This script is the base model"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """This is the class from which all other classes will inherit"""

    def __init__(self, *args, **kwargs):
        """This initializes instance attributes

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
=======
"""
Class base model
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """
    BaseModel that defines all common attributes/methods for other classes
    PUBLIC INSTANCE ATTRIBUTES:
    id: string - assign with an uuid when an instance is created
         uuid.uuid4(): generate a unique id but cant forget to
         convert to string. The goal is to have a unique id for each BaseModel
    created_at:  datetime - assign with the current datetime when an instance
                 is created
    updated_at: datetime - assign with the current datetime when an instance
                is created and it will be updated every time you change your
                object
    __str__: should print: [<class name>] (<self.id>) <self.__dict__>
    PUBLIC INSTANCE METHODS
    save(self):
    to_dict(self):
    """
    def __init__(self, *args, **kwargs):
        """ initialization """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "__class__":
                    setattr(self, key, type(self))
                else:
                    setattr(self, key, value)
>>>>>>> 582ae440d83f3959770d62eb40a3bc635c39bddb
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
<<<<<<< HEAD
            storage.new(self)

    def __str__(self):
        """Returns official string representation"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """This returns a dictionary containing all keys/values of __dict__"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
=======
            models.storage.new(self)

    def __str__(self):
        """
        __str__ method should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """
        save method  updates the public instance attribute updated_at
        with the current datetim
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        This method will be the first piece of the serialization/
        deserialization process: create a dictionary representation
        with simple object type of our BaseModel.
        By using self.__dict__, only instance attributes set will be returned.
        A key __class__ must be added to this dictionary with the class name
        of the object.
        created_at and updated_at must be converted to string object in
        ISO format.
        Format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
        Returns: a dictionary containing all keys/values of __dict__
                 of the instance.
        """
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
>>>>>>> 582ae440d83f3959770d62eb40a3bc635c39bddb
