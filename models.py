from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Room(Base):  
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    guests = relationship("Guest", back_populates="room")

    def __repr__(self):
        return f'id="{self.id}", name="{self.name}"'

class Amenity(Base):  
    __tablename__ = "amenities"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    guests = relationship("Guest", back_populates="amenity")  

    def __repr__(self):
        return f'id="{self.id}", name="{self.name}"'


class Guest(Base):
    __tablename__ = "guests"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(Integer, unique=True, nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"))  
    amenity_id = Column(Integer, ForeignKey("amenities.id"))  

    room = relationship("Room", back_populates="guests")  
    amenity = relationship("Amenity", back_populates="guests")  

    def __repr__(self):
        return f'name="{self.name}", room_id="{self.room_id}", amenity_id="{self.amenity_id}"'
