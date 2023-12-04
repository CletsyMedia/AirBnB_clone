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

    @classmethod
    def setUpClass(cls):
        """Set up class-level resources."""
        # Perform setup actions, e.g., rename file.json to tmp and clear objts
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level resources."""
        # Perform teardown actions, e.g., remove file.json and rename tmp back
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

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

    def test_create_missing_class(self):
        """Test create command with a missing class argument."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create"))
            error_output = output.getvalue().strip()
            self.assertIn("** class name missing **", error_output)

    def test_create_invalid_syntax(self):
        """Test create for invalid syntax."""
        test_cases = [
            ("MyModel.create()", "*** Unknown syntax: MyModel.create()"),
            ("BaseModel.create()", "*** Unknown syntax: BaseModel.create()")
        ]

        for command, expected_output in test_cases:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(self.hbnb_cmd.onecmd(command))
                self.assertEqual(expected_output, output.getvalue().strip())

    def test_create_objects(self):
        """Test the 'create' command for multiple classes.

        This test ensures that the 'create' command correctly creates objects
        for each specified class and that the created objects are stored in
        the storage engine.

        It iterates over a list of class names, executes the 'create' command
        for each class, and verifies that the expected object key is present
        in the storage engine.

        Classes tested: BaseModel, User, State, City, Amenity, Place, Review.
        """
        classes = [
            "BaseModel", "User", "State", "City",
            "Amenity", "Place", "Review"
        ]

        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(self.hbnb_cmd.onecmd(f"create {class_name}"))
                self.assertLess(0, len(output.getvalue().strip()))
                test_key = f"{class_name}.{output.getvalue().strip()}"
                self.assertIn(test_key, storage.all().keys())


class TestHBNBCommandShow(HBNBCommandTestCase):
    """Unittests for the show command."""

    @classmethod
    def setUpClass(cls):
        """Set up class-level resources."""
        # Perform setup actions, e.g., rename file.json to tmp and clear objts
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level resources."""
        # Perform teardown actions, e.g., remove file.json and rename tmp back
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

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

    def test_show_id_space_notation(self):
        """Test show command with ID in space notation."""
        # Assuming there is a BaseModel instance with ID '123'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show BaseModel 1 2 3"))
            show_output = output.getvalue().strip()
            self.assertTrue(show_output)

    def test_show_dot_notation(self):
        """Test show command with dot notation."""
        # Assuming there is a BaseModel instance with ID '123'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show BaseModel.123"))
            show_output = output.getvalue().strip()
            self.assertTrue(show_output)

    def test_show_no_instance_found(self):
        """Test show command with no instance found."""
        # Assuming there is no BaseModel instance with ID '789'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show BaseModel 789"))
            error_output = output.getvalue().strip()
            self.assertIn("** no instance can be found **", error_output)

    def test_show_space_notation_no_instance_found(self):
        """Test show command with space notation and no instance found."""
        # Assuming there is no BaseModel instance with ID '101'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show BaseModel 1 0 1"))
            error_output = output.getvalue().strip()
            self.assertIn("** no instance can be found **", error_output)

    def test_show_no_instance_found_dot_notation(self):
        """Test show command with dot notation and no instance found."""
        correct = "** no instance can be found **"

        classes = [
            "BaseModel", "User", "State", "City",
            "Amenity", "Place", "Review"
        ]

        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(self.hbnb_cmd.onecmd(f"{class_name}.show(1)"))
                self.assertEqual(correct, output.getvalue().strip())

    def test_show_objects_space_notation(self):
        """Test show command with 'objects' in space notation."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show objects BaseModel"))
            show_output = output.getvalue().strip()
            self.assertTrue(show_output)


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
            self.assertIn("** class does not exist **", error_output)


class TestHBNBCommandDestroy(HBNBCommandTestCase):
    """Unittests for the destroy command."""

    def test_destroy_command(self):
        """Test the destroy command."""
        # Assuming there is a BaseModel instance with ID '789'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy BaseModel 789"))
            destroy_output = output.getvalue().strip()
            self.assertEqual("** no instance can be found **", destroy_output)

    def test_destroy_invalid_id(self):
        """Test destroy command with an invalid ID."""
        # Assuming there is no BaseModel instance with ID '101'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy BaseModel 101"))
            error_output = output.getvalue().strip()
            self.assertIn("** no instance can be found **", error_output)
            
    def test_destroy_miss_class(self):
        """Test destroy command with missing class."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy"))
            error_output = output.getvalue().strip()
            self.assertIn("** class name is missing **", error_output)

    def test_destroy_invalid_class(self):
        """Test destroy command with an invalid class."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy InvalidClass 123"))
            error_output = output.getvalue().strip()
            self.assertIn("** class doesn't exist **", error_output)


class TestHBNBCommandUpdate(HBNBCommandTestCase):
    """Unittests for the update command."""

    def test_update_command(self):
        """Test the update command."""
        # Assuming there is a BaseModel instance with ID '999'
        update_cmd = "update BaseModel 999 name 'new_name'"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd(update_cmd))
            update_output = output.getvalue().strip()
            self.assertEqual("** no instance found **", update_output)

    def test_update_invalid_attribute(self):
        """Test update command with an invalid attribute."""
        # Assuming there is a BaseModel instance with ID '103'
        update_cmd = "update BaseModel 103 invalid_attribute 'new_value'"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd(update_cmd))
            error_output = output.getvalue().strip()
            self.assertIn("** no instance found **", error_output)


if __name__ == "__main__":
    unittest.main()
