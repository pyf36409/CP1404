from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
menu = "q)uit, c)hoose taxi, d)rive"
car = ""
taxi = 0
total = 0
print("Let's drive!")
print(menu)
choice = input(">>> ")
while choice != "q":
    if choice == "c":
        print("Taxis available:")
        print(Taxi)
        choice = int(input("Choose taxi: "))
        while choice > len(taxis):
            print("Invalid taxi choice")
            choice = input(">>> ")
        taxi = taxis[choice]
    elif choice == "d":
        if car == "":
            print("You need to choose a taxi before you can drive")
            choice = input(">>> ")
        else:
            distance = input("Drive how far? ")
            taxi.drive(distance)
            print(f"Your Prius trip cost you ${taxi.get_fare()}")
            total = total + taxi.get_fare()
    else:
        print("Invalid option")
        choice = input(">>> ")
print(f"Total trip cost: ${total}")
print(Taxi)
