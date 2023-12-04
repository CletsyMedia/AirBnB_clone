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
            actual_output = output.getvalue().strip()
            print("Actual Output:", repr(actual_output))  # Add this line
            self.assertEqual(help_msg, actual_output)




if __name__ == "__main__":
    unittest.main()
