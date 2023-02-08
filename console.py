#!/usr/bin/python3
"""Module console Creating command interpreter console
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """class for console"""

    prompt = "(hbnb) "
    valid_class = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """handles end of line char"""
        print()
        return True

    def emptyline(self):
        """does nothing on enter"""
        pass

    def do_create(self, arg):
        """Creates new instance of BaseModel"""

        if len(arg) == 0:
            print("** class name missing **")
        elif arg in self.valid_class:
            new = self.valid_class[arg]()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """prints a string representation of instance"""

        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            word = arg.split(' ')
            if word[0] not in self.valid_class:
                print("** class doesn't exist **")
            elif len(word) < 2:
                print("** instance id missing **")
            else:
                key = f'{word[0]}.{word[1]}'
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, obj):
        """Deletes an instance based on class name and id"""

        if obj == "" or obj is None:
            print("** class name missing **")
        else:
            word = obj.split(' ')
            if word[0] not in self.valid_class:
                print("** class doesn't exist **")
            elif len(word) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(word[0], word[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_update(self, arg):
        """updates an instance based on the class name and id"""
        list_arg = arg.split(' ')
        possible_error = ""

        if len(list_arg) < 4:
            possible_error = [
                "class name missing",
                "instance id missing",
                "attribute name missing",
                "value missing"
            ][len(list_arg)]

        other_possible_error = [
            arg == "" or arg is None,
            list_arg[0] not in self.valid_class
        ]
        if any(other_possible_error):
            possible_error = [
                "class name missing",
                "class doesn't exist"
            ][other_possible_error.index(True)]

        if len(possible_error) == 0:
            obj_search = list_arg[0] + "." + list_arg[1]
            if obj_search in storage.all():
                setattr(
                    storage.all()[obj_search], list_arg[2],
                    list_arg[3].strip('\'"')
                )
            else:
                print("** no instance found **")
        else:
            print("** {} **".format(possible_error))

    def do_all(self, arg):
        """prints string representations of all instance"""

        if arg != "":
            word = arg.split(' ')
            if word[0] not in self.valid_class:
                print("** class doesn't exist **")
            else:
                n = [
                    str(obj) for key, obj in storage.all().items()
                    if type(obj).__name__ == word[0]
                ]
                print(n)
        else:
            n = [str(obj) for key, obj in storage.all().items()]
            print(n)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
