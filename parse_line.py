#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import subprocess
import re

from shlex import split

def parse_line(arg):
    """PARSES A GIVEN SET OF ARGUMENTS"""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)

    if curly_braces:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl
    else:
        if brackets:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
        else:
            return [i.strip(",") for i in split(arg)]

test1 = "{asdf} {asdfadfs}"

print(parse_line(test1))