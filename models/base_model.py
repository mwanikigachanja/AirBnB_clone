#!/usr/bin/python3
"""
Base class module containing base class
for Airbnb module.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:

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
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """prints string
        representation of
        an object."""
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates current
        datetime"""
        self.updated_at = datetime.now()
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
