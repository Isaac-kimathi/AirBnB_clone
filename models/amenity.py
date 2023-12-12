#!/usr/bin/python3
"""module innitializing the class amenity"""
from models.base_model import BaseMdel

class Amenity(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
