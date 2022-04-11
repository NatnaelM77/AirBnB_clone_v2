#!/usr/bin/python3

"""
module FileStorage
"""

import os
import json
from models.base_model import BaseModel


class FileStorage:
    """Class FileStorage

       Attributes:
           __file_path (str): The name of the file
           __objects (dict): A dictionary of instantiated objects
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            cls_name = obj.__class__.__name__
            obj_id = obj.id
            self.__objects.update({
                f'{cls_name}.{obj_id}': obj
            })

    def save(self, cls=None):
        """Serializes __objects to the JSON file"""
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    cls_dict[k] = v
            return cls_dict
        return self.__objects

    def reload(self):
        """Deserialize the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                my_obj = {}
                dct = json.load(file)
                for key, value in dct.items():
                    cls_name = key.split('.')[0]
                    my_obj = eval(cls_name)(**value)
                    self.new(my_obj)

    def delete(self, obj=None):
        if obj is not None:
            del self.__objects[type(obj).__name__, obj.id]
