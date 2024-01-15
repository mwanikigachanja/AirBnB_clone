#!/usr/bin/python3
"""
amenity module inheriting from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Class
    attributes:
        name (str) -> Name of the amenity
    """
    name = ""
