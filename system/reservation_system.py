from models.passenger import Passenger
from models.ticket import Ticket
import random


class RailwayReservationSystem:
    def __init__(self):
        self.trains = []
        self.passengers = []
        self.tickets = []
        self.passenger_id_counter = 1
        self.used_pnrs = set()

    def add_train(self, train):
        self.trains.append(train)
        print(f"Train {train.name} added successfully!")

    def show_trains(self):
        if not self.trains:
            print("\nNo trains available.")
            return
        print("\n" + "="*60)
        for train in self.trains:
            print(f"Train No: {train.train_no}, Name: {train.name}")
            print(f"Route: {train.source} -> {train.destination}")
            print(f"Available Seats: {train.seats}, Fare: ₹{train.fare}")
            print("-"*60)

    def search_train(self, source, destination):
        found = [t for t in self.trains if t.source.lower() == source.lower() and t.destination.lower() == destination.lower()]
        if not found:
            print("\nNo trains found for this route.")
            return
        print("\n" + "="*60)
        for train in found:
            print(f"Train No: {train.train_no}, Name: {train.name}")
            print(f"Available Seats: {train.seats}, Fare: ₹{train.fare}")
            print("-"*60)

    def generate_passenger_id(self):
        passenger_id = self.passenger_id_counter
        self.passenger_id_counter += 1
        return passenger_id

    def generate_pnr(self):
        while True:
            pnr = random.randint(1000000000, 9999999999)  # Generate 10-digit PNR
            if pnr not in self.used_pnrs:
                self.used_pnrs.add(pnr)
                return pnr

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def view_passengers(self):
        if not self.passengers:
            print("\nNo passengers booked.")
            return
        print("\n" + "="*60)
        for passenger in self.passengers:
            passenger.display_passenger()
            print("-"*60)

    def view_trains(self):
        if not self.tickets:
            print("\nNo tickets booked.")
            return
        print("\n" + "="*60)
        for ticket in self.tickets:
            ticket.display_ticket()
            print("-"*60)

    def book_train(self):
        if not self.trains:
            print("\nNo trains available. Add a train first.")
            return

        try:
            train_no = int(input("Enter train number: "))
        except ValueError:
            print("Invalid train number.")
            return

        train = next((t for t in self.trains if t.train_no == train_no), None)

        if train is None:
            print("Train not found.")
            return

        if train.seats <= 0:
            print("No seats available on this train.")
            return

        name = input("Enter passenger name: ").strip()

        try:
            age = int(input("Enter passenger age: "))
        except ValueError:
            print("Invalid age.")
            return

        gender = input("Enter passenger gender: ").strip()

        passenger = Passenger(
            self.generate_passenger_id(),
            name,
            age,
            gender
        )

        self.add_passenger(passenger)

        seat_no = train.total_seats - train.seats + 1
        train.seats -= 1

        ticket = Ticket(
            self.generate_pnr(),
            passenger,
            train,
            seat_no
        )

        self.add_ticket(ticket)

        print("\nTicket booked successfully!")
        ticket.display_ticket()

    def cancel_train(self):
        if not self.tickets:
            print("\nNo tickets booked.")
            return

        try:
            pnr = int(input("Enter PNR to cancel: "))
        except ValueError:
            print("Invalid PNR.")
            return

        ticket = next(
            (t for t in self.tickets if t.pnr == pnr),
            None
        )

        if ticket is None:
            print("Ticket not found.")
            return

        if ticket.status == "CANCELLED":
            print("Ticket is already cancelled.")
            return

        ticket.status = "CANCELLED"
        ticket.train.seats += 1

        print(f"Ticket with PNR {pnr} cancelled successfully.")