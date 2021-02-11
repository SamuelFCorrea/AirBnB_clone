#!/usr/bin/python3
'''Defines the class FileStorage'''

import json


class FileStorage:
    '''Class to save and read the .json file'''

    __file_path = 'storage.json'
    __objects = {}

    def reload(self):
        '''Read the file and fill the __objects dictionary'''
        try:
            with open(self.__file_path, 'r') as f:
                tmp = json.loads(f.read())
                for key, value in tmp.items():
                    self.__objects.update({key: value})
        finally:
            return

    def all(self):
        '''Return all the objects'''
        return self.__objects

    def save(self):
        '''Saves the objects in the file'''
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(self.__objects))

    def new(self, obj):
        '''Create and actualize the objects'''
        self.__objects.update({'{}.{}'.format(obj['__class__'],
                              obj['id']): obj})
