#!/usr/bin/python3

'''
Class State inherit from BaseModel

    Attributes:

        state_id: it will be the State.id
        name: name

    Methods: inherits from BaseModel
'''

import datetime
from models.base_model import BaseModel


class City(BaseModel):
    '''
    A state class to save a state information
    '''

    state_id = ''
    name = ''
