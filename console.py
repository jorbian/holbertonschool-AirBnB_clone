#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd, subprocess


class HBNBCommand(cmd.Cmd):
    intro = ''
    prompt = '(hbnb) '
    file = None

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return self.do_quit("")

    def do_clear(self, arg):
        """Clears the screen."""
        subprocess.run(["clear"])

if __name__ == '__main__':
    HBNBCommand().cmdloop()