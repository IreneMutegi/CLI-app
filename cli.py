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

def create_guest():
    name = input("Enter guest name: ")
    email = input("Enter guest email: ")
    phone_number = int(input("Enter guest phone number: "))

    room_id = int(input("Enter room ID for the guest: "))
    amenity_id = int(input("Enter amenity ID for the guest: "))

    guest = Guest(
        name=name,
        email=email,
        phone_number=phone_number,
        room_id=room_id,
        amenity_id=amenity_id
    )

    session.add(guest)
    session.commit()
    
    print(f"Guest '{name}' created with ID {guest.id}.")




def update_guest():
    guest_id = int(input('Enter guest ID to update: '))
    
    guest = session.get(Guest, guest_id)
    if not guest:
        print(f"Guest with ID {guest_id} does not exist.")
        return
    
    guest.name = input(f"Enter new name for Guest (current: {guest.name}): ") or guest.name
    guest.email = input(f"Enter new email for Guest (current: {guest.email}): ") or guest.email
    guest.phone_number = int(input(f"Enter new phone number for Guest (current: {guest.phone_number}): ") or guest.phone_number)
    
    new_room_id = int(input(f"Enter new room ID for Guest (current: {guest.room_id}): ") or guest.room_id)
    guest.room_id = new_room_id

    new_amenity_id = int(input(f"Enter new amenity ID for Guest (current: {guest.amenity_id}): ") or guest.amenity_id)
    guest.amenity_id = new_amenity_id
    
    session.commit()
    print(f"Guest with ID {guest_id} updated successfully.")

def delete_guest():
    guest_id = int(input('Enter guest ID to delete: '))
    
    guest = session.get(Guest, guest_id)
    if not guest:
        print(f"Guest with ID {guest_id} does not exist.")
        return
    
    session.delete(guest)
    session.commit()
    print(f"Guest with ID {guest_id} deleted successfully.")

def create_amenity():
    name = input("Enter amenity name: ")

    amenity = Amenity(name=name)

    session.add(amenity)
    session.commit()
    
    print(f"Amenity '{name}' created with ID {amenity.id}.")

def update_amenity():
    amenity_id = int(input('Enter amenity ID to update: '))
    
    amenity = session.get(Amenity, amenity_id)
    if not amenity:
        print(f"Amenity with ID {amenity_id} does not exist.")
        return
    
    amenity.name = input(f"Enter new name for Amenity (current: {amenity.name}): ") or amenity.name
    
    session.commit()
    print(f"Amenity with ID {amenity_id} updated successfully.")

def delete_amenity():
    amenity_id = int(input('Enter amenity ID to delete: '))
    
    amenity = session.get(Amenity, amenity_id)
    if not amenity:
        print(f"Amenity with ID {amenity_id} does not exist.")
        return
    
    session.delete(amenity)
    session.commit()
    print(f"Amenity with ID {amenity_id} deleted successfully.")

def assign_guest():
    guest_id = int(input('Enter Guest ID: '))
    room_id = int(input('Enter Room ID: '))
    amenity_id = int(input('Enter Amenity ID: '))

    guest = session.get(Guest, guest_id)
    room = session.get(Room, room_id)
    amenity = session.get(Amenity, amenity_id)

    if not guest or not room or not amenity:
        print("Invalid input: Guest, Room, or Amenity not found.")
        return

    guest.room_id = room_id
    guest.amenity_id = amenity_id

    session.commit()
    print(f"Guest '{guest.name}' assigned to Room '{room.name}' with Amenity '{amenity.name}'.")



def list_rooms():
    rooms = session.query(Room).all()

    if not rooms:
        print("No rooms found.")
        return

    print("Rooms:")
    for room in rooms:
        print(f"Room ID: {room.id}, Name: {room.name}")

def list_amenities():
    amenities = session.query(Amenity).all()

    if not amenities:
        print("No amenities found.")
        return

    print("\nAmenities:")
    for amenity in amenities:
        print(f"Amenity ID: {amenity.id}, Name: {amenity.name}")



def list_guests():
    guests = session.query(Guest).all()

    if not guests:
        print("No guests found.")
        return

    print("Guests List:")
    for guest in guests:
        print(f"Guest ID: {guest.id}, Name: {guest.name}, Email: {guest.email}, Phone: {guest.phone_number}")


def view_guests_by_room():
    room_id = int(input('Enter Room ID to view guests: '))

    room = session.get(Room, room_id)

    if not room:
        print(f"Room with ID {room_id} does not exist.")
        return

    guests = room.guests

    if not guests:
        print(f"No guests found for Room with ID {room_id}.")
        return

    print(f"Guests belonging to Room {room.name}:")
    for guest in guests:
        print(f"Guest ID: {guest.id}, Name: {guest.name}, Email: {guest.email}, Phone: {guest.phone_number}")

def view_guests_by_amenity():
    amenity_id = int(input('Enter Amenity ID to view guests: '))

    amenity = session.get(Amenity, amenity_id)

    if not amenity:
        print(f"Amenity with ID {amenity_id} does not exist.")
        return

    guests = amenity.guests

    if not guests:
        print(f"No guests found with Amenity ID {amenity_id}.")
        return

    print(f"Guests with Amenity {amenity.name}:")
    for guest in guests:
        print(f"Guest ID: {guest.id}, Name: {guest.name}, Email: {guest.email}, Phone: {guest.phone_number}")


    def main_menu():
        while True:
            print("\nWelcome to Luxury Hotel Management System")
            print("1. Initialize Database")
            print("2. Create Room")
            print("3. Update Room")
            print("4. Delete Room")
            print("5. Create Guest")
            print("6. Update Guest")
            print("7. Delete Guest")
            print("8. Create Amenity")
            print("9. Update Amenity")
            print("10. Delete Amenity")
            print("11. Assign Guest to Room and Amenity")
            print("12. List Rooms")
            print("13. List Amenities")
            print("14. List Guests")
            print("15. View Guests by Room")
            print("16. View Guests by Amenity")
            print("17. Exit")
            
            choice = input("Choose an option: ")
            
            if choice == '1':
                init_db()
            elif choice == '2':
                create_room()
            elif choice == '3':
                update_room()
            elif choice == '4':
                delete_room()
            elif choice == '5':
                create_guest()
            elif choice == '6':
                update_guest()
            elif choice == '7':
                delete_guest()
            elif choice == '8':
                create_amenity()
            elif choice == '9':
                update_amenity()
            elif choice == '10':
                delete_amenity()
            elif choice == '11':
                assign_guest()
            elif choice == '12':
                list_rooms()
            elif choice == '13':
                list_amenities()
            elif choice == '14':
                list_guests()
            elif choice == '15':
                view_guests_by_room()
            elif choice == '16':
                view_guests_by_amenity()
            elif choice == '17':
                print("Exiting...")
                sys.exit()
            else:
                print("Invalid option, please try again.")
