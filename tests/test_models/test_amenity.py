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


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
    def setUp(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        self.assertLess(first_updated_at, am.updated_at)

    def test_two_saves(self):
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        second_updated_at = am.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        am.save()
        self.assertLess(second_updated_at, am.updated_at)

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

    def test_two_amenities_different_updated_at(self):
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_str_representation(self):
        dateT = datetime.today()
        date_repr = repr(dateT)
        amenity = Amenity()
        amenity.id = "123456"
        amenity.created_at = amenity.updated_at = dateT
        amenstr = amenity.__str__()
        self.assertIn("[Amenity] (123456)", amenstr)
        self.assertIn("'id': '123456'", amenstr)
        self.assertIn("'created_at': " + date_repr, amenstr)
        self.assertIn("'updated_at': " + date_repr, amenstr)

    def test_args_unused(self):
        amenity = Amenity(None)
        self.assertNotIn(None, amenity.__dict__.values())

    def test_2_amenities_unique_ids(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_2_amenities_different_created_at(self):
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, amenity2.created_at)

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dateT = datetime.today()
        date_iso = dateT.isoformat()
        amenity = Amenity(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(amenity.id, "345")
        self.assertEqual(amenity.created_at, dateT)
        self.assertEqual(amenity.updated_at, dateT)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

if __name__ == "__main__":
    unittest.main()
