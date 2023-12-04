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


class TestHBNBCommandShow(HBNBCommandTestCase):
    """Unittests for the show command."""

    def test_show_invalid_class(self):
        """Test show command with an invalid class."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show InvalidClass 123"))
            error_output = output.getvalue().strip()
            self.assertIn("** class does not exist **",
                          error_output)  # Update this line

    def test_show_invalid_id(self):
        """Test show command with an invalid ID."""
        # Assuming there is no BaseModel instance with ID '456'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show BaseModel 456"))
            error_output = output.getvalue().strip()
            self.assertIn("** no instance can be found **",
                          error_output)  # Update this line


class TestHBNBCommandAll(HBNBCommandTestCase):
    """Unittests for the all command."""

    def test_all_command(self):
        """Test the all command."""
        # Assuming there are some instances in the storage
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("all"))
            all_output = output.getvalue().strip()
            # Assuming the string representations are printed
            self.assertTrue(all_output)

    def test_all_invalid_class(self):
        """Test all command with an invalid class."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("all InvalidClass"))
            error_output = output.getvalue().strip()
            self.assertIn("** class does not exist **", error_output)  # Update this line


class TestHBNBCommandDestroy(HBNBCommandTestCase):
    """Unittests for the destroy command."""

    def test_destroy_command(self):
        """Test the destroy command."""
        # Assuming there is a BaseModel instance with ID '789'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy BaseModel 789"))
            destroy_output = output.getvalue().strip()
            self.assertEqual("", destroy_output)

    def test_destroy_invalid_class(self):
        """Test destroy command with an invalid class."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy InvalidClass 789"))
            error_output = output.getvalue().strip()
            self.assertIn("** class doesn't exist **", error_output)

    def test_destroy_invalid_id(self):
        """Test destroy command with an invalid ID."""
        # Assuming there is no BaseModel instance with ID '101'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy BaseModel 101"))
            error_output = output.getvalue().strip()
            self.assertIn("** no instance found **", error_output)

if __name__ == "__main__":
    unittest.main()
