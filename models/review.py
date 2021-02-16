#!/usr/bin/python3

'''Class Review inherit from BaseModel'''
import datetime
from models.base_model import BaseModel
from models import storage


class Review(BaseModel):
    '''A Review class to save a state information'''

    place_id = ''
    User_id = ''
    text = ''
