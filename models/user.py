#!/usr/bin/env python3

import models.base_model as BaseModel


class User(BaseModel.BaseModel):
    """Class User that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes User"""
        super().__init__(*args, **kwargs)
