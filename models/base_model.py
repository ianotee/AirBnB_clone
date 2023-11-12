#!/usr/bin/python3
"""
This is the Parent models that will be inherited.
"""

from datetime import datetime
import models
import uuid





class BaseModel:
    """This is the Parent Model that will be inherited."""

    def __init__(self, *args, **kwargs):
        """The init will convert the base Model into a package."""
        if kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

            for lop, vulu in kwargs.items():
                if lop != "__class__":
                    setattr(self, lop, vulu)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()


    def __str__(self):
        """This is the string of BaseModel"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def __str__(self):
        """
        This is the string of The BaseModel.
        """
        string_name = type(self).__name__
        string_id = self.id
        string_dict = str(self.__dict__)
        return "[{}] ({}) {}".format(string_name, string_id, string_dict)
    


    def save(self):
        """This code will update the attributes"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """This function will return a new dictionary"""
        my_Object = self.__dict__.copy()
        if "created_at" in  my_Object:
            my_Object["created_at"] = my_Object["created_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        if "updated_at" in my_Object:
            my_Object["updated_at"] = my_Object["updated_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_Object["__class__"] = self.__class__.__name__
        return my_Object
