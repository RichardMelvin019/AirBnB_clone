#!/usr/bin/python3
"""Module for the entry point of the
command interpreter. """

import cmd


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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
