#!/usr/bin/python3
"""Defining the HBnB console command"""
import cmd as command
import re as regexp
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


def parse(arg):
    braces_tokens = regexp.search(r"\{(.*?)\}", arg)
    brackets_tokens = regexp.search(r"\[(.*?)\]", arg)
    if braces_tokens is None:
        if brackets_tokens is None:
            return [i.strip(",") for i in split(arg)]
        else:
            braces_lexer = split(arg[:brackets_tokens.span()[0]])
            bracket_retl = [i.strip(",") for i in braces_lexer]
            bracket_retl.append(brackets_tokens.group())
            return bracket_retl
    else:
        braces_lexer = split(arg[:braces_tokens.span()[0]])
        bracket_retl = [i.strip(",") for i in braces_lexer]
        bracket_retl.append(braces_tokens.group())
        return bracket_retl


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "Amenity",
        "City",
        "Place",
        "Review"
        "State",
        "User",
    }

    def emptyline(self):
        """Do nothing when receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdictionary = {
            "all": self.do_all,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "show": self.do_show,
            "update": self.do_update
        }
        match = regexp.search(r"\.", arg)
        if match is not None:
            arglen = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = regexp.search(r"\((.*?)\)", arglen[1])
            if match is not None:
                command = [arglen[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdictionary.keys():
                    call = "{} {}".format(arglen[0], command[1])
                    return argdictionary[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program.

        This method terminates the HolbertonBnB command interpreter and exits the program. It takes no arguments.

        Returns:
            bool: True to indicate that the program should exit.
        """
        return True

    def do_EOF(self, arg):
        """EOF signals to exit the program.

        This method is called when the user enters the EOF (End Of File) character (usually Ctrl-D) to signal the end of input. It terminates the HolbertonBnB command interpreter and exits the program. It takes no arguments.

        Returns:
            bool: True to indicate that the program should exit.
        """
        print("")
        return True
