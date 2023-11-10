#!/usr/bin/python3
import uuid
import datetime


class BaseModel():
    """The class defines all common attributes/methods for other classes. """

    def __init__(self, *args, **kwargs):
        """__init__ method. """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
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
        return (f"[{self.__class__.__name__}], ({self.id}), {self.__dict__}")

    def save(self):
        """Updates the attribute updated_at with the current datetime. """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        dictionary = {}
        for key, value in self.__dict__.items():
            if key not in ('created_at', 'updated_at'):
                dictionary[key] = value
            else:
                dictionary[key] = datetime.datetime.isoformat(value)
        dictionary['__class__'] = self.__class__.__name__
        return (dictionary)
