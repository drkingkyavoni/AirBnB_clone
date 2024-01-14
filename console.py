#!/usr/bin/env python3

import cmd

import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classDict: dict[str, object] = {
    "FileStorage": FileStorage,
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review,
}


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = "(hbnb) "

    @classmethod
    def __checkMissingClassName(cls, arg) -> int:
        """
        Check if the class name is missing.

        Args:
            arg (Any): The argument to check.

        Returns:
            int: 1 if the class name is missing, 0 otherwise.
        """
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
            target_class = classDict.get(argElements[0])
            if not target_class or not issubclass(target_class, BaseModel):
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
    def __destroyClassID(cls, arg):
        """
        This class method destroys an instance of a class identified
        by the given argument.

        Parameters:
            cls (class): The class itself.
            arg (str): The argument used to identify the instance
            to destroy.

        Returns:
            dict: The updated dictionary of instances.

        Note:
            - The argument should be in the format
              "<class name> <instance id>".
            - If the instance does not exist, a message will be
              printed and
              the function will return.
            - The instance will be removed from the dictionary
              of instances.
            - The updated dictionary will be saved and reloaded.
        """
        argElements = arg.split()
        objKey = "{}.{}".format(argElements[0], argElements[1])

        if objKey not in models.storage.all():
            print("{}".format("** no instance found **"))
            return

        models.storage.all().pop(objKey, None)
        models.storage.save()
        models.storage.reload()
        return models.storage.all()

    @classmethod
    def __updateClassID(cls, arg):
        """
        Updates the class ID of an instance.

        Args:
            cls (type): The class.
            arg (str): The argument.

        Returns:
            dict: The updated storage dictionary.
        """
        argElements = arg.split()
        countElements = len(argElements)
        objKey = "{}.{}".format(argElements[0], argElements[1])

        if objKey not in models.storage.all():
            print("{}".format("** no instance found **"))
            return

        if countElements < 3:
            print("{}".format("** attribute name missing **"))
            return

        if len(argElements) < 4:
            print("{}".format("** value missing **"))
            return

        objInstance = models.storage.all().get(objKey)
        setattr(objInstance, argElements[2], argElements[3])
        objInstance.__dict__[argElements[2]] = str(argElements[3])
        objInstance.save()
        return models.storage.all()[objKey]

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
        A function that performs a specific action based on the given
        argument.

        Parameters:
            arg (str): The argument passed to the function.

        Returns:
            None: If the argument is not a valid class name or is
            an empty string.
        """
        target_class = HBNBCommand.__get_class(arg)
        if target_class or not arg:
            objStore = [
                obj.__str__()
                for obj in models.storage.all().values()
                if obj.__class__ is target_class or target_class is None
            ]
            print("{}".format(objStore))
        else:
            return

    def do_show(self, arg):
        """
        This function is responsible for displaying the details of
        a given object instance.

        Parameters:
        - arg: The argument passed to the function.

        Returns:
        - None

        Description:
        - The function first checks if the class name is missing in the
          argument. If it is, the function returns.
        - Next, it checks if the class exists. If it does not, the
          function returns.
        - Then, it checks if the class ID is missing in the argument.
          If it is, the function returns.
        - After that, it retrieves the details of the object instance.
        - Finally, it prints the string representation of the object
          instance.
        """
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
        """
        Destroy an object by ID

        Parameters:
            arg (str): The ID of the object to be destroyed

        Returns:
            None

        """
        if HBNBCommand.__checkMissingClassName(arg):
            return

        if not HBNBCommand.__get_class(arg):
            return

        if HBNBCommand.__checkMissingClassID(arg):
            return

        objInstance = HBNBCommand.__destroyClassID(arg)

        if not objInstance:
            return

        print(objInstance.__str__())

    def do_update(self, arg):
        """
        Updates a class instance based on the given argument.

        Args:
            arg (str): The argument to update the class instance.

        Returns:
            None
        """
        if HBNBCommand.__checkMissingClassName(arg):
            return

        if not HBNBCommand.__get_class(arg):
            return

        if HBNBCommand.__checkMissingClassID(arg):
            return

        objInstance = HBNBCommand.__updateClassID(arg)

        if not objInstance:
            return

        print(objInstance.__str__())


if __name__ == "__main__":
    HBNBCommand().cmdloop()
