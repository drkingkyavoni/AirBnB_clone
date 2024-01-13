#!/usr/bin/env python3

import cmd

import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

classDict = {"BaseModel": BaseModel, "FileStorage": FileStorage}


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = "(hbnb) "

    @classmethod
    def __checkMissingClassName(cls, arg) -> int:
        if not arg:
            print("{}".format("** class name missing **"))
            return 1
        return 0

    @classmethod
    def __get_class(cls, arg):
        """Returns the class object for the given class name"""
        argElements = arg.split()
        objClass: object = None
        try:
            if argElements[0] != "BaseModel":
                print("{}".format("** class doesn't exist **"))
                objClass = None
            else:
                objClass = classDict.get(argElements[0])
        except KeyError:
            print("{}".format("** class doesn't exist **"))
        finally:
            return objClass

    @classmethod
    def __checkMissingClassID(cls, arg):
        """
        Check if the given argument has a missing class ID.

        Args:
            arg (str): The argument to be checked.

        Returns:
            int: 1 if the class ID is missing, 0 otherwise.
        """

        argElements = arg.split()

        if len(argElements) < 2:
            print("{}".format("** instance id missing **"))
            return 1
        return 0

    @classmethod
    def __get_classDetails(cls, arg):
        """
        Get the details of a class.

        Args:
            cls (type): The class object.
            arg (str): The argument for getting the class details.

        Returns:
            The instance of the class if found, else None.
        """
        argElements = arg.split()

        objKey = "{}.{}".format(argElements[0], argElements[1])

        if objKey not in models.storage.all():
            print("{}".format("** no instance found **"))
            return

        return models.storage.all().get(objKey)

    @classmethod
    def __get_destroyClassID(cls, arg):
        argElements = arg.split()
        objKey = "{}.{}".format(argElements[0], argElements[1])

        if objKey not in models.storage.all():
            print("{}".format("** no instance found **"))
            return

        models.storage.all().pop(objKey, None)
        models.storage.save()
        models.storage.reload()
        return models.storage.all()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """
        Creates a new object based on the given argument.

        Args:
            arg (str): The name of the class to create an object from.

        Returns:
            None

        Raises:
            None
        """
        if HBNBCommand.__checkMissingClassName(arg):
            return

        objClass = HBNBCommand.__get_class(arg)
        if not objClass:
            return

        obj = objClass()
        obj.save()
        print("{}".format(obj.id))

    def do_all(self, arg):
        """
        A function that performs a specific action based on the given argument.

        Parameters:
            arg (str): The argument passed to the function.

        Returns:
            None: If the argument is not a valid class name or is an empty string.
        """
        if HBNBCommand.__get_class(arg) or arg == "":
            print([obj.__str__() for obj in models.storage.all().values()])
        else:
            return

    def do_show(self, arg):
        if HBNBCommand.__checkMissingClassName(arg):
            return

        if not HBNBCommand.__get_class(arg):
            return

        if HBNBCommand.__checkMissingClassID(arg):
            return

        objInstance = HBNBCommand.__get_classDetails(arg)

        if not objInstance:
            return

        print(objInstance.__str__())

    def do_destroy(self, arg):
        if HBNBCommand.__checkMissingClassName(arg):
            return

        if not HBNBCommand.__get_class(arg):
            return

        if HBNBCommand.__checkMissingClassID(arg):
            return

        objInstance = HBNBCommand.__get_destroyClassID(arg)

        if not objInstance:
            return

        print(objInstance.__str__())


if __name__ == "__main__":
    HBNBCommand().cmdloop()
