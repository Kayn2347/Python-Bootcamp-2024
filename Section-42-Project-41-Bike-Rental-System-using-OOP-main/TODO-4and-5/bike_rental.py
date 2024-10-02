import datetime as dt


# TODO 1 - Create Bike Rental Class and initialize stock attribute
class BikeRental:
    def __init__(self, stock=0):
        """Initializer for Bike rental class"""
        self.stock = stock

    # TODO 2 - Create a method to display stock
    def display_stock(self):
        """Display bikes that currently available in the system"""
        print(f"We have currently {self.stock} bikes available in the system")
        return self.stock
    # TODO 3 - Create a method to rent bike on hourly bases
    def rent_bike_on_hourly_basis(self, n):
        """Rents a bike on hourly basis"""
        if n <= 0:
            print("The number of bikes must be positive number!")
            return None
        elif n > self.stock:
            print(f"Sorry! We have only {self.stock} bikes available to rent!")
            return None
        else:
            now = dt.datetime.now()
            print(f"You have rented {n} bike(s) on hourly basis today at {now.hour}:{now.minute}:{now.second}")
            print("Your will be charged $5 for each bike per hour")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now


# TODO 4 - Create a method to rent bike on daily bases
def rent_bike_on_daily_basis(self, n):
    """Rents a bike on daily basis"""
    if n <= 0:
        print("The number of bikes must be positive number!")
    elif n > self.stock:
        print(f"Sorry! we have currently {self.stock} bikes available to rent.")
    else:
        now = dt.datetime.today()
        print(f"You have rented {n} bike(s) on daily basis today on {now}")
        print("Your will be charged $20 for each bike daily")
        print("We hope that you enjoy our service.")
        self.stock -= n
        return now

# TODO 5 - Create a method to rent bike on weekly bases
def rent_bike_on_weekly_basis(self, n):
    """Rents a bike on weekly basis"""
    if n <= 0:
        print("The number of bikes must be positive number!")
    elif n > self.stock:
        print(f"Sorry! we have currently {self.stock} bikes available to rent.")
    else:
        now = dt.datetime.today()
        print(f"You have rented {n} bike(s) on weekly basis today on {now}")
        print("Your will be charged $60 for each bike weekly")
        print("We hope that you enjoy our service.")
        self.stock -= n
        return now

rental_system = BikeRental(40)
(rental_system.rent_bike_on_hourly_basis(2)
rental_system.display_stock()