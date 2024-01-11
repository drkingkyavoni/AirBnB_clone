#!/usr/bin/env python3
import datetime
import uuid

import models


class BaseModel:
    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes the object after it has been created. Sets the 'created_at'
        and 'updated_at' attributes to the current datetime.

        Parameters:
            self: The object instance.

        Returns:
            None
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if not kwargs:
            self.name = ""
            self.my_number = 0
            models.storage.new(self)
        else:
            self.__dict__.update(kwargs)
            if "created_at" in kwargs:
                self.created_at = datetime.datetime.fromisoformat(kwargs["created_at"])
            if "updated_at" in kwargs:
                self.updated_at = datetime.datetime.fromisoformat(kwargs["updated_at"])

    def __str__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: The string representation of the object.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self) -> None:
        """
        Updates the `updated_at` attribute of the object with the current datetime.

        Parameters:
            None

        Returns:
            None
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the current object.

        Returns:
            dict: A dictionary representation of the current object.
                The dictionary includes the following key-value pairs:
                - "my_number" (int): The value of my_number attribute.
                - "name" (str): The value of name attribute.
                - "class_name" (str): The name of the class.
                - "updated_at" (str): The last update date and time of the object in ISO format.
                - "id" (int): The id of the object.
                - "created_at" (str): The creation date and time of the object in ISO format.
        """
        return {
            "my_number": self.my_number,
            "name": self.name,
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.isoformat(),
            "id": self.id,
            "created_at": self.created_at.isoformat(),
        }
