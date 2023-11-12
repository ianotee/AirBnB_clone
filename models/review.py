#!/usr/bin/python3
"""
This is  Review  class Models.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This is the Review  attribute 
    """
    place_id = ""
    user_id = ""
    text = ""
