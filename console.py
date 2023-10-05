#!/usr/bin/python3
"""entry point of command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """prompts user for input"""
    prompt = "tell me what to do "

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
        print("creating new instance")

    def do_show(self, arg):
        """prints string rep of instance of BaseModel"""
        print("string rep of instance")

    def do_destroy(self, arg):
        """destroys instance of BaseModel"""
        print("destroying instance")

    def do_all(self, arg):
        """prints string rep of all instances of BaseModel"""
        print("string rep of all instances")

    def do_update(self, arg):
        """updates instance of BaseModel"""
        print("updating instance")

if __name__ == '__main__':
    HBNBCommand().cmdloop()