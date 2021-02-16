#!/usr/bin/python3

'''Class State inherit from BaseModel'''
import datetime
from models.base_model import BaseModel


class City(BaseModel):
    '''A state class to save a state information'''

    state_id = ''
    name = ''
