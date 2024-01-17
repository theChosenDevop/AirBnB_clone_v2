#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
<<<<<<< HEAD
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
=======
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
>>>>>>> ricki
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
<<<<<<< HEAD
    latitude = Column(Float, nullable=True)
    longitude = Column(Float,nullable=True)
    amenity_ids = []
    reviews = relationship('Review', cascade='all, delete, delete-orphan', backref='user')
=======
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship('Review', cascade='all, delete', backref='place')
>>>>>>> ricki
    amenities = relationship('Amenity',
                             secondary='place_amenity',
                             viewonly=False
                             )

<<<<<<< HEAD
    """
        move place_amenity table to resolve TypeError: Additional
        arguments should be named <dialectname>_<argument>, got 'nullable '
    """
=======

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                             'amenities.id'), primary_key=True, nullable=False)
                      )
>>>>>>> ricki
