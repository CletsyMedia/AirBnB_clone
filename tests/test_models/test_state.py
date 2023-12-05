#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestStateInstantiation
    TestStateSave
    TestStateDict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State
from console import HBNBCommand


class HBNBCommandTestCase(unittest.TestCase):
    """Base class for HBNBCommand unittests."""

    def setUp(self):
        """Set up HBNBCommand instance for testing."""
        self.hbnb_cmd = HBNBCommand()


class TestState_instantiation(HBNBCommandTestCase):
    """Unittests for testing instantiation of the State class."""

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
