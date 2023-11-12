#!/usr/bin/python3
"""
This init initializes a module to a package.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
