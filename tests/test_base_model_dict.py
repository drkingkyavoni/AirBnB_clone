#!/usr/bin/python3
import os
import sys
import unittest

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__))))

from models.base_model import BaseModel


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
        self.assertIsInstance(my_model, BaseModel)

    def test_to_dict(self):
        """
        Test the to_dict() method of BaseModel.

        This method creates a BaseModel instance and sets its attributes.
        It then calls the to_dict() method to convert the BaseModel
        instance to a dictionary.
        The method asserts that the returned object is an instance of
        dict and contains the expected keys.
        Finally, the method asserts that the values of the keys in the
        dictionary match the expected values.

        Parameters:
            self (TestCase): The current test case.

        Returns:
            None
        """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertIsInstance(my_model_json, dict)
        self.assertIn("id", my_model_json)
        self.assertIn("created_at", my_model_json)
        self.assertIn("updated_at", my_model_json)
        self.assertIn("__class__", my_model_json)
        self.assertEqual(my_model_json["__class__"], "BaseModel")
        self.assertEqual(my_model_json["name"], "My_First_Model")
        self.assertEqual(my_model_json["my_number"], 89)


    def test_two_dict(self):
        """
        Test the case where two instances of the BaseModel class
        have the same id.
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        b3 = BaseModel(**bm1.to_dict())
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertEqual(bm1.id, b3.id)