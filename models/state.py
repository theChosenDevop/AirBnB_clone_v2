#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
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
