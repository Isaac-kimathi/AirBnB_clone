#!/usr/bin/bash
"""module for fileStorage class."""
import json
import os

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
        dict_obj = {}
        for key, obj in self.__objects.item():
            dict_obj[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, 'r', encoding="utf-8") as file:
            ld_objs = json.load(file)

        for key, dict_obj in ld_objs.items():
            class_name, obj_id = key.split('.')
            module = FileStorage
            class_ = getattr(module, class_name)
            obj = class_(**obj_dict)
            self.__objects[key] = obj
