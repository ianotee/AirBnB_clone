#!/usr/bin/python3
"""
This is the Users  class Models.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This is the Users class.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
