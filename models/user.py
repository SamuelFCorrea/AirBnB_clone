#!/usr/bin/python3

'''
Class User inherits from BaseModel

    Atributes:

        email: user email
        password: user password
        first_name: user first name
        last_name: user last name

    Methods: inherits
'''

import datetime
from models.base_model import BaseModel


class User(BaseModel):
    '''
Class to define the plataform users and save their info
    '''

    email = ''
    password = ''
    first_name = ''
    last_name = ''
