#!/usr/bin/python3
"""This module creates FileStorage instance"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
