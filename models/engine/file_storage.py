#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Manage the storage of objects in JSON format.

    Attributes:
        __file_path (str): The file path to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retrieve all stored objects.

        Returns:
            dict: A dictionary containing all instantiated objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the storage.

        Args:
            obj (BaseModel): The object to be added.

        Returns:
            None
        """
        obj_classname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_classname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdictionary = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdictionary, f)

    def reload(self):
        """Load serialized objects from the JSON file.

        Deserialize the JSON file specified by __file_path, if it exists,
        and populate the __objects dictionary with the deserialized objects.

        Returns:
            None
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdictionary = json.load(f)
                for objct in objdictionary.values():
                    class_name = objct["__class__"]
                    del objct["__class__"]
                    self.new(eval(class_name)(**objct))
        except FileNotFoundError:
            return
