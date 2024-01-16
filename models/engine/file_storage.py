#!/usr/bin/python3
import json
from pathlib import Path

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classDict: dict[str, object] = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review,
}


class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    def __init__(self) -> None:
        """
        Initializes an instance of the class.

        Parameters:
            self: The instance of the class.

        Returns:
            None.
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        objItems = {
            key: value.to_dict() for key, value in self.__objects.items()
        }

        with open(self.__file_path, "w") as fileStore:
            json.dump(objItems, fileStore, indent=4)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if not Path(self.__file_path).is_file():
            return

        with open(self.__file_path, "r") as file:
            obj_items = json.load(file)

        if not obj_items:
            return

        self.__objects = {
            key: classDict[obj["__class__"]](**obj)
            for key, obj in obj_items.items()
        }
