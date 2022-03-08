#!/usr/bin/python3

"""
module BaseModel
"""

import uuid
import models
from datetime import datetime


class BaseModel:
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel

        Args:
            *args (any): Unused
            **kwargs (dict): Key/value pairs of attributes.
        """
        time_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(value,
                                                             time_format))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """Returns printable string representation"""
        cls_name = self.__class__.__name__
        str = f'[{cls_name}] ({self.id}) {self.__dict__}'
        return str

    def save(self):
        """Updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of
        the instance."""
        dct = self.__dict__.copy()
        dct.update({
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        })
        return dct
