# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 21:57:15 2025

@author: Admin
"""

# Car Showroom Management System

# -------------------- Custom Exception --------------------
class LowSalaryException(Exception):
    """Raised when user salary is less than required amount"""
    def __init__(self, message="Access Denied! Salary must be at least ₹1,00,000 to view car details."):
        super().__init__(message)

# -------------------- Car Class --------------------
class Car:
    def __init__(self, brand, model, price, fuel_type, transmission, color):
        self.__brand = brand            # Encapsulation
        self.__model = model
        self.__price = price
        self.__fuel_type = fuel_type
        self.__transmission = transmission
        self.__color = color

    def get_model(self):
        return self.__model

    def display_summary(self):
        return f"{self.__brand} {self.__model} - ₹{self.__price}"

    def display_details(self):
        return (f"Brand: {self.__brand}\n"
                f"Model: {self.__model}\n"
                f"Price: ₹{self.__price}\n"
                f"Fuel Type: {self.__fuel_type}\n"
                f"Transmission: {self.__transmission}\n"
                f"Color: {self.__color}\n")

# -------------------- Showroom Class --------------------
class Showroom:
    def __init__(self):
        self.inventory = []

    def view_available_cars(self):
        if not self.inventory:
            print("\nNo cars available in the showroom.\n")
        else:
            print("\nAvailable Cars:")
            for idx, car in enumerate(self.inventory, start=1):
                print(f"{idx}. {car.display_summary()}")

    def display_car_details(self, model, user_salary):
        try:
            if user_salary < 100000:
                raise LowSalaryException()
            for car in self.inventory:
                if car.get_model().lower() == model.lower():
                    print("\nCar Details:")
                    print(car.display_details())
                    return
            print("Car not found!")
        except LowSalaryException as e:
            print(f"Error: {e}")

    def sell_car(self, model):
        for car in self.inventory:
            if car.get_model().lower() == model.lower():
                self.inventory.remove(car)
                print(f"\nCar '{model}' sold successfully!\n")
                return
        print("Car not found!")

    def buy_car(self, car):
        self.inventory.append(car)
        print(f"\nCar '{car.get_model()}' added to showroom successfully!\n")

# -------------------- Menu Driven Program --------------------
def main():
    showroom = Showroom()

    # Adding some initial cars
    showroom.buy_car(Car("Toyota", "Fortuner", 3200000, "Diesel", "Automatic", "White"))
    showroom.buy_car(Car("Hyundai", "Creta", 1500000, "Petrol", "Manual", "Black"))
    showroom.buy_car(Car("Maruti", "Baleno", 900000, "Petrol", "Automatic", "Red"))

    while True:
        print("\n------ Car Showroom Management ------")
        print("1. View Available Cars")
        print("2. Display Car Details")
        print("3. Sell a Car")
        print("4. Buy a Car")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            showroom.view_available_cars()

        elif choice == '2':
            model = input("Enter car model to view details: ")
            salary = int(input("Enter your salary: "))
            showroom.display_car_details(model, salary)

        elif choice == '3':
            model = input("Enter car model to sell: ")
            showroom.sell_car(model)

        elif choice == '4':
            brand = input("Enter Car Brand: ")
            model = input("Enter Car Model: ")
            price = int(input("Enter Car Price: "))
            fuel_type = input("Enter Fuel Type: ")
            transmission = input("Enter Transmission (Manual/Automatic): ")
            color = input("Enter Color: ")
            new_car = Car(brand, model, price, fuel_type, transmission, color)
            showroom.buy_car(new_car)

        elif choice == '5':
            print("Exiting... Thank you for visiting!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
