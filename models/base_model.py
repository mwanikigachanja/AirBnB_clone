#!/usr/bin/python3
"""
Base class module containing base class
for Airbnb module.
"""

import uuid
from datetime import datetime

class BaseModel:
    "A base model class"

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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

    def to_dict(self):
        """Dictionary with
        class name of an
        object as key"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict




