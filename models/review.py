#!/usr/bin/python3
""" Review module for the HBNB project """
<<<<<<< HEAD
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
  """ Review classto store review information """

  __tablename__ = "reviews"

  if getenv("HBNB_TYPE_STORAGE") == "db":
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)

  else:
    place_id = ""
    user_id = ""
    text = ""
=======
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel):
  """ Review class to store review information """
  __tablename__ = 'reviews'  # Table name

  text = Column(String(1024), nullable=False)  # Column for review text

  place_id = Column(String(60), ForeignKey('places.id'),
                    nullable=False)  # ForeignKey for place_id
  place = relationship(
    "Place", back_populates="reviews")  # Relationship with Place model

  user_id = Column(String(60), ForeignKey('users.id'),
                   nullable=False)  # ForeignKey for user_id

>>>>>>> ffc82477a0325a5b407471c8b87f23afb4beef9b
