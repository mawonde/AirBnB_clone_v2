from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place

from os import getenv


class DBStorage:
  """Create table for storage """
  __engine = None
  __session = None

  def __init__(self):
    """Create the engine and session upon instantiation."""
    # Configure MySQL connection using environment variables
    user = getenv('HBNB_MYSQL_USER')
    password = getenv('HBNB_MYSQL_PWD')
    host = getenv('HBNB_MYSQL_HOST', 'localhost')
    database = getenv('HBNB_MYSQL_DB')

    # Create engine with pool_pre_ping
    self.__engine = create_engine(
      f'mysql+mysqldb://{user}:{password}@{host}/{database}',
      pool_pre_ping=True)

    # Drop tables if environment is 'test'
    if getenv('HBNB_ENV') == 'test':
      Base.metadata.drop_all(self.__engine)

    # Create session using scoped_session
    self.__session = scoped_session(
      sessionmaker(bind=self.__engine, expire_on_commit=False))

  def all(self, cls=None):
    """Query all objects based on class name."""
    obj_dict = {}
    if cls:
      objects = self.__session.query(cls).all()
    else:
      classes = [User, State, City, Amenity, Place,
                 Review]  # Import the necessary classes
      objects = []
      for cls in classes:
        objects.extend(self.__session.query(cls).all())

    for obj in objects:
      key = f'{obj.__class__.__name__}.{obj.id}'
      obj_dict[key] = obj
    return obj_dict

  def new(self, obj):
    """Add object to the current session."""
    self.__session.add(obj)

  def save(self):
    """Commit all changes of the current session."""
    self.__session.commit()

  def delete(self, obj=None):
    """Delete object from the current session."""
    if obj:
      self.__session.delete(obj)

  def reload(self):
    """Create all tables and initialize session."""
    Base.metadata.create_all(self.__engine)
    self.__session = scoped_session(
      sessionmaker(bind=self.__engine, expire_on_commit=False))

