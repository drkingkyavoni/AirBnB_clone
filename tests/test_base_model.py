#!/usr/bin/env python3

import unittest
from datetime import datetime
from unittest.mock import patch
from uuid import uuid4

from ..models import storage
from ..models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment before running the test case.

        :param self: The reference to the current instance of the test case.
        :returns: None
        """
        self.model = BaseModel()

    def test_init(self):
        """
        Test the initialization of the object.

        Asserts that the ID is a string representation of a UUID generated by `uuid.uuid4()`.
        Asserts that `created_at` and `updated_at` are instances of the `datetime` class.
        Asserts that `name` is an empty string.
        Asserts that `my_number` is initialized with the value 0.
        Asserts that `storage.new` is called once with the model as an argument.
        """
        self.assertEqual(self.model.id, str(uuid4()))
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.name, "")
        self.assertEqual(self.model.my_number, 0)
        storage.new.assert_called_once_with(self.model)

    def test_init_with_kwargs(self):
        """
        Test the initialization of the BaseModel class with keyword arguments.

        This test case verifies that the BaseModel class can be successfully initialized with keyword arguments. It creates a dictionary `kwargs` containing the keyword arguments `name`, `my_number`, `created_at`, and `updated_at`. Then, it creates an instance of the BaseModel class using the unpacking operator `**kwargs`. Finally, it asserts that the attributes of the created instance match the expected values.

        Parameters:
        - None

        Returns:
        - None
        """
        kwargs = {
            "name": "John",
            "my_number": 123,
            "created_at": "2022-01-01T00:00:00",
            "updated_at": "2022-01-02T00:00:00",
        }
        model = BaseModel(**kwargs)
        self.assertEqual(model.name, "John")
        self.assertEqual(model.my_number, 123)
        self.assertEqual(
            model.created_at, datetime.fromisoformat("2022-01-01T00:00:00")
        )
        self.assertEqual(
            model.updated_at, datetime.fromisoformat("2022-01-02T00:00:00")
        )

    def test_str(self):
        """
        Test if the string representation of the BaseModel object is correct.

        Parameters:
            self (TestBaseModel): The current instance of the TestBaseModel class.

        Returns:
            None
        """
        expected_str = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_save(self):
        """
        Test the save function.

        This function tests the save function of the class. It uses the
        `patch` method to mock the `save` function from the `models.storage`
        module. It then calls the `save` method of the `self.model` object.
        The function asserts that the `updated_at` attribute of the `self.model`
        object is an instance of the `datetime` class. Finally, it asserts that
        the `save` function was called exactly once.

        Parameters:
            None

        Returns:
            None
        """
        with patch("models.storage.save") as mock_save:
            self.model.save()
            self.assertIsInstance(self.model.updated_at, datetime)
            mock_save.assert_called_once()

    def test_to_dict(self):
        """
        Test the 'to_dict' method of the class.

        This method tests the 'to_dict' method of the class and verifies if the output dictionary matches the expected dictionary.

        Parameters:
            self (TestCase): The current instance of the TestCase class.

        Returns:
            None: This method does not return anything.
        """
        expected_dict = {
            "id": self.model.id,
            "__class__": "BaseModel",
            "created_at": self.model.created_at.isoformat(),
            "updated_at": self.model.updated_at.isoformat(),
            "name": self.model.name,
            "my_number": self.model.my_number,
        }
        self.assertEqual(self.model.to_dict(), expected_dict)
