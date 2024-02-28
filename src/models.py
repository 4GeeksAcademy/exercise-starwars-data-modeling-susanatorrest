import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__ = 'characters'
    id          = Column(Integer, primary_key=True)
    name        = Column(String(250), nullable=False)
    mass        = Column(String(30), nullable=False)
    hair_color	= Column(String(10), nullable=False)
    skin_color	= Column(String(10), nullable=False)
    eye_color	= Column(String(10), nullable=False)
    birth_year	= Column(String(10), nullable=False)
    gender	    = Column(String(30), nullable=False)
    height      = Column(String(10), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id              = Column(Integer, primary_key=True)
    name            = Column(String(250), nullable=False)
    diameter        = Column(Integer(), nullable=False)
    rotation_period	= Column(Integer(), nullable=False)
    orbital_period	= Column(Integer(), nullable=False)
    gravity	        = Column(String(20), nullable=False)
    population	    = Column(Integer(), nullable=False)
    climate	        = Column(String(30), nullable=False)
    terrain         = Column(String(10), nullable=False)
    surface_water   = Column(Integer(), nullable=False)


class Vehicles(Base):
    __tablename__ = 'vehicles'
    id                      = Column(Integer, primary_key=True)
    name                    = Column(String(250), nullable=False)
    model                   = Column(String(50), nullable=False)
    vehicle_class	        = Column(String(50), nullable=False)
    manufacturer	        = Column(String(50), nullable=False)
    cost_in_credits	        = Column(Integer(), nullable=False)
    length	                = Column(Integer(), nullable=False)
    crew	                = Column(Integer(), nullable=False)
    max_atmosphering_speed  = Column(Integer(), nullable=False)
    cargo_capacity          = Column(Integer(), nullable=False)
    consumables             = Column(String(20), nullable=False)
    films                   = Column(Integer(), nullable=False)
    pilots                  = Column(Integer(), nullable=False)

class Starships(Base):
    __tablename__ = 'starships'
    id                      = Column(Integer, primary_key=True)
    name                    = Column(String(250), nullable=False)
    model                   = Column(String(50), nullable=False)
    starship_class	        = Column(String(50), nullable=False)
    manufacturer	        = Column(String(50), nullable=False)
    cost_in_credits	        = Column(Integer(), nullable=False)
    length	                = Column(Integer(), nullable=False)
    crew	                = Column(Integer(), nullable=False)
    passengers              = Column(Integer(), nullable=False)
    max_atmosphering_speed  = Column(Integer(), nullable=False)
    cargo_capacity          = Column(Integer(), nullable=False)
    consumables             = Column(String(30), nullable=False)
    films                   = Column(Integer(), nullable=False)
    pilots                  = Column(Integer(), nullable=False)

class User(Base):
    __tablename__ = 'user'
    id            = Column(Integer, primary_key=True)
    name          = Column(String(250))
    last_name     = Column(String(250))
    email         = Column(String(50))
    password      = Column(String(50))
    date_subscrip = Column(String(50))
    Activo        = Column(String(1))
    

class Favorites(Base):
    __tablename__ = 'favorites'
    id            = Column(Integer, primary_key=True)
    character_id  = Column(Integer, ForeignKey('characters.id'))
    vehicle_id   = Column(Integer, ForeignKey('vehicles.id'))
    planet_id    = Column(Integer, ForeignKey('planets.id'))
    user_id    = Column(Integer, ForeignKey('user.id'))
    starships_id  = Column(Integer, ForeignKey('starships.id'))
    user       = relationship(User)
    character        = relationship(Characters)
    vehicle          = relationship(Vehicles)
    planet         = relationship(Planets)
    star          = relationship(Starships)


  

    def to_dict(self):
        return {}
    
render_er(Base, 'diagram.png')