#!/usr/bin/python3
"""module innitializing class Review"""
from models.base_model import BaseModel

class Review:
    """class to handle review objecs"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user.id = ""
        self.text = ""
