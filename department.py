import csv

departments = []

def add_department():

    dept_id = input("Enter Department ID (Example: D001): ").upper()
    dept_name = input("Enter Department Name: ").title().upper()

    # Check if Department ID already exists
    try:
        with open("department.txt", "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if row and row[0] == dept_id:
                    print("Department ID already exists.")
                    return

    except FileNotFoundError:
        pass

    # Save Department
    with open("department.txt", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([dept_id, dept_name])

    print("Department Added Successfully.")

def view_department():

    try:
        with open("department.txt", "r", newline="") as file:

            reader = csv.reader(file)

            print("-" * 40)
            print(f"{'Dept ID':<15}{'Department Name'}")
            print("-" * 40)

            for row in reader:
                print(f"{row[0]:<15}{row[1]}")

            print("-" * 40)

    except FileNotFoundError:
        print("No Departments Found.")

def department_menu():

    while True:

        print("\nDepartment Module")
        print("1.Add Department")
        print("2.View Department")
        print("3.Back")

        choice = input("Enter Choice : ")

        if choice=="1":
            add_department()

        elif choice=="2":
            view_department()

        elif choice=="3":
            break

        else:
           print("Invalid Choice.")

