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


class TestHBNBCommandQuit(HBNBCommandTestCase):
    """Unittests for the quit command."""

    def test_quit_command(self):
        """Test the quit command."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(self.hbnb_cmd.onecmd("quit"))
            quit_output = output.getvalue().strip()
            self.assertEqual("", quit_output)

    def test_EOF_command(self):
        """Test the EOF command."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(self.hbnb_cmd.onecmd("EOF"))
            eof_output = output.getvalue().strip()
            self.assertEqual("", eof_output)


class TestHBNBCommandCreate(HBNBCommandTestCase):
    """Unittests for the create command."""

    def test_create_command(self):
        """Test the create command."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create BaseModel"))
            create_output = output.getvalue().strip()
            self.assertTrue(create_output)  # Assuming the ID is printed

    def test_create_invalid_class(self):
        """Test create command with an invalid class."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create InvalidClass"))
            error_output = output.getvalue().strip()
            self.assertIn("** class doesn't exist **", error_output)


class TestHBNBCommandAll(HBNBCommandTestCase):
    """Unittests for the all command."""

    def test_all_command(self):
        """Test the all command."""
        # Assuming there are some instances in the storage
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("all"))
            all_output = output.getvalue().strip()
            self.assertTrue(all_output)  # Assuming the string representations are printed

    def test_all_invalid_class(self):
        """Test all command with an invalid class."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("all InvalidClass"))
            error_output = output.getvalue().strip()
            self.assertIn("** class doesn't exist **", error_output)


if __name__ == "__main__":
    unittest.main()
