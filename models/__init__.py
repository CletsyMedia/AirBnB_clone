#!/usr/bin/python3
"""Initialize the models package and create a FileStorage instance."""
from models.engine.file_storage import FileStorage

# Create a FileStorage instance to manage object serialization/deserialization
storage = FileStorage()

# Reload previously stored objects from the serialized file (if any)
storage.reload()
