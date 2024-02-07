# Question 3 :-
# Medicine Store Management System
# Problem Statement:
# You are tasked with creating a Medicine Store Management System using lists and dictionaries. The
# system will allow users to perform various operations related to managing medicine inventory in a
# store. Implement the following menu-based operations:
# 1. Add Medicine:
# • Collect medicine details (Medicine ID, Medicine Name, Quantity, and Price).
# • Add the medicine to the store inventory.
# 2. Display Medicine Inventory:
# • Display details of all medicines in the store.
# 3. Update Medicine Quantity:
# • Update the quantity of a specific medicine in the inventory.
# 4. Search Medicine by ID:
# • Search for a medicine based on its ID.
# 5. Exit:
# • Exit the program.


# Answer
medicine_store = []


def add_medicine():
    medicine_id = input("Enter Medicine ID: ")
    medicine_name = input("Enter Medicine Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))
    medicine_store.append({
        "medicine_id": medicine_id,
        "medicine_name": medicine_name,
        "quantity": quantity,
        "price": price
    })


def display_medicine_inventory():
    print("Medicine ID\tMedicine Name\tQuantity\tPrice")
    for medicine in medicine_store:
        print(f"{medicine['medicine_id']}\t\t{medicine['medicine_name']}\t\t{medicine['quantity']}\t\t{medicine['price']}")


def update_medicine_quantity():
    medicine_id = input("Enter Medicine ID: ")
    new_quantity = int(input("Enter new Quantity: "))
    for medicine in medicine_store:
        if medicine["medicine_id"] == medicine_id:
            medicine["quantity"] = new_quantity
            print("Medicine Quantity Updated Successfully")
            return
    print("Medicine not found")


def search_medicine_by_id():
    medicine_id = input("Enter Medicine ID: ")
    for medicine in medicine_store:
        if medicine["medicine_id"] == medicine_id:
            print(f"Medicine ID: {medicine['medicine_id']}")
            print(f"Medicine Name: {medicine['medicine_name']}")
            print(f"Quantity: {medicine['quantity']}")
            print(f"Price: {medicine['price']}")
            return
    print("Medicine not found")


def main():
    while True:
        print("\nMedicine Store Management System")
        print("1. Add Medicine")
        print("2. Display Medicine Inventory")
        print("3. Update Medicine Quantity")
        print("4. Search Medicine by ID")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_medicine()
        elif choice == 2:
            display_medicine_inventory()
        elif choice == 3:
            update_medicine_quantity()
        elif choice == 4:
            search_medicine_by_id()
        elif choice == 5:
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
    