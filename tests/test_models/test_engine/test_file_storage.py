#!/usr/bin/python3
'''Test to the BaseModel class'''

from models import storage
import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    '''Test cases to the BaseModel class'''

    def test_class_documentation(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("models").storage.__doc__, None)

    def test_reload_documentation(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("models").storage.reload.
                            __doc__, None)

    def test_all_documentation(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("models").storage.all.__doc__, None)

    def test_new_documentation(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("models").storage.
                            new.__doc__, None)

    def test_class_len_doc(self):
        '''Test the documentation'''
        self.assertGreater(len(__import__("models").storage.__doc__), 40)

    def test_reload_len_doc(self):
        '''Test the documentation'''
        self.assertGreater(len(__import__("models").storage.reload.
                               __doc__), 40)

    def test_new_len_doc(self):
        '''Test the documentation'''
        self.assertGreater(len(__import__("models").storage.
                               new.__doc__), 40)
