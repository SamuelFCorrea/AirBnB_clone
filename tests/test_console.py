#!/usr/bin/python3
'''Test to the BaseModel class'''

from console import HBNBCommand
import datetime
import unittest


class TestCommand(unittest.TestCase):
    '''Test cases to the BaseModel class'''

    def test_file_documentation(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("console").__doc__, None)

    def test_class_documentation(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("console").HBNBCommand.
                            __doc__, None)

    def test_empty_documentation(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("console").HBNBCommand.
                            emptyline.__doc__, None)

    def test_eof_documentation(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("console").HBNBCommand.
                            do_EOF.__doc__, None)

    def test_quit_documentation(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("console").HBNBCommand
                            .do_quit.__doc__, None)

    def test_create_documentation(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("console").HBNBCommand
                            .do_create.__doc__, None)

    def test_show_documentation(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("console").HBNBCommand
                            .do_show.__doc__, None)

    def test_destroy_documentation(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("console").HBNBCommand
                            .do_destroy.__doc__, None)

    def test_all_documentation(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("console").HBNBCommand
                            .do_all.__doc__, None)

    def test_update_documentation(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("console").HBNBCommand
                            .do_update.__doc__, None)

    def test_file_len_doc(self):
        '''Test the documentation'''
        self.assertGreater(len(__import__("console").__doc__), 40)

    def test_class_len_doc(self):
        '''Test the documentation'''
        self.assertGreater(len(__import__("console").HBNBCommand.__doc__), 40)

    def test_emptyline_len_doc(self):
        '''Test the documentation'''
        self.assertGreater(len(__import__("console").HBNBCommand.
                           emptyline.__doc__), 40)

    def test_eof_len_doc(self):
        '''Test the documentation'''
        self.assertGreater(len(__import__("console").HBNBCommand.
                           do_EOF.__doc__), 40)

    def test_quit_len_doc(self):
        '''Test the documentation'''
        self.assertGreater(len(__import__("console").HBNBCommand.
                           do_quit.__doc__), 40)

    def test_create_len_doc(self):
        '''Test the documentation'''
        self.assertGreater(len(__import__("console").HBNBCommand.
                           do_create.__doc__), 40)

    def test_show_len_doc(self):
        '''Test the documentation'''
        self.assertGreater(len(__import__("console").HBNBCommand.
                           do_show.__doc__), 40)

    def test_destroy_len_doc(self):
        '''Test the documentation'''
        self.assertGreater(len(__import__("console").HBNBCommand.
                           do_destroy.__doc__), 40)

    def test_update_len_doc(self):
        '''Test the documentation'''
        self.assertGreater(len(__import__("console").HBNBCommand.
                           do_update.__doc__), 40)
