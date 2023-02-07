#!/usr/bin/python3
"""New class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class that inherits from BaseModel class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
