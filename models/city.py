#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
<<<<<<< HEAD

=======
>>>>>>> ffc82477a0325a5b407471c8b87f23afb4beef9b

class City(BaseModel, Base):
  """ The city class, contains state ID and name """

<<<<<<< HEAD
  __tablename__ = "cities"

  if getenv('HBNB_TYPE_STORAGE') == "db":
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", cascade="all, delete", backref="cities")

  else:
    state_id = ""
    name = ""
=======
class City(BaseModel):
  """ The city class, contains state ID and name """
  __tablename__ = 'cities'
  name = Column(String(128), nullable=False)
  state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

  # Define the relationship between City and Place
  places = relationship('Place',
                        backref='cities',
                        cascade='all, delete-orphan')
>>>>>>> ffc82477a0325a5b407471c8b87f23afb4beef9b
