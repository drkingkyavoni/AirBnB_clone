#!/usr/bin/env python3

import unittest

import pytest

from ...models.base_model import BaseModel
from ...models.place import Place


class TestCity(unittest.TestCase):
    @pytest.fixture
    def place():
        """
        A fixture that returns an instance of the Place class.
        """
        place = Place()
        return place

    def test_place_instance(self, place):
        """
        Check if the given place is an instance of the Place class.

        Parameters:
            place (Place): The place object to be checked.

        Returns:
            None
        """
        assert isinstance(place, Place)

    def test_place_attributes(self, place):
        """
        Checks if the given place object has all the required attributes.

        Args:
            place (object): The place object to be checked.

        Returns:
            None
        """
        assert hasattr(place, "city_id")
        assert hasattr(place, "user_id")
        assert hasattr(place, "name")
        assert hasattr(place, "description")
        assert hasattr(place, "number_rooms")
        assert hasattr(place, "number_bathrooms")
        assert hasattr(place, "max_guest")
        assert hasattr(place, "price_by_night")
        assert hasattr(place, "latitude")
        assert hasattr(place, "longitude")
        assert hasattr(place, "amenity_ids")

    def test_place_attributes_default_values(self, place):
        """
        Test the default values of the attributes of a place object.

        Parameters:
            place (object): The place object to be tested.

        Returns:
            None
        """
        assert place.city_id == ""
        assert place.user_id == ""
        assert place.name == ""
        assert place.description == ""
        assert place.number_rooms == 0
        assert place.number_bathrooms == 0
        assert place.max_guest == 0
        assert place.price_by_night == 0
        assert place.latitude == 0.0
        assert place.longitude == 0.0
        assert place.amenity_ids == []

    def test_place_inherits_from_base_model(self, place):
        """
        Check if the given `place` object inherits from the `BaseModel` class.

        Parameters:
            place (BaseModel): The object to be checked.

        Returns:
            None
        """
        assert isinstance(place, BaseModel)
