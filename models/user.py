#!/usr/bin/python3

'''Class User inherits from BaseModel'''
import datetime
from models.base_model import BaseModel


class User(BaseModel):
    '''Class for define the plataform users'''

    email = ''
    password = ''
    first_name = ''
    last_name = ''
