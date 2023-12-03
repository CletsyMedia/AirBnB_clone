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
        """Update the 'updated_at' attribute with the current datetime
        and save the instance to the storage system.
        
        This method ensures that the 'updated_at' attribute reflects the
        most recent modification time, and it then calls the storage system
        to persist the changes.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        return_dict = self.__dict__.copy()
        return_dict["created_at"] = self.created_at.isoformat()
        return_dict["updated_at"] = self.updated_at.isoformat()
        return_dict["__class__"] = self.__class__.__name__
        return return_dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

