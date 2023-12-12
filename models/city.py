#!/usr/bin/python3
"""module creating class city"""
from models.base_model import BaseModel

class City(BaseModel):
    """manages city objects"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
