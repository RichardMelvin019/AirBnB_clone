#!/usr/bin/python3
"""Module for the entry point of the
command interpreter. """

import cmd
import json
from models import *
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command Interpreter. """

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Handles End of File Character. """
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass

    def do_create(self, arg):
        """Creates an instance of the class"""
        if arg:
            if not storage.classes().get(arg):
                print("** class doesn't exist **")
            else:
                insta_obj = storage.classes()[arg]()
                insta_obj.save()
                print(insta_obj.id)
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return
        class_name, *instance = arg.split()
        insta_id = "".join(insta_id)
        if not class_nmae:
            print("** class name missing **")
            return
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if not insta_id:
            print("** instance id missing **")
            return
        key = f"{class_name}.{insta_id}"
        if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        class_name, *insta_id = arg.split()
        insta_id = "".join(insta_id)
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if not insta_id:
            print("** instance id missing **")
            return
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name."""
        insta_obj = storage.all()
        insta_list = []
        if not arg:
            insta_list = [str(value) for value in insta_obj.values()]
        else:
            class_name = arg.strip()
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return
            insta_list = [
                    str(value) for key, value in insta_obj.items()
                    if key.startswith(f"{class_name}.")
                    ]
        print(insta_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        tokens = shlex.split(arg)
        if len(tokens) < 4:
            print("** insufficient arguments **")
            return
        class_name, insta_id, attr_name, value = tokens[:4]
        if not class_name:
            print("** class name missing **")
            return
        if not insta_id:
            print("** instance id missing **")
            return
        if not attr_name:
            print("** attribute name missing **")
            return
        if not value:
            print("** value missing **")
            return
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        key = f"{class_name}.{insta_id}"
        insta_dict = models.storage.all()
        if key not in insta_dict:
            print("** no instance found **")
            return
        instance = insta_dict[key]
        try:
            attr_type = type(getattr(instance, attr_name))
            value = attr_type(value)
        except AttributeError:
            print(f"Attribute '{attr_name}' not found in instance.")
            return

        setattr(instance, attr_name, value)
        models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
