from database_setup import Base,User,City,Trip
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


j = City(name='Jerusalem', num_of_visitors=0, photo='jerusalem.jpeg')
session.add(j)
t= City(name='Tel_Aviv', num_of_visitors=0, photo='telaviv.jpg')
session.add(t)
n= City(name='Nazareth', num_of_visitors=0, photo='Nazareth1.jpg')
session.add(n)
session.commit()
