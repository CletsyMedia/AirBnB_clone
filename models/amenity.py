#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity service for lodging.

    Attributes:
        name (str): The descriptive name of the amenity.
    """

    name = ""
