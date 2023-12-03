#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Stands for the BaseModel of the HBnB application"""

    def __init__(self, *args, **kwargs):
        """BaseModel is the base class for all models in this application.

        Attributes:
            id (str): A unique identifier for each instance.
            created_at (datetime): The datetime when an instance is created.
            updated_at (datetime): The datetime when an instance is last updated.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)
            
    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

