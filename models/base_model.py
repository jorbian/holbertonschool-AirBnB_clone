#!/usr/bin/python3
"""
The BaseModel class defines all common attributes/methods
for other classes
"""

from datetime import datetime
import uuid
from itertools import chain

import models


class BaseModel:
    """Class defines all common attributes/methods"""
    def __init__(self, *args, **kwargs):
        self.created_at = self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        if kwargs != {}:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
        else:
            models.storage.new(self)
        self.created_at = self.created_at \
            if type(self.created_at) is not str else\
            datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at \
            if type(self.updated_at) is not str else \
            datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """Creates str representation of object"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """Updates pub instance attr updated_at w/ current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dict containing all
        keys/values of __dict__ of the instance
        """
        return dict(
            chain.from_iterable(
                d.items() for d in
                (self.__dict__,
                    {
                        "updated_at": self.updated_at.isoformat(),
                        "created_at": self.created_at.isoformat(),
                        "__class__": self.__class__.__name__
                    })
            )
        )
