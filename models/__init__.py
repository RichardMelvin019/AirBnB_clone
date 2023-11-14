#!/usr/bin/python3
"""Initializes the package. """


from models.engine.file_storage import FileStorage

classes = {'BaseModel': 'BaseModel'}
storage = FileStorage()
storage.reload()
