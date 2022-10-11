#!/usr/bin/python3
"""Cmd module to develop shell"""

import cmd


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
  
    def do_EOF(self, line):
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        raise SystemExit

if __name__ == '__main__':
    HBNBCommand().cmdloop()