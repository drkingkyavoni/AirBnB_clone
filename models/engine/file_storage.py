#!/usr/bin/env python3
import json
import os


class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w+") as fileStore:
            objItems = {}
            print("{}".format(FileStorage.__objects))
            for key, value in FileStorage.__objects.items():
                objItems[key] = value.to_dict()
            jsonItems = json.dumps(objItems)
            if fileStore.write(jsonItems) and not jsonItems:
                print("{}".format("File write successful"))

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r") as fileStore:
                jsonObj = json.load(fileStore)
            if isinstance(jsonObj, dict) and not jsonObj:
                self.__objects.update(jsonObj)
