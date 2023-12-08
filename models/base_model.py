#usr/bin/python3
"""
module that contain base class of AirBnB clone console
"""

import uuid
from datetime import datetime

class BaseModel:
    """primary class for other classes"""
    def __init__(self):
        """initialization of public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """updates attribute updated_at with current datetime"""
        self.updated_at = datetime.now()

    def __str__(self):
        """returns a string from instances"""
        return "[{}] ({}) {}".\
        format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """returns a dictionary containing values of instances"""
        tw_dict = self.__dict__.copy()
        tw_dict['__class__'] = self.__class__.__name__
        tw_dict['created_at'] = self.created_at.isoformat()
        tw_dict['updated_at'] = self.updated_at.isoformat()
        return tw_dict
