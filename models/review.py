#!/usr/bin/python3
""" Review module for the HBNB project """
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

