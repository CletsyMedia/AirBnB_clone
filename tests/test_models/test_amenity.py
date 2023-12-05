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


class TestAmenitySave(HBNBCommandTestCase):
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
        amenity = Amenity()
        sleep(0.05)
        first_updated_at = amenity.updated_at
        amenity.save()
        self.assertLess(first_updated_at, amenity.updated_at)

    def test_save_with_arg(self):
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.save(None)

    def test_save_updates_file(self):
        amenity = Amenity()
        amenity.save()
        amid = "Amenity." + amenity.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())

    def test_two_saves(self):
        amenity = Amenity()
        sleep(0.05)
        first_updated_at = amenity.updated_at
        amenity.save()
        second_updated_at = amenity.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amenity.save()
        self.assertLess(second_updated_at, amenity.updated_at)


class TestAmenityDict(HBNBCommandTestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        amenity = Amenity()
        self.assertIn("id", amenity.to_dict())
        self.assertIn("created_at", amenity.to_dict())
        self.assertIn("updated_at", amenity.to_dict())
        self.assertIn("__class__", amenity.to_dict())

    def test_to_dict_contains_added_attributes(self):
        amenity = Amenity()
        amenity.middle_name = "Holberton"
        amenity.my_number = 98
        self.assertEqual("Holberton", amenity.middle_name)
        self.assertIn("my_number", amenity.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        amenity = Amenity()
        am_dict = amenity.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        dateT = datetime.today()
        amenity = Amenity()
        amenity.id = "123456"
        amenity.created_at = amenity.updated_at = dateT
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dateT.isoformat(),
            'updated_at': dateT.isoformat(),
        }
        self.assertDictEqual(amenity.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        amenity = Amenity()
        self.assertNotEqual(amenity.to_dict(), amenity.__dict__)

    def test_to_dict_with_arg(self):
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.to_dict(None)


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
