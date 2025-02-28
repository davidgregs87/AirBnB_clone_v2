#!/usr/bin/python3
"""create class DBStorage"""
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


database = getenv("HBNB_MYSQL_DB")
user = getenv("HBNB_MYSQL_USER")
host = getenv("HBNB_MYSQL_HOST")
password = getenv("HBNB_MYSQL_PWD")
hbnb_env = getenv("HBNB_ENV")

classes = {"State": State, "City": City, "User": User,
           "Place": Place, "Review": Review, "Amenity": Amenity, "BaseModel": BaseModel}


class DBStorage:
    """class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """initialize instances"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format
                                      (user, password, host, database),
                                      pool_pre_ping=True)

        if hbnb_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return dictionary of instance attributes
        Args:
            cls (obj): memory address of class
        Returns:
            dictionary of objects
        """
        objects = {}
        if cls:
            if isinstance(cls, str) and cls in classes:
                cls = eval(cls)
            if cls in classes.values():
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = f'{type(obj).__name__}.{obj.id}'
                    objects[key] = obj
        else:
            for cls in classes.values():
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = f'{type(obj).__name__}.{obj.id}'
                    objects[key] = obj
        return objects
       

    def new(self, obj):
        """
        add object to current database session
        Args:
            obj (obj): an object
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        Args:
            obj (obj): an object
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database and the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close session"""
        self.__session.close()
