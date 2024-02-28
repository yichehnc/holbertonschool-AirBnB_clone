#!/usr/bin/python3
"""Command interpreter console"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }


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
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, save it to JSON
        abnd prints the id
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args not in class_dict:
            print("** class doesn't exist **")
        else:
            new_model = class_dict[args]()  # create an instance
            new_model.save()
            print(new_model.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance based on
        the class name and id
        """
        args_list = args.split()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in class_dict:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args_list[0], args_list[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])
                # access the value from the storage dictionary

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args_list = args.split()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in class_dict:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args_list[0], args_list[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del (storage.all()[key])
                storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all instances based
        or not on the class name
        """
        object_list = []
        if len(args) == 0:
            for value in storage.all().values():
                object_list.append(str(value))
                # change to str representation of object
            print(object_list)
        elif args not in class_dict:
            print("** class doesn't exist **")
        else:
            for value in storage.all().values():
                if args == value.to_dict()["__class__"]:
                    object_list.append(str(value))
            print(object_list)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute
        """
        args_list = args.split()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in class_dict:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        elif len(args_list) == 2:
            print("** attribute name missing **")
        elif len(args_list) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args_list[0], args_list[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                # convert object to dict,access by updating the key value pair
                # instead of creating a new dict it edits the existing dict
                storage.all()[key].__dict__[args_list[2]] = args_list[3]
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
