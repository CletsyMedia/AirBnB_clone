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

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))




if __name__ == "__main__":
    unittest.main()
