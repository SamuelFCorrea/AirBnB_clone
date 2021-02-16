#!/usr/bin/python3
'''Test to the BaseModel class'''

from models.base_model import BaseModel
import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    '''Test cases to the BaseModel class'''

    def test_id(self):
        '''Test the correct id assignment'''
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)

    def test_datastored(self):
        '''Test the data type stored in the object'''
        test2 = BaseModel()
        self.assertEqual(type(test2.id), str)
        self.assertEqual(type(test2.created_at), datetime.datetime)
        self.assertEqual(type(test2.updated_at), datetime.datetime)

    def test_to_dic(self):
        '''Test the correct output of the 'to_dic' method'''
        test3 = BaseModel()
        dic = test3.to_dict()
        self.assertEqual(len(dic), 4)
        test3.name = 'John'
        dic = test3.to_dict()
        self.assertEqual(len(dic), 5)
        test3.last_name = 'Wick'
        dic = test3.to_dict()
        self.assertEqual(len(dic), 6)
        for i in dic.values():
            self.assertEqual(type(i), str)

    def test_from_dic(self):
        '''Test the generation of a object from a dic'''
        a = BaseModel()
        dic = a.to_dict()
        b = BaseModel(dic)
        self.assertNotEqual(a, b)
        self.assertEqual(type(b.created_at), datetime.datetime)
        self.assertEqual(type(b.updated_at), datetime.datetime)

    def test_file_documentation(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("models").base_model.__doc__, None)

    def test_class_documentation(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("models").base_model.BaseModel.__doc__, None)

    def test_init_documentation(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("models").base_model.BaseModel.__init__.__doc__, None)

    def test_str_documentation(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("models").base_model.BaseModel.__str__.__doc__, None)

    def test_save_method_doc(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("models").base_model.BaseModel.save.__doc__, None)

    def test_to_dict_method_doc(self):
        '''Test the documentation'''
        self.assertNotEqual(__import__("models").base_model.BaseModel.to_dict.__doc__, None)

    def test_file_len_doc(self):
        '''Test the documentation'''
        self.assertGreater(len(__import__("models").base_model.__doc__), 40)

    def test_class_len_doc(self):
        '''Test the documentation'''
        self.assertGreater(len(__import__("models").base_model.BaseModel.__doc__), 40)

    def test_init_len_doc(self):
        '''Test the documentation'''
        self.assertGreater(len(__import__("models").base_model.BaseModel.__init__.__doc__), 40)

    def test_str_len_doc(self):
        '''Test the documentation'''
        self.assertGreater(len(__import__("models").base_model.BaseModel.__str__.__doc__), 40)

    def test_save_len_doc(self):
        '''Test the documentation'''
        self.assertGreater(len(__import__("models").base_model.BaseModel.save.__doc__), 40)

    def test_to_dict_len_doc(self):
        '''Test the documentation'''
        self.assertGreater(len(__import__("models").base_model.BaseModel.to_dict.__doc__), 40)
