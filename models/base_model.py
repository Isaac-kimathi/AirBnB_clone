#!usr/bin/python3
"""
module that contain base class of AirBnB clone console
"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """primary class for other classes"""
    def __init__(self, *args, **kwargs): 
        
        """
        initialization of public instance attributes
        *args: list of arguments
        **kwargs: dict of keyword arguments
        """
        if kwargs:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """updates attribute updated_at with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing values of instances"""
        tw_dict = self.__dict__.copy()
        tw_dict['__class__'] = self.__class__.__name__
        tw_dict['created_at'] = self.created_at.isoformat()
        tw_dict['updated_at'] = self.updated_at.isoformat()
        return tw_dict

    def __str__(self):
        """returns a string from instances"""
        return "[{}] ({}) {}".\
                format(type(self).__name__, self.id, self.__dict__)
