import unittest

from ...models.base_model import BaseModel
from ...models.city import City


class TestCity(unittest.TestCase):
    def test_city_initialization(self):
        """
        Test the initialization of a city object.

        This function creates a city object with the state_id parameter set to "CA" and the name parameter set to "San Francisco".
        It then asserts that the state_id attribute of the city object is equal to "CA" and the name attribute is equal to "San Francisco".

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """
        city = City(state_id="CA", name="San Francisco")
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")

    def test_city_inheritance(self):
        """
        Test case to verify the inheritance of the City class from the BaseModel class.

        Parameters:
            self (TestCase): The current test case.

        Returns:
            None
        """
        self.assertTrue(issubclass(City, BaseModel))
