#!/usr/bin/python3
""" Amenity Module for HBNB project """

from os import getenv
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Table, Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    '''class for amenity:
    like services eg WIFI
    '''
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        # set default charset to match the db dump charset:
        __table_args__ = {'mysql_default_charset': 'latin1'}
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
