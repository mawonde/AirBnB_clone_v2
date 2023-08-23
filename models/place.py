#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

# Import the SQLAlchemy Base and metadata objects
from models.base_model import Base

# Define the many-to-many table for place_amenity relationship
place_amenity = Table(
  'place_amenity', Base.metadata,
  Column('place_id',
         String(60),
         ForeignKey('places.id'),
         primary_key=True,
         nullable=False),
  Column('amenity_id',
         String(60),
         ForeignKey('amenities.id'),
         primary_key=True,
         nullable=False))


class Place(BaseModel):
  """ A place to stay """
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

  if getenv('HBNB_TYPE_STORAGE') == 'db':
    # Relationship for DBStorage
    reviews = relationship("Review",
                           backref="place",
                           cascade="all, delete-orphan")
    amenities = relationship("Amenity",
                             secondary=place_amenity,
                             viewonly=False)
  else:
    # Getter attribute for FileStorage
    @property
    def reviews(self):
      """Getter attribute for reviews"""
      from models import storage
      review_list = []
      for review in storage.all("Review").values():
        if review.place_id == self.id:
          review_list.append(review)
      return review_list

    # Getter and setter for amenities in FileStorage
    @property
    def amenities(self):
      """Getter attribute for amenities"""
      from models import storage
      amenity_list = []
      for amenity_id in self.amenity_ids:
        amenity = storage.get("Amenity", amenity_id)
        if amenity:
          amenity_list.append(amenity)
      return amenity_list

    @amenities.setter
    def amenities(self, amenity_obj):
      """Setter attribute for amenities"""
      if amenity_obj.__class__.__name__ == 'Amenity':
        self.amenity_ids.append(amenity_obj.id)

