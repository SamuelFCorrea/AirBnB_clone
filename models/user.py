#!/usr/bin/python3

'''Class User inherits from BaseModel'''
import datetime
from models.base_model import BaseModel
from models import storage


class User(BaseModel):
    '''Class for define the plataform users'''

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kargs):
        '''Initialize the class with the respective passed
values or the kargs ones'''

        if kargs is None or len(kargs) < 1:
            super().__init__()
        else:
            for key, value in kargs.items():
                if key == '__class__':
                    continue
                elif key in {'updated_at', 'created_at'}:
                    setattr(self, key, datetime.datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        storage.new(self)
