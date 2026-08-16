from models.train import Train
from system.reservation_system import RailwayReservationSystem

system=RailwayReservationSystem()

while True:

    
    print("  RAILWAY RESERVATION SYSTEM ")
    



    print("1.ADD TRAIN")
    print("2.VIEW ALL TRAIN")
    print("3.SEARCH TRAIN")
    print("4.BOOK TICKET")
    print("5.CANCEL TICKET")
    print("6.VIEW TICKET")
    print("7.VIEW PASSENGER")
    print("8..EXIT")


    choice=input("enter your choice : ")

    if choice=="1":
        try:
            train_no=int(input("enter train no: "))
            name=input("enter train name:")
            source=input("enter the source:")
            destination=input("enter destination:")
            seats=int(input("enter number of seats:"))
            fare=float(input("enter fare:"))

            train=Train(
                train_no,
                name,
                source,
                destination,
                seats,
                fare

            )
            system.add_train(train)
        except ValueError:
            print("invalid input! please enter corectly input")


    elif choice=="2":
        system.show_trains()

    elif choice=="3":

        source = input("Enter source: ")
        destination = input("Enter destination: ")
        system.search_train(source, destination)

    elif choice=="4":
        system.book_train()

    elif choice=="5":
        system.cancel_train()

    elif choice=="6":
        system.view_trains()

    elif choice=="7":
        system.view_passengers()

    elif choice=="8":
        print("thank you for using Railway Reservation System")

    else:
        print("invalid choice , please choose 1 to 8 options")

           




    



