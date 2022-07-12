import time
from getpass import getpass


class bike_class:
    log_count = 0
    first_count = 0
    room_no_count = 0
    lst = []

    def __init__(
        self,
        days="",
        date="",
        cindate="",
        person="",
        room="",
        rno=0,
        lst=[]
    ):
        self.lst = []
        self.days = days
        self.date = date
        self.cindate = cindate
        self.person = person
        self.room = room


def main():

    rooms = []
    a = None  # object of class
    count = 0
    log = 0
    lst = []
    ttl = []
    n = 0
    start = 0
    bikes_rented = 0
    bike_choise = ""
    hours = 0
    rate = 10
    while 1:
        print("\n--------------")
        print("Bike Rental Shop")
        print("--------------")
        print("\n1. Admin")

        print("2. User")

        print("3. EXIT")
        print("\n--------------")

        b = int(input("\n\nEnter your choice: "))
        if b == 1:
            a = bike_class()
            while 1:
                print("\n--------------")
                print("\n1. Add Inventory")
                print("2. View Inventory")
                print("3. Total Bikes Rented")
                print("4. Total Revenue Generated")
                print("5. Exit")
                print("\n--------------")

                adm_choise = int(input("\nEnter your choise: "))
                if adm_choise == 1:
                    start += 1
                    n = int(input("\nHow many inventories you want to add: "))
                    # iterating till the range
                    for i in range(0, n):
                        print(f"\nInventory number: {i+1}")
                        ele1 = input("\nBike Type: ")
                        # bikes_rented += 1
                        ele2 = input("Amount of bikes: ")
                        lst.append(ele1)  # adding the element
                        ttl.append(ele2)

                    print("\n---Inventory added---\n")
                elif adm_choise == 2:
                    print("\nBikes\t\tAmount\n")
                    for i in range(0, n):
                        print(f"{lst[i]}\t\t{ttl[i]}")
                elif adm_choise == 3:
                    print(f"\n\nBike name: {bike_choise}")
                    print(f"\nTotal Bikes Rented: {bikes_rented}")
                elif adm_choise == 4:
                    print(f"\nTotal Bikes Rented: {bikes_rented}")
                    print(f"Total hours Rented: {hours}hrs")
                    print("Rate per hour: $10")
                    print(f"Total revenue: ${bikes_rented * hours * rate}")
                elif adm_choise == 5:
                    break
                else:
                    print('\nWrong Input')

        if b == 2:
            yes = 0
            while 1:
                print("\n--------------")
                print("\n1. New Customer Rental")

                print("2. Show Inventory")

                print("3. Rental Return")

                print("4. Exit")
                print("\n--------------")

                choise = int(input("\n\nEnter your choice: "))
                if choise == 1:
                    if start > 0:
                        yes += 1
                        print("\nCredentials")
                        name = input("\nEnter your name: ")
                        iid = input("Enter your unique ID: ")
                        print("\nWhich bike you want to rent:\n")
                        for i in range(0, n):
                            print(f"{lst[i]}")
                        bike_choise = input("\nEnter bike name: ")
                        bikes_rented = int(
                            input("How many bike you want to rent: "))
                        hours = int(
                            input("For how many hours you want to rent: "))
                        print("\n---Now you can check Rental Return---")
                    else:
                        print("\nNo Inventory added. Ask admin to add inventory first")

                elif choise == 2:
                    print("\nBikes     \tAmount\n")
                    for i in range(0, n):
                        print(f"{lst[i]}  \t{ttl[i]}")

                elif choise == 3:
                    if yes > 0:
                        print(f"\nID: {iid}")
                        print(f"Name: {name}")
                        print(f"Type of Bike: {bike_choise}")
                        print(f"Bike Rent: ${hours*rate*bikes_rented}")
                    else:
                        print("\nNo Record Found. First rent a bike")

                elif choise == 4:
                    break
                else:
                    print("\nWrong Input")
        if b == 3:
            print("\n---Thanks for using Bike Rental Shop---")
            quit()


main()
