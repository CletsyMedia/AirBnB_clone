#!/usr/bin/python3
"""Defining the HBnB console command"""
import cmd as cmd
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
    """Defines the Holbertomdcmd interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "Amenity",
        "City",
        "Place",
        "Review",
        "State",
        "User"
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
        This method terminates the HolbertonBnB command
        interpreter and exits the program. It takes no arguments.

        Returns:
            bool: True to indicate that the program should exit.
        """
        return True

    def do_EOF(self, arg):
        """EOF signals to exit the program.

        This method is called when the user enters the EOF (End Of File)
        character (usually Ctrl-D) to signal the end of input. It terminates
        the HolbertonBnB command interpreter and exits the program.
        It takes no arguments.

        Returns:
            bool: True to indicate that the program should exit.
        """
        print("")
        return True

    def do_create(self, arg):
        """Create a new instance of a class and print its ID.

        Usage: create <class>

        This method creates a new instance of the specified class and
        prints its ID. If the class does not exist, it prints an
        error message.

        Args:
            arg (str): The name of the class to create an instance of.

        Returns:
            None
        """
        arglen = parse(arg)
        if len(arglen) == 0:
            print("** class name missing **")
        elif arglen[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arglen[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        arglen = parse(arg)
        objdictionary = storage.all()
        if len(arglen) == 0:
            print("** class name missing **")
        elif arglen[0] not in HBNBCommand.__classes:
            print("** class does not exist **")
        elif len(arglen) == 1:
            print("** instance id is missing **")
        elif "{}.{}".format(arglen[0], arglen[1]) not in objdictionary:
            print("** no instance can be found **")
        else:
            print(objdictionary["{}.{}".format(arglen[0], arglen[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        arglen = parse(arg)
        objdictionary = storage.all()
        if len(arglen) == 0:
            print("** class name is missing **")
        elif arglen[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arglen) == 1:
            print("** instance id is missing **")
        elif "{}.{}".format(arglen[0], arglen[1]) not in objdictionary.keys():
            print("** no instance can be found **")
        else:
            del objdictionary["{}.{}".format(arglen[0], arglen[1])]
            storage.save()
   
    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        arglen = parse(arg)
        if len(arglen) > 0 and arglen[0] not in HBNBCommand.__classes:
            print("** class does not exist **")
        else:
            objlen = []
            for obj in storage.all().values():
                if len(arglen) > 0 and arglen[0] == obj.__class__.__name__:
                    objlen.append(obj.__str__())
                elif len(arglen) == 0:
                    objlen.append(obj.__str__())
            print(objlen)
  
    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        arglen = parse(arg)
        counter = 0
        for obj in storage.all().values():
            if arglen[0] == obj.__class__.__name__:
                counter += 1
        print(counter)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <attribute_name>, <attribute_value>) or
        <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        arglen = parse(arg)
        objdict = storage.all()

        if len(arglen) == 0:
            print("** class name missing **")
            return False
        if arglen[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arglen) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arglen[0], arglen[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(arglen) == 2:
            print("** attribute name missing **")
            return False
        if len(arglen) == 3:
            try:
                type(eval(arglen[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arglen) == 4:
            obj = objdict["{}.{}".format(arglen[0], arglen[1])]
            if arglen[2] in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[arglen[2]])
                obj.__dict__[arglen[2]] = val_type(arglen[3])
            else:
                obj.__dict__[arglen[2]] = arglen[3]
        elif type(eval(arglen[2])) == dict:
            obj = objdict["{}.{}".format(arglen[0], arglen[1])]
            for k, v in eval(arglen[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    val_type = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = val_type(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
