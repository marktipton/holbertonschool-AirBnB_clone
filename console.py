#!/usr/bin/python3
"""entry point of command interpreter"""
import cmd
import json
import os
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """prompts user for input"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """quit command to exit program"""
        return True

    def do_EOF(self, arg):
        """use Ctrl+D to exit program"""
        print()
        return True

    def emptyline(self):
        """Do nothing if empty line"""
        pass

    def do_create(self, arg):
        """creates new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance_data = new_instance.to_dict()
            print(new_instance.id)

    def do_show(self, arg):
        """prints string rep of instance of BaseModel"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key in FileStorage.__objects:
            print(FileStorage.__objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """destroys instance of BaseModel"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key in FileStorage.__objects:
            del FileStorage.__objects[key]
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """prints string rep of all instances of BaseModel"""
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
        objects = FileStorage.__objects.copy()
        for instance in objects.values():
            instance_string = instance.to_dict()
            print(instance_string)

    def do_update(self, arg):
        """updates instance of BaseModel"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key in FileStorage.__objects:
            if len(args) < 3:
                print ("** attribute name missing **")
            if len(args) < 4:
                print("** value missing **")
                return

            attr_name = args[2]
            attr_value = args[3]

            if key in FileStorage.__objects:
                obj = FileStorage.__objects[key]
            setattr(obj, attr_name, attr_value)
            obj.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
