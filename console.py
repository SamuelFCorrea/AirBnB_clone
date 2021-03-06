#!/usr/bin/python3
'''
A command interpreter to administrate the program.

Works in interactive mode:

    $ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit

    (hbnb)
    (hbnb)
    (hbnb) quit
    $

And in non-interactive mode:

    $ echo "help" | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb)
    $
'''

import sys
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


def clean(line):
    '''Return the commands in a list to facilitate the command read'''
    commands = []
    tmp = line.rsplit(' ')
    for i in tmp:
        if i:
            commands.append(i)
    return commands


Classes = {'BaseModel': BaseModel, 'User': User,
           'State': State, 'City': City,
           'Amenity': Amenity, 'Place': Place,
           'Review': Review}


class HBNBCommand(cmd.Cmd):
    '''Command line to administrate the creation, update and remove the objects

    Commands:

        create: Creates a new instance, saves it
                (to the JSON file) and prints the id.
                Ex: $ create BaseModel

        show: Prints the string representation of an instance based
              on the class name and id.
              Ex: $ show BaseModel 1234-1234-1234

        destroy: Deletes an instance based on the class name and id
                 (save the change into the JSON file). Ex:
                 destroy BaseModel 1234-1234-1234

        all: Prints all string representation of all instances based or not
             on the class name.
             Ex: $ all BaseModel or $ all

        update: Updates an instance based on the class name and id by adding or
                updating attribute (save the change into the JSON file).
                Ex: $ update BaseModel 14-234 email "aibnb@holbertonschool.com"

    For more info type 'help <Command>'
    '''

    prompt = '(hbnb) '

    def emptyline(self):
        '''
        Empty line management
        By default an empty line execute the last command now do nothing
        '''
        pass

    def do_EOF(self, line):
        '''
        Exit the cmd and print a new line when the imput is EOF
        '''
        print('')
        return True

    def do_quit(self, line):
        '''
        Quit command to exit the program normally
        '''
        return True

    def do_create(self, line):
        '''
        Creates a new instance of a class, saves it (to the JSON file)
        and prints the id.

        Usage: $ create <class name>
        '''
        if not line:
            print('** class name missing **')
        elif line in Classes.keys():
            tmp = Classes[line]()
            print(tmp.id)
            tmp.save()
        else:
            print('** class doesn\'t exist **')

    def do_show(self, line):
        '''
        Prints the string representation of an instance based on the
        class name and id.

        Usage: $ show <class name> <instance id>
        '''
        commands = clean(line)
        if not len(commands):
            print('** class name missing **')
            return
        if commands[0] in Classes.keys():
            if len(commands) >= 2:
                ret = storage.all().get('{}.{}'.format(commands[0],
                                                       commands[1]))
                if ret:
                    print(ret)
                else:
                    print('** no instance found **')
            else:
                print('** instance id missing **')
        else:
            print('** class doesn\'t exist **')

    def do_destroy(self, line):
        '''
        Deletes an instance based on the class name and id

        Usage: $ destroy <class name> <instance id>
        '''
        commands = clean(line)
        if not len(commands):
            print('** class name missing **')
            return
        if commands[0] in Classes.keys():
            if len(commands) >= 2:
                ret = storage.all().get('{}.{}'.format(commands[0],
                                                       commands[1]))
                if ret:
                    storage.all().pop('{}.{}'.format(commands[0],
                                                     commands[1]))
                    storage.save()
                else:
                    print('** no instance found **')
            else:
                print('** instance id missing **')
        else:
            print('** class doesn\'t exist **')

    def do_all(self, line):
        '''
        Prints all string representation of all instances based or not
        on the class name.

        Usage: $ all
               $ all <class name>
        '''
        ls = []
        if not line:
            for i in storage.all().values():
                ls.append(str(i))
        elif line in Classes.keys():
            for i in storage.all().values():
                if i.to_dict()['__class__'] == line:
                    ls.append(str(i))
        else:
            print('** class doesn\'t exist **')
            return
        print(ls)

    def do_update(self, line):
        '''
        Updates an instance based on the class name and
        id by adding or updating attribute

        Usage: $ update <class name> <id> <attribute name> <attribute value>
        $ update <class name> <id> <attribute name> "<attribute value>"
        '''
        commands = clean(line)
        if not len(commands):
            print('** class name missing **')
            return
        if commands[0] in Classes.keys():
            if len(commands) >= 2:
                item = storage.all().get('{}.{}'.format(commands[0],
                                                        commands[1]))
                if item:
                    if len(commands) >= 3:
                        if len(commands) >= 4:
                            try:
                                rt = float(commands[3])
                                if int(rt) == rt:
                                    rt = int(rt)
                            except:
                                rt = commands[3]
                            setattr(item, commands[2], rt)
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

    def do_count(self, line):
        count = 0
        if line in Classes.keys():
            for obj in storage.all().values():
                if line == obj.__class__.__name__:
                    count += 1
        print(count)

    def precmd(self, line):
        if line and line.rsplit('.')[0] in Classes.keys():
            end = ''
            tmp = line.rsplit('.')
            if len(tmp) < 2:
                return line
            cls = tmp[0]
            com = tmp[1].rsplit('(')[0]
            end = com + ' ' + cls
            if line.rsplit('(')[1].rsplit(')')[0] == '':
                return end
            opt = line.rsplit('(')[1].rsplit(')')[0].rsplit(',')
            for i in opt:
                end = end + ' ' + i
            return end
        return line


if __name__ == '__main__':
    import sys
    HBNBCommand().cmdloop()
