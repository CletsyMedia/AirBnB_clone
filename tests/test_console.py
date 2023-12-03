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
# import sys
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

    def help_quit(self):
        """Test help message for quit command."""
        help_msg = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help quit"))
            self.assertEqual(help_msg, output.getvalue().strip())

    def help_create(self):
        """Test help message for create command."""
        help_msg = ("Usage: create <class>\n        "
                    "Create a new class instance and print its id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help create"))
            self.assertEqual(help_msg, output.getvalue().strip())

    def help_EOF(self):
        """Test help message for EOF command."""
        help_msg = "EOF signal to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help EOF"))
            self.assertEqual(help_msg, output.getvalue().strip())

    def help_show(self):
        help_msg = (
            "Usage: show <class> <id> or <class>.show(<id>)\n        "
            "Display the string representation of a class instance of"
            " a given id."
        )
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help show"))
            self.assertEqual(help_msg, output.getvalue().strip())

    def help_destroy(self):
        help_msg = ("Usage: destroy <class> <id>)\n        "
                    "Delete a class instance of a given id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help destroy"))
            self.assertEqual(help_msg, output.getvalue().strip())

    def help_all(self):
        help_msg = ("Usage: all or all <class> or <class>.all()\n        "
                    "Display string representation of all instances of a class"
                    ".\n  If no class is specified, displays all instantiated "
                    "objects.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help all"))
            self.assertEqual(help_msg, output.getvalue().strip())

    def help_count(self):
        help_msg = ("Usage: count <class> or <class>.count()\n        "
                    "Retrieve the number of instances of a given class.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help count"))
            self.assertEqual(help_msg, output.getvalue().strip())

    def help_update(self):
        help_msg = ("Usage: update <class> <id> <attri_name> <attri_value> or"
                    "\n  <class>.update(<id>, <attri_name>, <attri_value"
                    ">) or\n       <class>.update(<id>, <dictionary>)\n       "
                    "Update a class instance id by adding or updating\n   "
                    "     a given attribute key/value pair or dictionary.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help update"))
            self.assertEqual(help_msg, output.getvalue().strip())

    def help(self):
        help_msg = ("Documented commands (type help <topic>):\n"
                    "========================================\n"
                    "EOF all count create destroy  help quit show update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("help"))
            self.assertEqual(help_msg, output.getvalue().strip())


class TestHBNBCommandExit(HBNBCommandTestCase):
    """Unittests for exiting from the HBNB command interpreter."""

    def quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(self.hbnb_cmd.onecmd("quit"))

    def EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(self.hbnb_cmd.onecmd("EOF"))


class TestHBNBCommandCreate(HBNBCommandTestCase):
    """Unittests for testing create from the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def create_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create"))
            self.assertEqual(correct, output.getvalue().strip())

    def create_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def create_invalid_syntax(self):
        correct = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("MyModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())
        correct = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("BaseModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())

    def create_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "User.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "State.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "City.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "Place.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "Review.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())


class TestHBNBCommandShow(HBNBCommandTestCase):
    """Unittests for testing show from the HBNB command interpreter"""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def show_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd(".show()"))
            self.assertEqual(correct, output.getvalue().strip())

    def show_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("MyModel.show()"))
            self.assertEqual(correct, output.getvalue().strip())

    def show_missing_id_space_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show BaseModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show User"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show State"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show City"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show Amenity"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show Place"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show Review"))
            self.assertEqual(correct, output.getvalue().strip())

    def show_missing_id_dot_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("BaseModel.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("User.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("State.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("City.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("Amenity.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("Place.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("Review.show()"))
            self.assertEqual(correct, output.getvalue().strip())

    def show_no_instance_found_space_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show BaseModel 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show User 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show State 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show City 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show Amenity 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show Place 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("show Review 1"))
            self.assertEqual(correct, output.getvalue().strip())

    def show_no_instance_found_dot_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("BaseModel.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("User.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("State.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("City.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("Amenity.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("Place.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("Review.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())

    def show_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create BaseModel"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "show BaseModel {}".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create User"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(testID)]
            command = "show User {}".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create State"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(testID)]
            command = "show State {}".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create Place"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(testID)]
            command = "show Place {}".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create City"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(testID)]
            command = "show City {}".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create Amenity"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "show Amenity {}".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create Review"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(testID)]
            command = "show Review {}".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create BaseModel"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "BaseModel.show({})".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create User"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(testID)]
            command = "User.show({})".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create State"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(testID)]
            command = "State.show({})".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create Place"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(testID)]
            command = "Place.show({})".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create City"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(testID)]
            command = "City.show({})".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create Amenity"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "Amenity.show({})".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create Review"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(testID)]
            command = "Review.show({})".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())


class TestHBNBCommandDestroy(HBNBCommandTestCase):
    """Unittests for testing destroy from the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        storage.reload()

    def destroy_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd(".destroy()"))
            self.assertEqual(correct, output.getvalue().strip())

    def destroy_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("MyModel.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())

    def destroy_id_missing_space_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy BaseModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy User"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy State"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy City"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy Amenity"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy Place"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy Review"))
            self.assertEqual(correct, output.getvalue().strip())

    def destroy_id_missing_dot_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("BaseModel.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("User.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("State.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("City.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("Amenity.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("Place.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("Review.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())

    def destroy_invalid_id_space_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy BaseModel 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy User 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy State 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy City 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy Amenity 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy Place 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("destroy Review 1"))
            self.assertEqual(correct, output.getvalue().strip())

    def destroy_invalid_id_dot_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("BaseModel.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("User.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("State.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("City.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("Amenity.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("Place.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("Review.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())

    def destroy_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create BaseModel"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "destroy BaseModel {}".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create User"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(testID)]
            command = "show User {}".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create State"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(testID)]
            command = "show State {}".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create Place"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(testID)]
            command = "show Place {}".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create City"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(testID)]
            command = "show City {}".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create Amenity"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "show Amenity {}".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create Review"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(testID)]
            command = "show Review {}".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertNotIn(obj, storage.all())

    def destroy_objects_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create BaseModel"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "BaseModel.destroy({})".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create User"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(testID)]
            command = "User.destroy({})".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create State"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(testID)]
            command = "State.destroy({})".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create Place"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(testID)]
            command = "Place.destroy({})".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create City"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(testID)]
            command = "City.destroy({})".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create Amenity"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "Amenity.destroy({})".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_cmd.onecmd("create Review"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(testID)]
            command = "Review.destory({})".format(testID)
            self.assertFalse(self.hbnb_cmd.onecmd(command))
            self.assertNotIn(obj, storage.all())


class TestHBNBCommandAll(HBNBCommandTestCase):
    """Unittests for testing all of the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_all_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.all()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_all_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    def test_all_objects_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    def test_all_single_object_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all City"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

    def test_all_single_object_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
