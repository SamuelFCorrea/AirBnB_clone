#!/usr/bin/python3

'''Class State inherit from BaseModel'''
import datetime
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''A Amenity class to save a state information'''

    name = ''
