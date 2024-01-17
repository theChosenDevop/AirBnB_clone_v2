#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from sqlalchemy import ForeignKey, Column, String
=======
from sqlalchemy import Column, String, ForeignKey
>>>>>>> ricki
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
<<<<<<< HEAD
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship('Place', cascade="all, delete, delete-orphan", backref="cities")
=======
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship('Place', cascade='all, delete', backref='cities')
>>>>>>> ricki
