""" Place Module for HBNB project """

from os import getenv
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

# association table probably:
if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table(
        'place_amenity', Base.metadata,
        Column('place_id', String(60),
               ForeignKey('places.id', onupdate='CASCADE',
                          ondelete='CASCADE'), primary_key=True),
        Column('amenity_id', String(60),
               ForeignKey('amenities.id',
                          onupdate='CASCADE',
                          ondelete='CASCADE'), primary_key=True),
        mysql_charset='latin1')


class Place(BaseModel, Base):
    '''place to stay:
    Representation of Place
    '''
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place')
        amenities = relationship('Amenity', secondary='place_amenity',
                                 backref='place_amenities',
                                 viewonly=False)
        # set default charset to match the db dump charset:
        __table_args__ = {'mysql_default_charset': 'latin1'}
    else:
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        '''initializes Place'''
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        @property
        def reviews(self):
            '''getter attribute reviews
            returns the list of Review instances
            with place_id equals to the current Place.id
            '''
            from models.review import Review
            review_list = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """getter attribute returns the list of Amenity instances"""
            from models.amenity import Amenity
            amenity_list = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list