#!/usr/bin/python3
"""module for entry point of a command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
import json

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
    def do_create(self, arg):
        """creates a new instance of BaseModel,
        save it(to the JSON file) and prints the id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            nw_instnc = storage.classes()[arg]()
            nw_instnc.save()
            print(nw_instnc.id)
    def do_show(self, arg):
        """Prints the str representation of an instance
        based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            instance = instances.get(key)
            if instance is None:
                print("** no instance found **")
            else:
                print(instance)
    def do_destroy(self, arg):
        """Deletes an instance based on the class and id(
        save the change into the JSON file)"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()
    def do_all(self, arg):
        """prints all string representation of all instances
        based or not on the class name"""
        args = arg.split()
        instances = storage.all()
        if not args:
            """no class name, prints all instances"""
            print([str(instance) for instance in instances.values()])
        elif args[0] not in storage.classes():
            """class doesn't exist"""
            print("** class doesn't exist **")
        else:
            lst_instance = [str(instance) for instance in instances.values()
                    if instance.__class__.__name__ == args[0]]
            print(lst_instance)

    def do_update(self, arg):
        """updates an instances based on the class name and id by
        adding or updating attribute"""
        args = arg.split()
        insts = storage.all()

        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            inst = insts.get(key)
            if inst is None:
                print("** no instance found **")
            else:
                attribute_nm = args[2]
                attribute_val = args[3]
                setattr(inst, attribute_nm, attribute_val)
                inst.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
