#!/usr/bin/python3
"""entry point of command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """prompts user for input"""
    prompt = "tell me what to do "

    def do_quit(self, arg):
        """exit program"""
        return True

    def do_EOF(self, arg):
        """exit on Ctrl+D"""
        print()
        return True

    def emptyline(self) -> bool:
        return super().emptyline()

if __name__ == '__main__':
    HBNBCommand().cmdloop()