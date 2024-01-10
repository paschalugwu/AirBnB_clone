#!/usr/bin/python3
"""The User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent an AirBnB User."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
