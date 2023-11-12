#!/usr/bin/python3
"""
This is the File database .
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

My_classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}



class FileStorage():
    """ This code is for serialization and deserialization """

  
    __file_path = "file.json"
    
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return (FileStorage.__objects)

    def new(self, obj):
        """This is the object with  a className."""
        if obj is not None:
            lop = obj.__class__.__name__ + "." + obj.id
            self.__objects[lop] = obj

    def save(self):
        """This serializes the python object int a JSON format"""
        My_dict = {}
        for lop in self.__objects:
            My_dict[lop] = self.__objects[lop].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(My_dict, file)


    
       
    def reload(self):
        """This code deserializes the JSON format to a python object."""
        try:
            with open(self.__file_path, 'r') as file:
                my_object_all = json.load(file)
            for lop in my_object_all:
                self.__objects[lop] = My_classes[my_object_all[lop]["__class__"]](**my_object_all[lop])
        except:
            pass
