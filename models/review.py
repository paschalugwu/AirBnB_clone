#!/usr/bin/python3
"""The Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review"""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
