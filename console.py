#!/usr/bin/python3

import cmd, subprocess

class HBNBCommand(cmd.Cmd):
    intro = ''
    prompt = '(hbnb) '
    file = None

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return self.do_quit("")

    def do_clear(self, arg):
        subprocess.run(["clear"])

if __name__ == '__main__':
    HBNBCommand().cmdloop()