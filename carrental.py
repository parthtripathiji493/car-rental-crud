

cars = []       # List to store car records
customers = []  # List to store customer records
rentals = []    # List to store rental records



def add_car():
    print("\n--- Add New Car ---")
    car_id = len(cars) + 1
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = input("Enter car year: ")
    daily_rate = float(input("Enter daily rent price: "))

    car = {
        "id": car_id,
        "make": make,
        "model": model,
        "year": year,
        "daily_rate": daily_rate,
        "available": True
    }

    cars.append(car)
    print("Car added successfully!")


def view_cars():
    print("\n--- List of Cars ---")
    if not cars:
        print("No cars available.")
    else:
        for car in cars:
            print(car)


def update_car():
    print("\n--- Update Car ---")
    car_id = int(input("Enter car ID: "))

    for car in cars:
        if car["id"] == car_id:
            car["make"] = input("Enter new make: ")
            car["model"] = input("Enter new model: ")
            car["year"] = input("Enter new year: ")
            car["daily_rate"] = float(input("Enter new daily rate: "))
            print("Car updated successfully!")
            return

    print("Car not found!")


def delete_car():
    print("\n--- Delete Car ---")
    car_id = int(input("Enter car ID: "))

    for car in cars:
        if car["id"] == car_id:
            cars.remove(car)
            print("Car deleted successfully!")
            return

    print("Car not found!")


def add_customer():
    print("\n--- Add Customer ---")
    customer_id = len(customers) + 1
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    customer = {"id": customer_id, "name": name, "phone": phone}
    customers.append(customer)

    print("Customer added successfully!")


def view_customers():
    print("\n--- Customer List ---")
    if not customers:
        print("No customers found.")
    else:
        for customer in customers:
            print(customer)




def rent_car():
    print("\n--- Rent a Car ---")
    car_id = int(input("Enter car ID: "))
    customer_id = int(input("Enter customer ID: "))
    days = int(input("Enter number of rental days: "))

    car = next((c for c in cars if c["id"] == car_id), None)
    customer = next((c for c in customers if c["id"] == customer_id), None)

    if car and customer:
        if car["available"]:
            total_cost = days * car["daily_rate"]
            rental = {
                "car_id": car_id,
                "customer_id": customer_id,
                "days": days,
                "total_cost": total_cost
            }
            rentals.append(rental)
            car["available"] = False
            print("Car rented successfully!")
            print("Total cost:", total_cost)
        else:
            print("Car is not available!")
    else:
        print("Car or customer not found!")


def view_rentals():
    print("\n--- Rental Records ---")
    if not rentals:
        print("No rentals found.")
    else:
        for rental in rentals:
            print(rental)


def return_car():
    print("\n--- Return a Car ---")
    car_id = int(input("Enter car ID to return: "))

    car = next((c for c in cars if c["id"] == car_id), None)

    if car:
        car["available"] = True
        print("Car returned successfully!")
    else:
        print("Car not found!")


def main_menu():
    while True:
        print("\n====== CAR RENTAL MANAGEMENT ======")
        print("1. Add Car")
        print("2. View Cars")
        print("3. Update Car")
        print("4. Delete Car")
        print("5. Add Customer")
        print("6. View Customers")
        print("7. Rent Car")
        print("8. View Rentals")
        print("9. Return Car")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_car()
        elif choice == "2":
            view_cars()
        elif choice == "3":
            update_car()
        elif choice == "4":
            delete_car()
        elif choice == "5":
            add_customer()
        elif choice == "6":
            view_customers()
        elif choice == "7":
            rent_car()
        elif choice == "8":
            view_rentals()
        elif choice == "9":
            return_car()
        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid option! Try again.")


# Run the menu
main_menu()