#!/usr/bin/python3
import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """
        Initializes a new instance of the Test class.
        This function creates a new BaseModel object and verifies that it is an instance of the BaseModel class.

        Parameters:
            self (Test): The Test instance.

        Returns:
            None
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_save(self):
        """
        Test the save() method of the BaseModel class.

        This function creates an instance of the BaseModel class and calls its save() method. It then
        asserts that the 'created_at' and 'updated_at' attributes of the instance are not None.

        Parameters:
        - self: the instance of the TestBaseModel class.

        Returns:
        - None
        """
        my_model = BaseModel()
        my_model.save()
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)


    def test_str(self):
        """
        Test the __str__ method of the BaseModel class.

        This test checks if the __str__ method of the BaseModel class returns the expected string representation of the object.
        It creates an instance of the BaseModel class and sets its attributes.
        Then it creates the expected string representation using the format method and compares it with the actual result of calling the __str__ method.

        Parameters:
            self (TestCase): The current test case.

        Returns:
            None
        """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

    def test_two_base_model(self):
        """
        Test the creation of two BaseModel instances and compare their ids.
        """
        bm1 = BaseModel()
        bm2 = BaseModel(**bm1.to_dict())
        self.assertEqual(bm1.id, bm2.id)
