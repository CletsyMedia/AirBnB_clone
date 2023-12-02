#!/usr/bin/python3
"""Defining the HBnB console command"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
