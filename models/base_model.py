#!/usr/bin/python3
"""This module contains the ptototype for BaseModel Class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel of the AirBnB project"""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(
                        v, "%Y-%m-%dT%H:%M:%S.%f"
                        )
                elif k == "__class__":
                    continue
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """Prints [<class name>] (self.id) <self.__dict__>"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribut updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
        __dict__ of the instance"""
        d = self.__dict__.copy()
        d["updated_at"] = self.updated_at.isoformat()
        d["created_at"] = self.created_at.isoformat()
        d["__class__"] = self.__class__.__name__
        return d
