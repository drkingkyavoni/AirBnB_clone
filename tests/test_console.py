#!/usr/bin/env python3

import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        """
        Test the quit command of the HBNBCommand class.

        This function creates an instance of the HBNBCommand class and tests the
        `onecmd` method by passing the argument "quit". It uses the `assertTrue`
        method to assert that the return value of `onecmd` is True, indicating
        that the command was executed successfully. It also uses the `assertEqual`
        method to check that the value of `mock_stdout.getvalue()` is an empty
        string, indicating that no output was printed to the console.

        Args:
            self (TestCase): The current test case.
            mock_stdout (StringIO): A mock object representing the standard output.

        Returns:
            None
        """
        cmd = HBNBCommand()
        self.assertTrue(cmd.onecmd("quit"))
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch("sys.stdout", new_callable=StringIO)
    def test_create_command(self, mock_stdout):
        """
        Test the create_command method of the HBNBCommand class.

        :param mock_stdout: The mock object for the sys.stdout.
        :return: None
        """
        cmd = HBNBCommand()
        self.assertFalse(cmd.onecmd("create"))
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    def test_checkMissingClassName(self):
        """
        Checks if the class name is missing.

        Parameters:
            self (TestClass): An instance of the TestClass.

        Returns:
            int: Returns 1 if the class name is missing, 0 otherwise.
        """
        cmd = HBNBCommand()

        # Case when class name is missing
        self.assertEqual(cmd.__checkMissingClassName(""), 1)

        # Case when class name is provided
        self.assertEqual(cmd.__checkMissingClassName("User"), 0)

    def redirect_stdout(self, method, *args):
        """
        Redirects the standard output to a `StringIO` object, executes the specified `method` with the given `args`, and returns the captured output as a string.

        Parameters:
            method (callable): The method to be executed.
            *args: Variable length argument list.

        Returns:
            str: The captured output as a string.
        """
        output = StringIO()
        with redirect_stdout(output):
            method(*args)
        return output.getvalue().strip()

    def test_do_create(self):
        """
        Test the functionality of the do_create method in the HBNBCommand class.

        Parameters:
            self (TestCase): An instance of the TestCase class.

        Returns:
            None
        """
        cmd = HBNBCommand()

        # Case when class name is missing
        output = self.redirect_stdout(cmd.do_create, "")
        self.assertEqual(output, "** class name missing **")

        # Case when class doesn't exist
        output = self.redirect_stdout(cmd.do_create, "InvalidClass")
        self.assertEqual(output, "** class doesn't exist **")

        # Case when class name is valid
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            cmd.do_create("User")
            output = fakeOutput.getvalue().strip()
            self.assertTrue(output.startswith("User."))
