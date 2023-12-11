#!/usr/bin/bash
"""module for fileStorage class."""
import json

class FileStorage:
    """class serializes and deserializes instances a Json file & viceversa"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """set in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        dicts_obj = {}
        for key, obj in self.__objects.items():
            dicts_obj[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(dicts_obj, file)

    def classes(self):
        """Returns a dic of valid classes and their references"""
        from models.base_model import BaseModel

        classes = { "BaseModel": BaseModel}
        return classes

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                dict_obj = json.load(file)
                dict_obj = {k: self.classes()[v["__class__"]](**v)
                            for k, v in dict_obj.items()}
                self.__objects = dict_obj
        except FileNotFoundError:
            dict_obj = {}
        except json.JSONDecodeError:
            dict_obj = {}
