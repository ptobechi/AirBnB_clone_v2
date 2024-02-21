#!/usr/bin/python3
"""DB Storage engine"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    """DB Storage engine"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST", default="localhost")
        database = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        self.__engine = create_engine(
                f"mysql+mysqldb://{user}:{password}@{host}/{database}",
                pool_pre_ping=True
                )

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

        self.__session = scoped_session(
                sessionmaker(bind=self.__engine, expire_on_commit=False)
                )

        def all(self, cls=None):
            """Query on the current database session"""
        classes = [User, State, City, Amenity, Place, Review]
        if cls:
            classes = [cls]

        objects = {}
        for c in classes:
            query_result = self.__session.query(c).all()
            for obj in query_result:
                key = f"{obj.__class__.__name__}.{obj.id}"
                objects[key] = obj

        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
                sessionmaker(bind=self.__engine, expire_on_commit=False)
                )
        class DBStorage:
            """DB Storage engine"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST", default="localhost")
        database = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        self.__engine = create_engine(
                f"mysql+mysqldb://{user}:{password}@{host}/{database}",
                pool_pre_ping=True
                )

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

        self.__session = scoped_session(
                sessionmaker(bind=self.__engine, expire_on_commit=False)
                )

        def all(self, cls=None):
            """Query on the current database session"""
        classes = [User, State, City, Amenity, Place, Review]
        if cls:
            classes = [cls]

        objects = {}
        for c in classes:
            query_result = self.__session.query(c).all()
            for obj in query_result:
                key = f"{obj.__class__.__name__}.{obj.id}"
                objects[key] = obj

        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
                sessionmaker(bind=self.__engine, expire_on_commit=False)
                )
