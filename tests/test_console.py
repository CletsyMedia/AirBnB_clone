#!/usr/bin/python3
"""Defines unittests for the HBNB console.

This module contains a series of unittest classes to test the functionality
of the HBNB console. Each unittest class focuses on specific aspects of the
console's behavior.

Unittest classes:
    - TestHBNBCommandPrompting: Tests for console prompting behavior.
    - TestHBNBCommandHelp: Tests for console help command.
    - TestHBNBCommandExit: Tests for console exit command.
    - TestHBNBCommandCreate: Tests for console create command.
    - TestHBNBCommandShow: Tests for console show command.
    - TestHBNBCommandAll: Tests for console all command.
    - TestHBNBCommandDestroy: Tests for console destroy command.
    - TestHBNBCommandUpdate: Tests for console update command.
"""
import os
import sys
import unittest
from io import StringIO
from unittest.mock import patch
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class HBNBCommandTestCase(unittest.TestCase):
    """Base class for HBNBCommand unittests."""

    def setUp(self):
        """Set up HBNBCommand instance for testing."""
        self.hbnb_cmd = HBNBCommand()


class TestHBNBCommandPrompting(HBNBCommandTestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        """Test that the command prompt is correctly set."""
        self.assertEqual("(hbnb) ", self.hbnb_cmd.prompt)

    def test_empty_line_output(self):
        """Test the output when an empty line is entered."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommandHelp(HBNBCommandTestCase):
    """Unittests for HBNB command interpreter help messages."""

    def test_help_exit(self):
        """Test help message for quit command."""
        help_msg = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help quit"))
            self.assertEqual(help_msg, output.getvalue().strip())

    def test_help_create(self):
        """Test help message for create command."""
        help_msg = ("Usage: create <class>\n        "
                    "Create a new class instance and print its id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help create"))
            self.assertEqual(help_msg, output.getvalue().strip())

    def test_helping_EOF(self):
        """Test help message for EOF command."""
        help_msg = "EOF signal to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help EOF"))
            self.assertEqual(help_msg, output.getvalue().strip())

    def test_help_show(self):
        help_msg = (
            "Usage: show <class> <id> or <class>.show(<id>)\n        "
            "Display the string representation of a class instance of"
            " a given id."
        )
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help show"))
            self.assertEqual(help_msg, output.getvalue().strip())

    def test_help_scatter(self):
        help_msg = ("Usage: destroy <class> <id>)\n        "
                    "Delete a class instance of a given id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help destroy"))
            self.assertEqual(help_msg, output.getvalue().strip())

    def test_help_allThings(self):
        help_msg = ("Usage: all or all <class> or <class>.all()\n        "
                    "Display string representation of all instances of a class"
                    ".\n  If no class is specified, displays all instantiated "
                    "objects.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help all"))
            self.assertEqual(help_msg, output.getvalue().strip())

    def test_help_counter(self):
        help_msg = ("Usage: count <class> or <class>.count()\n        "
                    "Retrieve the number of instances of a given class.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help count"))
            self.assertEqual(help_msg, output.getvalue().strip())

    def test_help_updater(self):
        help_msg = ("Usage: update <class> <id> <attri_name> <attri_value> or"
                    "\n  <class>.update(<id>, <attri_name>, <attri_value"
                    ">) or\n       <class>.update(<id>, <dictionary>)\n       "
                    "Update a class instance id by adding or updating\n   "
                    "     a given attribute key/value pair or dictionary.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help update"))
            self.assertEqual(help_msg, output.getvalue().strip())

    def test_help(self):
        help_msg = ("Documented commands (type help <topic>):\n"
                    "========================================\n"
                    "EOF all count create destroy  help quit show update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help"))
            self.assertEqual(help_msg, output.getvalue().strip())




if __name__ == "__main__":
    unittest.main()
