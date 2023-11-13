#!/usr/bin/python3
"""
console.py
Module that contains the entry point of the command interpreter for the AirBnB
clone project.
"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Simple command processor for AirBnB clone."""
    prompt = '(hbnb) '

    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program.
        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program.
        Usage: EOF
        """
        print()
        return True

    def emptyline(self):
        """
        Method called when an empty line is entered in response to the prompt.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of the specified class and saves it to the JSON
        file.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.class_dict:
            print("** class doesn't exist **")
            return
        obj = self.class_dict[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Shows an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Destroys an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representations of instances.
        Usage: all [class name]
        """
        if arg and arg not in self.class_dict:
            print("** class doesn't exist **")
            return
        objs = storage.all()
        print([
            str(objs[key])
            for key in objs if not arg or arg == objs[key].__class__.__name__
        ])

    def do_update(self, arg):
        """
        Updates an instance based on class name and id by adding or updating
        attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split(" ")
        if not args or args[0] == "":
            print("** class name missing **")
            return
        if args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        obj = storage.all()[f"{args[0]}.{args[1]}"]
        value = args[3].strip('"\'')
        setattr(obj, args[2], value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
