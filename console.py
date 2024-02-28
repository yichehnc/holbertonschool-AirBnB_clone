#!/usr/bin/python3
"""Command interpreter console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This defines the HBNB Command Class"""
    prompt = '(hbnb) '

    # EOF
    def do_EOF(self, args):
        """EOF command <Ctrl + D> to exit the program"""
        print()
        return True

    # quit
    def do_quit(self, args):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
