#!/usr/bin/python3
"""test for file storage"""
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """this will test the FileStorage"""

    def setUp(self):
        """Sets up test methods."""
        self.storage = FileStorage()

    def test_all(self):
        """tests if all works in File Storage"""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(objects, {})

    def test_new(self):
        """test when new is created"""
        model = BaseModel()
        self.storage.new(model)
        objects = self.storage.all()
        self.assertIn(f"{model.__class__.__name__}.{model.id}", objects)

    def test_save(self):
        """test when file is saved"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        with open("file.json", "r", encoding="utf-8") as f:
            saved_data = json.load(f)
        self.assertIn(f"{model.__class__.__name__}.{model.id}", saved_data)

    def test_reload(self):
        """test reload"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()

        # Clear existing objects and reload
        self.storage.__objects = {}
        self.storage.reload()
        objects = self.storage.all()
        self.assertIn(f"{model.__class__.__name__}.{model.id}", objects)


if __name__ == "__main__":
    unittest.main()
