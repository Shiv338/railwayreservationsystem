class Ticket:

    def __init__(self, pnr, passenger, train, seat_no):
        self.pnr = pnr
        self.passenger = passenger
        self.train = train
        self.seat_no = seat_no
        self.status = "CONFIRMED"

    def display_ticket(self):
        
        print(" RAILWAY TICKET")
        

        print(f"PNR : {self.pnr}")

        print(f"Passenger Name: {self.passenger.name}")
        print(f"Passenger Age : {self.passenger.age}")
        print(f"Passenger Gender : {self.passenger.gender}")

        print(f"Train Number : {self.train.train_no}")
        print(f"Train Name: {self.train.name}")

        print(f"Source  : {self.train.source}")
        print(f"Destination : {self.train.destination}")

        print(f"Seat Number : {self.seat_no}")
        print(f"Fare : ₹{self.train.fare}")
        print(f"Status : {self.status}")

        