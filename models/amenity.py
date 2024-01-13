#!/usr/bin/env python3

import models.base_model as BaseModel


class Amenity(BaseModel.BaseModel):
    """Class User that inherits from BaseModel"""

    name: str = ""

    def __init__(self, *args, **kwargs):
        """Initializes User"""
        super().__init__(*args, **kwargs)
