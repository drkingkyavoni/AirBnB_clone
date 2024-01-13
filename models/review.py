#!/usr/bin/env python3

import models.base_model as BaseModel


class Review(BaseModel.BaseModel):
    """Class User that inherits from BaseModel"""

    place_id: str = ""
    user_id: str = ""
    text: str = ""

    def __init__(self, *args, **kwargs):
        """Initializes User"""
        super().__init__(*args, **kwargs)
