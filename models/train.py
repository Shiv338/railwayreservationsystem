class Train:
    def __init__(self,train_no,name,source,destination,seats,fare):

        self.train_no=train_no
        self.name=name
        self.source=source
        self.destination=destination
        self.seats=seats
        self.total_seats=seats
        self.fare=fare

    def display_train(self):
        print("TRAIN DETAILS")

        print(f"train no: {self.train_no}")
        print(f"name: {self.name}")
        print(f"source:{self.source}")
        print(f"destination:{self.destination}")
        print(f"available:{self.seats}")
        print(f"fare:{self.fare}")
