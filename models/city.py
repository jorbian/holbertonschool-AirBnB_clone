#!/usr/bin/python3
"""New class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class that inherits from BaseModel class"""
    state_id = ""
    name = ""
