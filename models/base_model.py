#!/usr/bin/python3
'''Defines the 'BaseModel' class'''

from models import storage
import datetime
import uuid


class BaseModel:
    '''Class to assing id and avoid any redundancy in the code'''

    def __init__(self, *args, **kargs):
        '''Initialize the class with the default values or the kargs ones'''

        if kargs is None or len(kargs) < 1:
            self.id = str(uuid.uuid4())
            self.my_number = 0
            self.name = ''
            self.updated_at = datetime.datetime.now()
            self.created_at = datetime.datetime.now()
        elif kargs:
            for key, value in kargs.items():
                if key == '__class__':
                    continue
                elif key in {'updated_at', 'created_at'}:
                    exec('self.{} = datetime.datetime.\
                            fromisoformat("{}")'.format(key, value))
                elif key == 'my_number':
                    exec('self.{} = {}'.format(key, value))
                else:
                    exec('self.{} = "{}"'.format(key, value))

    def __str__(self) -> str:
        '''Return the info of the object in a string'''
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''Like touch command only update the object'''
        self.updated_at = datetime.datetime.now()
        storage.new(self.to_dict())
        storage.save()

    def to_dict(self):
        '''Return a dictionary with all the object information,
        the dates change to str type'''
        a = {}
        for key, arg in self.__dict__.items():
            if key in {'updated_at', 'created_at'}:
                a.update({key: arg.isoformat()})
            elif key == 'name':
                a.update({key: arg})
                a.update({'__class__': self.__class__.__name__})
            else:
                a.update({key: arg})
        return a
