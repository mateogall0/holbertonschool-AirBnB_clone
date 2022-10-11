#!/usr/bin/python3
"""File storage"""


import json


from models.base_model import BaseModel


class FileStorage:
    """File Storage class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects"""
        name = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[name] = obj.to_dict()

    def save(self):
        """Serializes"""
        d = {}
        for i in self.__objects:
            d[i] = self.__objects[i]
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(d, default=str))

    def reload(self):
        """Deserializes"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                for i, j in json.load(f).items():
                    FileStorage.__objects[i] = BaseModel(**j)
        except:
            pass
