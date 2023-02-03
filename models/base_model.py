#!/usr/bin/python3
"""
The BaseModel class defines all common attributes/methods
for other classes
"""

from datetime import datetime
import uuid
from itertools import chain


class BaseModel:
    """Defines all common attributres/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initializing method"""
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()

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
