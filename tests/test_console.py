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


class TestHBNBCommandHelp(HBNBCommandTestCase):
    """Unittests for HBNB command interpreter help messages."""

    def test_help_command(self):
        """Test the help command."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help"))
            help_output = output.getvalue().strip()
            print("Actual Output:\n", help_output)  # Add this line for debugging
            self.assertIn("EOF", help_output)
            self.assertIn("all", help_output)
            self.assertIn("count", help_output)
            self.assertIn("create", help_output)
            self.assertIn("destroy", help_output)
            self.assertIn("help", help_output)
            self.assertIn("quit", help_output)
            self.assertIn("show", help_output)
            self.assertIn("update", help_output)

    def test_help_quit_command(self):
        """Test the help command for quit."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help quit"))
            help_output = output.getvalue().strip()
            print("Actual Output:\n", help_output)  # Add this line for debugging
            self.assertIn("Quit command to exit the program.", help_output)


if __name__ == "__main__":
    unittest.main()
