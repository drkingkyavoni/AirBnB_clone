#!/usr/bin/env python3

import unittest
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from ....models.base_model import BaseModel
from ....models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """
        Set up the test case by initializing the file storage and file path.

        This function is called before each test case to ensure that the necessary
        objects and variables are properly set up.

        Parameters:
            self (TestCase): The current test case object.

        Returns:
            None
        """
        self.file_storage = FileStorage()
        self.file_path = "file.json"

    def tearDown(self):
        """
        Tears down the test environment after each test case.

        This method is called automatically by the testing framework after each test case to clean up any resources used during the test. It checks if the file path exists and if it does, it deletes the file.

        Parameters:
        - self: The instance of the test case.

        Returns:
        - None
        """
        if Path(self.file_path).is_file():
            Path(self.file_path).unlink()

    def test_all_returns_empty_dict_when_no_objects(self):
        """
        Test case for the 'test_all_returns_empty_dict_when_no_objects' method.

        This test case ensures that the 'all' method of the 'file_storage' object returns an empty dictionary when there are no objects stored.

        Parameters:
            self (TestClass): The TestClass instance.

        Returns:
            None
        """
        result = self.file_storage.all()
        self.assertEqual(result, {})

    def test_new_adds_object_to_objects_dict(self):
        """
        Test if the `new` method adds an object to the `objects` dictionary.

        Args:
            self: An instance of the test case class.

        Returns:
            None.
        """
        obj = BaseModel()
        self.file_storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertEqual(self.file_storage.all()[key], obj)

    def test_save_writes_to_file(self):
        """
        Test if the save method correctly writes to a file.

        This function creates a new instance of the BaseModel class and adds it to the file storage.
        Then, it uses the patch decorator to replace the "open" function with a StringIO object.
        This allows us to simulate writing to a file without actually creating a physical file.
        The save method is then called on the file storage, and we assert that the value written to the file
        matches the expected JSON string.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """
        obj = BaseModel()
        self.file_storage.new(obj)

        with patch("builtins.open", new=StringIO()) as mock_file:
            self.file_storage.save()
            self.assertEqual(mock_file.getvalue(), '{"SomeClass.123": {}}')

    def test_reload_loads_data_from_file(self):
        """
        Test if the reload() method of the file_storage object loads data from a file correctly.

        Parameters:
            self (TestCase): The current test case.

        Returns:
            None
        """
        data = '{"SomeClass.123": {}}'
        with open(self.file_path, "w") as file:
            file.write(data)

        self.file_storage.reload()
        self.assertEqual(self.file_storage.all(), {"SomeClass.123": {}})
