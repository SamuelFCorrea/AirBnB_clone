#!/usr/bin/python3
'''Defines the class FileStorage.

At the start of the program a new object called 'storage'
will be created and with it all the current class operation
will executed

For more info read the fuction documentation.
'''

import json
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


class FileStorage:
    '''
Class to save and read the .json file

    File name at root directory 'file.json'.
    No need to worrie about the .json extention the program still working
    without it.

    If the file doesn't exist it will be created

    Atributtes:

        __file_path: path to the file
        __objects: will almacenate all the objects

    Methods:
        reload(): it will be called only one time to read the
                  '__file_path' file
                  and load all the classes
        all(): return the '__objects' variable
        save(): saves the '__objects' content in the '__file_path' file
    '''

    __file_path = 'file.json'
    __objects = {}

    def reload(self):
        '''Read the file and fill the __objects dictionary'''
        try:
            with open(self.__file_path, 'r') as f:
                loads = json.loads(f.read())
                for value in loads.values():
                    if value['__class__'] in Classes:
                        self.new(Classes[value['__class__']](**value))
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
        '''
Create and actualize the objects and add a key

Format: <class name>.<object id>: <dict>
        '''
        if obj:
            self.__objects.update({'{}.{}'.format(obj.__class__.__name__,
                                   obj.id): obj})
