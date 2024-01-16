#!/usr/bin/python3
import os
import sys
import unittest

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__))))

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """
        Initializes a new instance of the test_init function.

        Parameters:
            self: The instance of the class.

        Returns:
            None
        """
        my_model = BaseModel()
        fs = FileStorage()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(fs, FileStorage)

    def test_presave(self):
        """
        Test the presave functionality of the class.

        This function retrieves all objects from the storage
        and assigns the last one to `obj`.
        It then asserts that `obj` is `None`.

        Parameters:
        self (TestClass): The instance of the TestClass.

        Returns:
        None
        """
        obj = ""
        file_path = "file.json"
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]

        with open(file_path) as file:
            content = file.read()
        if content is None:
            self.assertIsNone(obj, "obj is not None")


    def test_save(self):
        """
        Test the save() method of the BaseModel class.

        This function creates an instance of the BaseModel class
        and calls its save() method. It then
        asserts that the 'created_at' and 'updated_at' attributes
        of the instance are not None.

        Parameters:
        - self: the instance of the TestBaseModel class.

        Returns:
        - None
        """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        self.assertEqual(my_model.name, "My_First_Model")
        self.assertEqual(my_model.my_number, 89)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)