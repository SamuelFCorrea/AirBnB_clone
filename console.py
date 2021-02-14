#!/usr/bin/python3
'''A command interpreter to administrate the program'''

import sys
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place 
from models.review import Review 


def clean(line):
    '''return the commands in a list'''
    commands = []
    tmp = line.rsplit(' ')
    for i in tmp:
        if i:
           commands.append(i)
    return commands

def create_class(name):
    '''Create a new class based in the name'''
    Classes = {'BaseModel': BaseModel, 'User': User,
               'State': State, 'City': City,
               'Amenity': Amenity, 'Place': Place,
               'Review': Review}

    if name in Classes:
        tmp = Classes[name]()
        print(tmp.id)
        tmp.save()


class HBNBCommand(cmd.Cmd):
    '''Command line to admin'''

    prompt = '(hbnh) '
    file = None
    Classes = ['BaseModel', 'User', 'State', 'City',
               'Amenity', 'Place', 'Review']


    def emptyline(self):
        '''Empty line management'''
        pass

    def do_EOF(self, line):
        '''Exit the cmd ctrl+D'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_create(self, line):
        '''Creates a new instance of BaseModel,
saves it (to the JSON file) and prints the id'''
        if not line:
            print('** class name missing **')
        elif line in self.Classes:
            create_class(line)
        else:
            print('** class doesn\'t exist **')

    def do_show(self, line):
        '''Prints the string representation of an
instance based on the class name and id'''
        commands = clean(line)
        if not len(commands):
            print('** class name missing **')
            return
        if commands[0] in self.Classes:
            if len(commands) >= 2:
                ret = storage.all().get('{}.{}'.format(commands[0], commands[1]))
                if ret:
                    print(ret)
                else:
                    print('** no instance found **')
            else:
                print('** instance id missing **')
        else:
            print('** class doesn\'t exist **')

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''
        commands = clean(line)
        if not len(commands):
            print('** class name missing **')
            return
        if commands[0] in self.Classes:
            if len(commands) >= 2:
                ret = storage.all().get('{}.{}'.format(commands[0], commands[1]))
                if ret:
                    storage.all().pop('{}.{}'.format(commands[0], commands[1]))
                    storage.save()
                else:
                     print('** no instance found **')
            else:
                print('** instance id missing **')
        else:
            print('** class doesn\'t exist **')

    def do_all(self, line):
        '''Prints the string representation of an instance
based on the class name and id'''
        ls = []
        if not line:
            for i in storage.all().values():
                ls.append(str(i))
        elif line in self.Classes:
            for i in storage.all().values():
                if i.to_dict()['__class__'] == line:
                    ls.append(str(i))
        else:
            print('** class doesn\'t exist **')
            return
        print(ls)

    def do_update(self, line):
        '''Updates an instance based on the class name and
id by adding or updating attribute'''
        command = clean(line)
        if not command:
            print('** class name missing **')
        if command[0] in self.Classes:
            if command[1]:
                item = storage.all().get('{}.{}'.format(command[0], command[1]))
                if item:
                    if command[2]:
                        if command[3]:
                            setattr(item, command[2], command[3])
                            item.save()
                        else:
                            print('** value missing **')
                    else:
                        print('** attribute name missing **')
                else:
                    print('** no instance found **')
            else:
                print('** instance id missing **')
        else:
            print('** class doesn\'t exist **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
