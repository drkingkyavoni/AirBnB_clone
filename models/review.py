#!/usr/bin/env python3

import models.base_model as BaseModel


class Review(BaseModel.BaseModel):
    """Class User that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes User"""
        super().__init__(*args, **kwargs)
