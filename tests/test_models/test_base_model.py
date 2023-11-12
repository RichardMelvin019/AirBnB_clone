#!/usr/bin/python3
"""Unittest BaseModel. """

import unittest
import inspect
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test for class BaseModel"""

    def setUp(self):
        """setup. """
        self.model = BaseModel()

    def test_class_docstring(self):
        """checks if class has docstring. """
        msg = "BaseModel class does not have docstring"
        self.assertIsNotNone(BaseModel.__doc__, msg)

    def test_method_docstring(self):
        """checks if class methods have docstring. """
        methods = inspect.grtmembers(BasModel, predicate=inspect.ismethod)
        msg = "method should have a dostring"
        for name, method in methods:
            with self.subTest(method=name):
                self.assertIsNotNone(method.__doc__, f"{name} {msg}")

    def test_module_docstring(self):
        """check if modules have docstring. """
        msg = "modules does not have docstring"
        self.assertIsNotNone(models.base_model.__doc__, msg)

    def test__init__(self):
        """test if an obj is a type BaseModel. """
        self.assertIsInstance(self.model, BaseModel)

    def test_id(self):
        """test that id is Unique. """
        objectid = BaseModel()
        objectid_2 = BaseModel()
        self.assertNotEqual(objectid.id, objectid_2.id)

    def test_str(self):
        """check if the output of stris in
        the specified format."""
        object_str = "[BaseModel], ({0}), {1}".format(
                self.model.id, self.model.__dict__
                )
        self.assertEqual(str(self.model), object_str)

    def tets_save(self):
        "check is date updated when save"
        first_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(first_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """check if to_dict returns a dictionary, if add a class
        key with class name of the object and if updated_at and
        created_at are converted to string object in ISO format."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)


if __name__ == "__main__":
    unittest.main()
