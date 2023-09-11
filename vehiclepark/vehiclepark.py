import datetime
PARKING_FILE = "parking_details.txt"
LOGIN_FILE = "login_details.txt"
def register():
    while True:
        username = input("Enter username: ")
        with open(LOGIN_FILE, "r") as file:
            for line in file:
                line = line.strip().split(",")
                if line[0] == username :
                    print("Username already taken.Please enetr different one...\n")
                    break
            else:
                password = input("Enter password: ")
                with open(LOGIN_FILE, "a") as file:
                  file.write(f"{username},{password}\n")
                break
    print("Registration successful!")
    print("-"*70)

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open(LOGIN_FILE, "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")
            if username == stored_username and password == stored_password:
                print("Login successful!")
                print("------------------------")
                return True
    print("Invalid username or password. Please try again.")
    return False

def insert_details():
    plate_number = input("Enter vehicle plate number: ")
    driver_name = input("Enter driver name: ")
    vehicle_name = input("Enter vehicle name: ")
    vehicle_type = input("Enter vehicle type: ")
    parking_slot = find_empty_slot()
    if not parking_slot:
        print("No empty slots available.")
        return
    entry_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(PARKING_FILE, "a") as file:
        file.write(f"{plate_number},{driver_name},{vehicle_name},{vehicle_type},{parking_slot},{entry_time}\n")
        print("Details inserted successfully!.....")
        print("You Slot Number Will be :  " +parking_slot)
print("\n")

def find_empty_slot():
    with open(PARKING_FILE, "r") as file:
        slots = set(line.split(",")[4] for line in file)
    for i in range(1, 20): 
        if str(i) not in slots:
            return str(i)
    return None

def search_details():
    plate_number = input("Enter vehicle plate number: ")
    with open(PARKING_FILE, "r") as file:
        found = False
        for line in file:
            details = line.strip().split(",")
            if plate_number == details[0]:
                print("Details found!")
                print("------------------------")
                print(f"vehicle plate number: {details[0]}")
                print(f"Driver Name         : {details[1]}")
                print(f"Vehicle Name        : {details[2]}")
                print(f"Vehicle Type        : {details[3]}")
                print(f"Parking Slot        : {details[4]}")
                print(f"Entry Time          : {details[5]}")
                found = True
                break
        if not found:
            print("Details not found.")
    print("------------------------")

def delete_details():
    plate_number = input("Enter vehicle plate number: ")
    with open(PARKING_FILE, "r") as file:
        lines = file.readlines()
    with open(PARKING_FILE, "w") as file:
        deleted = False
        for line in lines:
            details = line.strip().split(",")
            if plate_number != details[0]:
                file.write(line)
            else:
                deleted = True
        if deleted:
            print("Details deleted successfully!")
        else:
            print("Details not found.")
    print("------------------------")

def display_all():
    with open("parking_details.txt", "r") as file:
        print("Plate Number  |   Driver Name   |   Vehicle Name |  Vehicle Type   |  Parking Slot  |  Entry Time")
        print("-" * 120)  
        for line in file:
            details = line.strip().split(",")
            plate_number= details[0].ljust(13)
            driver_name= details[1].ljust(15)
            vehicle_name = details[2].ljust(14)
            vehicle_type= details[3].ljust(15)
            parking_slot = details[4].ljust(14)
            entry_time = details[5]
            print(f"{plate_number} | {driver_name} | {vehicle_name} | {vehicle_type} | {parking_slot} | {entry_time}")
        print("-"*120)

def update_details():
    plate_number = input("Enter vehicle plate number: ")
    with open(PARKING_FILE, "r") as file:
        lines = file.readlines()
    with open(PARKING_FILE, "w") as file:
        updated = False
        for line in lines:
            details = line.strip().split(",")
            if plate_number == details[0]:
                driver_name = input("Enter new driver name: ")
                vehicle_name = input("Enter new vehicle name: ")
                vehicle_type = input("Enter new vehicle type: ")
                parking_slot=details[4]
                entry_time = details[5]
                updated_line = f"{plate_number},{driver_name},{vehicle_name},{vehicle_type},{parking_slot},{entry_time}\n"
                file.write(updated_line)
                updated = True
            else:
                file.write(line)
        if updated:
            print("Details updated successfully!")
        else:
            print("Details not found.")
    print("------------------------")

def calculate_payment(minutes): 
    rate = 3
    return rate *minutes

def generate_payment():
    plate_number = input("Enter vehicle plate number: ")
    with open(PARKING_FILE, "r") as file:
        found = False
        for line in file:
            details = line.strip().split(",")
            if plate_number == details[0]:
                entry_time = datetime.datetime.strptime(details[5], "%Y-%m-%d %H:%M:%S")
                now = datetime.datetime.now()
                exit_time = now.strftime("%Y-%m-%d %H:%M:%S")
                duration = now - entry_time
                minutes = int(duration.total_seconds() // 60)
                payment = calculate_payment(minutes)
                print("\n-------------------------PARKING MANAGEMENT SYSTEM--------------------------\n")
                print("           Payment Details:         ")
                print("**********************************************")
                print(f"Vehicle Plate Number: {details[0]}")
                print(f"Driver Name         : {details[1]}")
                print(f"Vehicle Name        : {details[2]}")
                print(f"Slot No             : {details[4]}")
                print(f"Entry Time          : {details[5]}")
                print(f"Exit Time           : {exit_time} ")
                print(f"Parking Duration    : {minutes} minutes")
                print(f"Amount Due          : ₹{payment:.2f}")
                print("**********************************************")
                print("\n........THANK YOU AND DRIVE SAFELY......... \n")
                found = True
                break
        if not found:
            print("Details not found.")
    print("------------------------")

while True:
    print("-------------------Parking Management System-------------------")
    print("---------------------------------------------------------------")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        if login():
            while True:
                print("        Menu:           ")
                print("------------------------")
                print("1. Insert Details")
                print("2. Search Details")
                print("3. Delete Details")
                print("4. Display All Details")
                print("5. Update Details")
                print("6. Generate Payment")
                print("7. Logout")
                print("-------------------------")
                menu_choice = input("Enter your choice: ")
                if menu_choice == "1":
                    insert_details()
                elif menu_choice == "2":
                    search_details()
                elif menu_choice == "3":
                    delete_details()
                elif menu_choice == "4":
                    display_all()
                elif menu_choice == "5":
                    update_details()
                elif menu_choice == "6":
                    generate_payment()
                elif menu_choice == "7":
                    print("Logging out...")
                    print("-"*60)
                    break
                else:
                    print("Invalid choice. Please try again.")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
