#!/usr/bin/python3
"""Defining the HBnB console command"""
import cmd as command
import re as regexp
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity


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
  