#!/usr/bin/python3
"""module for entry point of a command interpreter"""
import cmd

class HBNBCommand(cmd.Cmd):
    """basic command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to handle end of file character"""
        print()
        return True

    def emptyline(self):
        """Does nothing on empty input line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
