#!/usr/bin/python3
"""Base Model"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """Base class for the console clone"""
    def __init__(self, *args, **kwargs):
        if kwargs:

            if key, value in kwargs:

            uuid_string = str(uuid.uuid4())
