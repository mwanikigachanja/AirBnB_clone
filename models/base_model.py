#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the AirBnB clone console.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:

<<<<<<< HEAD
    """BaseModel that defines all common
    attributes/methods for other classes
    """
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """Args constructor
        args: list arguments
        kwargs: key value args
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, self.DATE_FORMAT)
                setattr(self, key, value)
=======
    """Class for base model of object hierarchy."""

    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance.

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
>>>>>>> ae015a04f9f70f802bb1d1126321389dc4b24beb
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a human-readable string representation
        of an instance."""

        return "[{}] ({}) {}".\
<<<<<<< HEAD
            format(self.__class__.__name__, self.id, self.__dict__)
=======
            format(type(self).__name__, self.id, self.__dict__)
>>>>>>> ae015a04f9f70f802bb1d1126321389dc4b24beb

    def save(self):
        """Updates the updated_at attribute
        with the current datetime."""

        self.updated_at = datetime.now()
<<<<<<< HEAD
        storage.save(self)

    def to_dict(self):
        """Dictionary with
        class name of an
        object as key"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self)
        obj_dict['created_at'] = obj_dict['created_at'].\
            strftime(self.DATE_FORMAT)
        obj_dict['updated_at'] = obj_dict['updated_at'].\
            strftime(self.DATE_FORMAT)
        return obj_dict
=======
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an instance."""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
>>>>>>> ae015a04f9f70f802bb1d1126321389dc4b24beb
