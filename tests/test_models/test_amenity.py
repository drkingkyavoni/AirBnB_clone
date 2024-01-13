import unittest

from ...models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_init(self):
        """
        Test the initialization of the Amenity class.

        Parameters:
            self (TestCase): The current test case.

        Returns:
            None
        """
        amenity = Amenity(name="Test Name")
        self.assertEqual(amenity.name, "Test Name")
