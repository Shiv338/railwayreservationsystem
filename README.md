# 🚆 Railway Reservation System

A console-based Railway Reservation System developed using **Python and
Object-Oriented Programming (OOP)** concepts.

The project simulates basic railway reservation operations such as
adding trains, searching trains, booking tickets, cancelling tickets,
and managing passenger and ticket information.

## Project Overview

The Railway Reservation System is a modular Python application designed
to demonstrate practical use of OOP concepts.

The project separates different responsibilities into classes and
packages, making the code easier to understand, maintain, and extend.

## Features

-   Add new train
-   View all available trains
-   Search train by source and destination
-   Book railway ticket
-   Cancel railway ticket
-   View ticket using PNR
-   View passenger details
-   Manage available seats
-   Automatic Passenger ID generation
-   Automatic PNR generation
-   Prevent duplicate train numbers
-   Basic input validation
-   Modular Python project structure

## Technologies Used

-   Python 3
-   Object-Oriented Programming (OOP)
-   Python Modules and Packages
-   Command Line Interface (CLI)

## OOP Concepts Used

### Classes and Objects

The project contains the following major classes:

-   `Train`
-   `Passenger`
-   `Ticket`
-   `RailwayReservationSystem`

### Encapsulation

Data and related methods are organized inside classes.

### Composition

The `Ticket` class contains references to both a `Passenger` object and
a `Train` object.

``` python
self.passenger = passenger
self.train = train
```

### Modular Programming

Classes are separated into different Python files and packages for
better organization.

## Project Structure

RailwayReservationSystem/
│
├── README.md
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── train.py
│   ├── passenger.py
│   └── ticket.py
│
└── system/
    ├── __init__.py
    └── reservation_system.py

### `models/train.py`

Contains the `Train` class.

Train information includes:

-   Train Number
-   Train Name
-   Source
-   Destination
-   Available Seats
-   Fare

### `models/passenger.py`

Contains the `Passenger` class.

Passenger information includes:

-   Passenger ID
-   Name
-   Age
-   Gender

### `models/ticket.py`

Contains the `Ticket` class.

Ticket information includes:

-   PNR
-   Passenger
-   Train
-   Seat Number
-   Ticket Status

### `system/reservation_system.py`

Contains the `RailwayReservationSystem` class.

It manages:

-   Trains
-   Passengers
-   Tickets
-   Passenger ID generation
-   PNR generation
-   Train management
-   Train searching

### Open the Project

Open the `RailwayReservationSystem` folder in VS Code.



## Main Menu

The application provides options such as:
     RAILWAY RESERVATION SYSTEM
1. Add Train
2. View All Trains
3. Search Train
4. Book Ticket
5. Cancel Ticket
6. View Ticket
7. View Passengers
8. Exit


## Adding a Train

Select:
1. Add Train

Then enter the required information:
Enter Train Number: 12301
Enter Train Name: Rajdhani Express
Enter Source: Delhi
Enter Destination: Mumbai
Enter Number of Seats: 100
Enter Fare: 1500


The train is then added to the system.

## 🎫 Booking a Ticket

Select:
Book Ticket

The user enters the train number and passenger details.

The system generates:

-   Passenger ID
-   PNR
-   Seat Number

The initial ticket status is:

``` text
CONFIRMED
```

## ❌ Cancelling a Ticket

Select:
 Cancel Ticket

Enter the PNR number.

The system changes the ticket status to:


CANCELLED


and makes the seat available again.

## Viewing a Ticket

Select:


6. View Ticket

Enter the PNR number to display the ticket details.

## Learning Objectives

This project demonstrates practical understanding of:

-   Python programming
-   Object-Oriented Programming
-   Classes and Objects
-   Constructors
-   Methods
-   Object relationships
-   Modules and Packages
-   Exception Handling
-   Modular software design


## Author

**Shiv Sagar Kumar**

B.Tech -- Computer Science & Engineering

