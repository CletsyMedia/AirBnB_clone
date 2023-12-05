#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

This module contains a series of unittest classes to test the functionality
of the HBNB console. Each unittest class focuses on specific aspects of the
console's behavior.

Unittest classes:
    TestBaseModelInstantiation
    TestBaseModelSave
    TestBaseModelDict
"""
from datetime import datetime
import unittest
import models
import os
from time import sleep
from models.amenity import Amenity
from console import HBNBCommand


class HBNBCommandTestCase(unittest.TestCase):
    """Base class for HBNBCommand unittests."""

    def setUp(self):
        """Set up HBNBCommand instance for testing."""
        self.hbnb_cmd = HBNBCommand()


class TestBaseModelInstantiation(HBNBCommandTestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())