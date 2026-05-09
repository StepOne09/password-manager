import json
import os
from getpass import getpass

FILE_NAME = "passwords.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def add_password(data):
    website = input("Website: ")
    username = input("Username/Email: ")
    password = getpass("Password: ")

    entry = {
        "website": website,
        "username": username,
        "password": password
    }

    data.append(entry)
    save_data(data)

    print("\nPassword saved successfully.\n")

def view_passwords(data):
    if not data:
        print("\nNo passwords stored.\n")
        return

    print("\nStored Passwords:\n")

    for i, entry in enumerate(data, start=1):
        print(f"{i}. Website : {entry['website']}")
        print(f"   Username: {entry['username']}")
        print(f"   Password: {entry['password']}")
        print()

def search_password(data):
    keyword = input("Search website: ").lower()

    found = False

    for entry in data:
        if keyword in entry["website"].lower():
            print("\nMatch Found:\n")
            print(f"Website : {entry['website']}")
            print(f"Username: {entry['username']}")
            print(f"Password: {entry['password']}")
            print()
            found = True

    if not found:
        print("\nNo matching website found.\n")

def delete_password(data):
    view_passwords(data)

    if not data:
        return

    try:
        number = int(input("Enter entry number to delete: "))

        if 1 <= number <= len(data):
            removed = data.pop(number - 1)
            save_data(data)

            print(f"\nDeleted {removed['website']} successfully.\n")
        else:
            print("\nInvalid entry number.\n")

    except ValueError:
        print("\nPlease enter a valid number.\n")

def main():
    data = load_data()

    while True:
        print("===== PASSWORD MANAGER =====")
        print("1. View Passwords")
        print("2. Add Password")
        print("3. Search Password")
        print("4. Delete Password")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            view_passwords(data)

        elif choice == "2":
            add_password(data)

        elif choice == "3":
            search_password(data)

        elif choice == "4":
            delete_password(data)

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option.\n")

if __name__ == "__main__":
    main()
