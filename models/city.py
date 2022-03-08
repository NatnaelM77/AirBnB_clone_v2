#!/usr/bin/python3

"""
Module city
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class City

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """
    state_id = ''
    name = ''
