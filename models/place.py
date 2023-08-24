#!/usr/bin/python3
""" Place Module for HBNB project """
<<<<<<< HEAD
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
=======
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
>>>>>>> ffc82477a0325a5b407471c8b87f23afb4beef9b

if getenv("HBNB_TYPE_STORAGE") == "db":
  place_amenity = Table(
    "place_amenity", Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id"), primary_key=True),
    Column("amenity_id",
           String(60),
           ForeignKey("amenities.id"),
           primary_key=True))

<<<<<<< HEAD

class Place(BaseModel, Base):
  """ A place to stay """

  __tablename__ = "places"

  if getenv("HBNB_TYPE_STORAGE") == "db":
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", cascade="all, delete", backref="place")
    amenities = relationship("Amenity",
                             secondary=place_amenity,
                             backref="place_amenities",
                             viewonly=False)

  else:
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    @property
    def reviews(self):
      """ Returns the list of Review instances with
            place_id equals to the current Place.id """
      reviews = models.storage.all(Review)
      lst = []
      for review in reviews.values():
        if review.place_id == self.id:
          lst.append(review)
      return lst

    @property
    def amenities(self):
      """Amenities getter"""
      amenities = models.storage.all(Amenity)
      lst = []
      for amenity in amenities.values():
        if amenity.id in self.amenity_ids:
          lst.append(amenity)
      return lst

    @amenities.setter
    def amenities(self, obj):
      """Amenities setter"""
      if type(obj) == Amenity:
        self.amenity_ids.append(obj.id)
=======
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

>>>>>>> ffc82477a0325a5b407471c8b87f23afb4beef9b
