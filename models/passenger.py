class Passenger:

    def __init__(self, passenger_id, name, age, gender):
        self.passenger_id = passenger_id
        self.name = name
        self.age = age
        self.gender = gender

    def display_passenger(self):
        
        print("PASSENGER DETAILS")
        

        print(f"Passenger ID : {self.passenger_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

        