#!/usr/bin/env python3

import unittest

from ...models.base_model import BaseModel
from ...models.review import Review


class TestReview(unittest.TestCase):
    def test_review_init(self):
        """
        Initialize a Review object with the given place_id, user_id, and text.

        Params:
            place_id (str): The ID of the place associated with the review.
            user_id (str): The ID of the user who created the review.
            text (str): The text content of the review.

        Returns:
            None
        """
        review = Review(place_id="123", user_id="456", text="example text")
        assert review.place_id == "123"
        assert review.user_id == "456"
        assert review.text == "example text"

    def test_review_inheritance(self):
        """
        Test the inheritance of the Review class from the BaseModel class.

        :param self: The current instance of the test case.
        :return: None
        """
        assert issubclass(Review, BaseModel)
