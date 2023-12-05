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
