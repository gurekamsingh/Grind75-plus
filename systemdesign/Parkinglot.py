# Assuming functional requirements:
# 1. Parking lot with multiple levels
# 2. vehicle types: motorcycle, car, bus
# 3. parking spot types: motorcycle, compact, large
# 4. parking rules:
#    - motorcycle can park in any spot
#    - car can park in compact or large spot
#    - bus can park in large spots

from enum import Enum
import uuid, datetime

class Vehicle:
    def __init__(self, license_plate):
        self.license_plate = license_plate

class Motorcycle(Vehicle): pass
class Car(Vehicle): pass
class Bus(Vehicle): pass

class spot_type(Enum):
    MOTORCYCLE = 1
    COMPACT = 2
    LARGE = 3

class parking_spot:
    def __init__(self, spot_type, spot_id, is_free=True):
        self.spot_type = spot_type
        self.spot_id = spot_id
        self.is_free = is_free
        self.vehicle = None

    def park(self, vehicle):
        self.is_free = False
        self.vehicle = vehicle

    def free(self):
        self.is_free = True
        self.vehicle = None

class Ticket:
    def __init__(self, vehicle, spot_type):
        self.ticket_id = uuid.uuid4()
        self.issue_time = datetime.datetime.now()
        self.vehicle = vehicle
        self.spot_type = spot_type
        self.spot_id = None
        self.spot = None

class Parkingfloor:
    def __init__(self, floor_number, spots):
        self.floor_number = floor_number
        self.spots = spots

    # def is_spot_compatible(self, spot, vehicle):
    #     if isinstance(vehicle, Motorcycle):
    #         return True
    #     if isinstance(vehicle, Car):
    #         return spot.spot_type in [spot_type.COMPACT, spot_type.LARGE]
    #     if isinstance(vehicle, Bus):
    #         return spot.spot_type == spot_type.LARGE
    #     return False

    def available_spots(self, vehicle):
        for spot in self.spots:
            if spot.is_free: # and self.is_spot_compatible(spot, vehicle):
                return spot
        return None

class Parkinglot:
    def __init__(self, floors):
        self.floors = floors
        self.active_tickets = {}

    def park_vehicle(self, vehicle):
        for floor in self.floors:
            spot = floor.available_spots(vehicle)
            if spot:
                spot.park(vehicle)
                ticket = Ticket(vehicle, spot.spot_type)
                ticket.spot = spot
                ticket.spot_id = spot.spot_id
                self.active_tickets[ticket.ticket_id] = ticket
                return ticket
        raise Exception("No available parking spots for this vehicle type")

    def unpark_vehicle(self, ticket_id):
        ticket = self.active_tickets.pop(ticket_id, None)
        if ticket and ticket.spot:
            ticket.spot.free()
            return True
        return False



# Vehicle <--- Bike, Car, Truck
# ParkingSpot → belongs to → ParkingFloor → part of → ParkingLot
# Vehicle → parked in → ParkingSpot
# Ticket → issued for → Vehicle + Spot

# example usage:
motorcycle = Motorcycle("MOTO123")
car = Car("CAR456")
bus = Bus("BUS789")
parking_spot1 = parking_spot(spot_type.MOTORCYCLE, "SPOT1")
parking_spot2 = parking_spot(spot_type.COMPACT, "SPOT2")
parking_spot3 = parking_spot(spot_type.LARGE, "SPOT3")  

parking_floor1 = Parkingfloor(1, [parking_spot1, parking_spot2, parking_spot3])
parking_lot = Parkinglot([parking_floor1])
# Park vehicles
ticket1 = parking_lot.park_vehicle(motorcycle)
ticket2 = parking_lot.park_vehicle(car)
print(f"Ticket issued for motorcycle: {ticket1.ticket_id}, Spot: {ticket1.spot_id}")
print(f"Ticket issued for car: {ticket2.ticket_id}, Spot: {ticket2.spot_id}")