#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

This module contains a series of unittest classes to test the functionality
of the HBNB console. Each unittest class focuses on specific aspects of the console's behavior.

Unittest classes:
    TestAmenityInstantiation
    TestAmenitySave
    TestAmenityDict
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


class TestAmenityInstantiation(HBNBCommandTestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_name_is_public_class_attribute(self):
        amenity = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amenity.__dict__)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
