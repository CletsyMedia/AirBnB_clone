#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUserInstantiation
    TestUserSave
    TestUserDict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User
from console import HBNBCommand


class HBNBCommandTestCase(unittest.TestCase):
    """Base class for HBNBCommand unittests."""

    def setUp(self):
        """Set up HBNBCommand instance for testing."""
        self.hbnb_cmd = HBNBCommand()


class TestUser_instantiation(HBNBCommandTestCase):
    """Unittests for testing instantiation of the User class."""

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))
    
    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User().email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User().password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User().first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User().last_name))


if __name__ == "__main__":
    unittest.main()
