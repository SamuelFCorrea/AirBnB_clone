#!/usr/bin/python3

'''Class State inherit from BaseModel'''
import datetime
from models.base_model import BaseModel
from models import storage


class State(BaseModel):
    '''A state class to save a state information'''

    name = ''
