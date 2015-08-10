
from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Boolean

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

#PLACE YOUR TABLE SETUP INFORMATION HERE
class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	name = Column(String(30))
	age = Column(Integer)
	email = Column(String(50))
	password = Column(String(30))
	experience = Column(String(10))## either visit study or host
	address = Column(String(70))
	city_id = Column(Integer)

class Trip(Base):
	__tablename__ = 'trips'
	id = Column(Integer, primary_key=True)
	traveler_id = Column(Integer)
	destination_id = Column(Integer)
	departure = Column(Date) ##date of leaving original country
	arrival = Column(Date) ##date of arriving at original country

class City(Base):
	__tablename__ = 'cities'
	id = Column(Integer, primary_key=True)
	name = Column(String(50))
	num_of_visitors = Column(Integer) ##keeps adding everytime someone visits
	photo = Column(String)


