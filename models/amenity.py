#!/usr/bin/python3
<<<<<<< HEAD
""" State Module for HBNB project """
from models.state import State
=======
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
>>>>>>> ffc82477a0325a5b407471c8b87f23afb4beef9b

from os import getenv
from models.base_model import BaseModel, Base
# import models
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship

<<<<<<< HEAD

class Amenity(BaseModel, Base):
  """ The amenity class """

  __tablename__ = "amenities"

  if getenv('HBNB_TYPE_STORAGE') == "db":
    name = Column(String(128), nullable=False)
    # place_amenities = relationship("Place", secondary=place_amenity)

  else:
    name = ""
=======
class Amenity(BaseModel, Base):
  __tablename__ = 'amenities'

  name = Column(String(128), nullable=False)

  place_amenities = relationship("Place",
                                 secondary=place_amenity,
                                 back_populates="amenities")
>>>>>>> ffc82477a0325a5b407471c8b87f23afb4beef9b
