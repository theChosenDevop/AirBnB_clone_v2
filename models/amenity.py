#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column(
                          'place_id',
                          String(60),
                          ForeignKey('places.id'),
                          primary_key=True, nullable=False),
                      Column(
                          'amenity_id',
                          String(60),
                          ForeignKey('amenities.id'),
                          primary_key=True, nullable=False),
                          extend_existing=True
                      )


class Amenity(BaseModel, Base):
    """Defines the logic for the Amenity class"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary=place_amenity)

    """ moved Table up to resolve `TypeError: Additional arguments should
        be named <dialectname>_<argument>, got 'nullable'`
    """
