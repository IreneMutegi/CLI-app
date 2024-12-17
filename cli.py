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
    room_id = int(input('Enter room ID to update: '))
    
    room = session.get(Room, room_id)
    if not room:
        print(f"Room with ID {room_id} does not exist.")
        return
    
    room.name = input(f"Enter new name for Room (current: {room.name}): ") or room.name
    session.commit()
    print(f"Room with ID {room_id} updated successfully.")

def delete_room():
   room_id = int(input('Enter room ID to update: '))
   room = session.get(Room, room_id)
   if not room:
        print(f"Room with ID {room_id} does not exist.")
        return

   session.delete(room)
   session.commit()
   print(f"Room with ID {room_id}  successfully.")



   def 

