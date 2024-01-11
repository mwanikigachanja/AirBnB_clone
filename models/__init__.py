#!/usr/bin/python3
<<<<<<< HEAD
"""__init__ magic method for models dir"""
from models.engine.file_storage import FileStorage


=======
"""Module for FileStorage autoinit."""

from models.engine.file_storage import FileStorage
>>>>>>> ae015a04f9f70f802bb1d1126321389dc4b24beb
storage = FileStorage()
storage.reload()
