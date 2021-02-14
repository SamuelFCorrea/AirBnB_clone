#!/usr/bin/python3
'''Defines the class FileStorage'''

import json

def load_class(dic):
    '''Load the class in the file'''
    from models.base_model import BaseModel
    from models.user import User
    from models.state import State
    from models.city import City
    from models.amenity import Amenity
    from models.place import Place
    from models.review import Review

    Classes = {'BaseModel': BaseModel, 'User': User,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Place': Place, 'Review': Review}

    for i in Classes.keys():
        if i == dic['__class__']:
            Classes[i](**dic)


class FileStorage:
    '''Class to save and read the .json file'''

    __file_path = 'storage.json'
    __objects = {}

    def reload(self):
        '''Read the file and fill the __objects dictionary'''
        try:
            with open(self.__file_path, 'r') as f:
                 loads = json.loads(f.read())
                 for i in loads.values():
                      load_class(i)
        finally:
            return

    def all(self):
        '''Return all the objects'''
        return self.__objects

    def save(self):
        '''Saves the objects in the file'''
        dic = {}
        with open(self.__file_path, 'w') as f:
            for item, val in self.__objects.items():
                dic.update({item: val.to_dict()})
            f.write(json.dumps(dic))

    def new(self, obj):
        '''Create and actualize the objects'''
        self.__objects.update({'{}.{}'.format(obj.__class__.__name__, obj.id): obj})
