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
from models.base_model import BaseModel
from console import HBNBCommand


class HBNBCommandTestCase(unittest.TestCase):
    """Base class for HBNBCommand unittests."""

    def setUp(self):
        """Set up HBNBCommand instance for testing."""
        self.hbnb_cmd = HBNBCommand()


class TestBaseModelInstantiation(HBNBCommandTestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_two_models_unique_ids(self):
        baseModel1 = BaseModel()
        baseModel2 = BaseModel()
        self.assertNotEqual(baseModel1.id, baseModel2.id)

    def test_two_models_different_created_at(self):
        baseModel1 = BaseModel()
        sleep(0.05)
        baseModel2 = BaseModel()
        self.assertLess(baseModel1.created_at, baseModel2.created_at)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dateT = datetime.today()
        date_iso = dateT.isoformat()
        baseModel = BaseModel("12", id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(baseModel.id, "345")
        self.assertEqual(baseModel.created_at, dateT)
        self.assertEqual(baseModel.updated_at, dateT)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_str_representation(self):
        dateT = datetime.today()
        date_repr = repr(dateT)
        baseModel = BaseModel()
        baseModel.id = "123456"
        baseModel.created_at = baseModel.updated_at = dateT
        baseModelstr = baseModel.__str__()
        self.assertIn("[BaseModel] (123456)", baseModelstr)
        self.assertIn("'id': '123456'", baseModelstr)
        self.assertIn("'created_at': " + date_repr, baseModelstr)
        self.assertIn("'updated_at': " + date_repr, baseModelstr)

    def test_args_unused(self):
        baseModel = BaseModel(None)
        self.assertNotIn(None, BaseModel.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dateT = datetime.today()
        date_iso = dateT.isoformat()
        baseModel = BaseModel(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(baseModel.id, "345")
        self.assertEqual(baseModel.created_at, dateT)
        self.assertEqual(baseModel.updated_at, dateT)


class TestBaseModelSave(HBNBCommandTestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        baseModel = BaseModel()
        sleep(0.05)
        first_updated_at = baseModel.updated_at
        baseModel.save()
        self.assertLess(first_updated_at, baseModel.updated_at)

    def test_two_saves(self):
        baseModel = BaseModel()
        sleep(0.05)
        first_updated_at = baseModel.updated_at
        baseModel.save()
        second_updated_at = baseModel.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        baseModel.save()
        self.assertLess(second_updated_at, baseModel.updated_at)

    def test_save_with_arg(self):
        baseModel = BaseModel()
        with self.assertRaises(TypeError):
            baseModel.save(None)

    def test_save_updates_file(self):
        baseModel = BaseModel()
        baseModel.save()
        baseModel_id = "BaseModel." + baseModel.id
        with open("file.json", "r") as f:
            self.assertIn(baseModel_id, f.read())


class TestBaseModelDict(HBNBCommandTestCase):
    """Unittests for testing dict method of the BaseModel class."""

    def test_to_dict_type(self):
        baseModel = BaseModel()
        self.assertTrue(dict, type(baseModel.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        baseModel = BaseModel()
        self.assertIn("id", baseModel.to_dict())
        self.assertIn("created_at", baseModel.to_dict())
        self.assertIn("updated_at", baseModel.to_dict())
        self.assertIn("__class__", baseModel.to_dict())

    def test_to_dict_contains_added_attributes(self):
        baseModel = BaseModel()
        baseModel.name = "Holberton"
        baseModel.my_number = 98
        self.assertIn("name", baseModel.to_dict())
        self.assertIn("my_number", baseModel.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        baseModel = BaseModel()
        bm_dict = baseModel.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        baseModel = BaseModel()
        baseModel.id = "123456"
        baseModel.created_at = baseModel.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(baseModel.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)
