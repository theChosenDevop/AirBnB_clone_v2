#!/usr/bin/python3
""" State Module for HBNB project """
<<<<<<< HEAD
import models
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.city import City
=======
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
>>>>>>> ricki


class State(BaseModel, Base):
    """ State class """
<<<<<<< HEAD
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    #for DBStorage
    cities = relationship("City", cascade="all, delete, delete-orphan", backref="state")

    #for FileStorage
    @property
    def cities(self):
        """ returns the list of City instances with state_id equals to the current State.id """
        city_instances = models.storage.all("City")
        return [city for city in city_instances.values() if city.state_id == self.id]
=======
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')
>>>>>>> ricki
