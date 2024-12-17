import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Room, Guest, Amenity

DATABASE_URL = "sqlite:///guests.db"

engine = create_engine (DATABASE_URL)
Session = sessionmaker (bind=engine)
session = Session()

def init_db():
    Base.metadata.create_all(engine)
    print("Database Initialized")


def create_room():
    name = input("Enter Room Name: ")
    
    room = Room(name=name)
    
    session.add(room)
    session.commit()
    
    print(f'Room "{name}" created with ID {room.id}')

def update_room():
    pass

