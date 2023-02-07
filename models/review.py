#!/usr/bin/python3
"""New class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class that inherits from BaseModel class"""
    place_id = ""
    user_id = ""
    text = ""
