#!/usr/bin/python3
"""BaseModel script. """
import uuid
import datetime
import models


class BaseModel():
    """The class defines all common attributes/methods for other classes. """

    def __init__(self, *args, **kwargs):
        """__init__ method. """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                else:
                    if key in ('created_at', 'updated_at'):
                        self.__dict__[key] = datetime.datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

    def __str__(self):
        """Prints print: [<class name>] (<self.id>) <self.__dict__> """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        """Updates the attribute updated_at with the current datetime. """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary['__class__'] = self.__class__.__name__
        return dictionary
