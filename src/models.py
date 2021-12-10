import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    homeplanet_id = Column(String(250))
    name = Column(String(250))
    birth_year = Column(Integer, primary_key=True)
    eye_color = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    height = Column(Integer, primary_key=True)
    mass = Column(Integer, primary_key=True)
    skin_color = Column(Integer, primary_key=True)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(Integer, primary_key=True)
    climate = Column(String(250))
    diameter = Column(Integer, primary_key=True)
    gravity = Column(String(250))
    rotation_period = Column(Integer, primary_key=True)
    surface_water = Column(Integer, primary_key=True)
    terrain = Column(String(250))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    cargo_capacity = Column(Integer, primary_key=True)
    consumables = Column(String(250))
    cost_in_credits = Column(Integer, primary_key=True)
    crew = Column(Integer, primary_key=True)
    length = Column(Integer, primary_key=True)
    manufacturer = Column(String(250))
    passengers = Column(Integer, primary_key=True)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250))

class Drives(Base):
    __tablename__ = 'drives'
    people_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), primary_key=True)
    



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')