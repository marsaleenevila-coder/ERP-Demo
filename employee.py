import database

employees = database.get_all_employees()
employees=database.load_employees()

#employees = []

def add_employee():

    emp_id = database.generate_employee_id()

    print("Employee ID :", emp_id)

    name = input("Enter Employee Name : ")

    departments = load_departments()

    if len(departments) == 0:
        print("No departments available.")
        return

    print("\nAvailable Departments")
    print("-" * 35)
    print(f"{'No':<5}{'Dept ID':<10}{'Department'}")
    print("-" * 35)

    for i, dept in enumerate(departments, start=1):
        print(f"{i:<5}{dept[0]:<10}{dept[1]}")

    print("-" * 35)

    while True:

        try:

            choice = int(input("Enter Department Number : "))

            if choice < 1 or choice > len(departments):
                raise ValueError("Invalid Department Number")

            department = departments[choice - 1][1]   # Department Name
            break

        except ValueError as e:
            print(e)

    designation = input("Enter Designation : ")
    salary = float(input("Enter Salary : "))

    employee = [emp_id, name, department, designation, salary]

    database.save_employee(employee)
    
    print("\nEmployee Added Successfully.")

    

def view_employee():
    #print("View Employee")
    try:

        file = open("employees.txt", "r")

        print("-" * 80)
        print(f"{'ID':<10}{'Name':<20}{'Department':<15}{'Designation':<20}{'Salary':>10}")
        print("-" * 80)

        for line in file:

            data = line.strip().split(",")

            print(f"{data[0]:<10}{data[1]:<20}{data[2]:<15}{data[3]:<20}{float(data[4]):>10.2f}")

        print("-" * 80)

        file.close()

    except FileNotFoundError:

        print("No Employee Records Found.")

    

def search_employee():
    #print("Search Employee")
    employees = database.load_employees()
     
    emp_id = int(input("Enter Employee ID to Search: "))

    found = False

    for emp in employees:

        if emp[0] == emp_id:

            print("\nEmployee Found")
            print("-" * 70)
            print(f"ID          : {emp[0]}")
            print(f"Name        : {emp[1]}")
            print(f"Department  : {emp[2]}")
            print(f"Designation : {emp[3]}")
            print(f"Salary      : {emp[4]:.2f}")

            found = True
            break

    if not found:
        print("Employee Not Found.")

def update_employee():
    #print("Update Employee")
    employees = database.load_employees()

    emp_id = int(input("Enter Employee ID to Update: "))

    found = False

    for emp in employees:

        if emp[0] == emp_id:

            print("\nCurrent Details")
            print(emp)

            emp[1] = input("Enter New Name        : ")
            emp[2] = input("Enter New Department  : ")
            emp[3] = input("Enter New Designation : ")
            #emp[4] = float(input("Enter New Salary      : "))
            emp[4] = float(input("New Salary : "))

            database.save_all(employees)

            print("Employee Updated Successfully.")

            found = True
            break

    if not found:
        print("Employee Not Found.")

def delete_employee():

    employees = database.load_employees()

    emp_id = int(input("Enter Employee ID to Delete: "))

    found = False

    for emp in employees:

        if emp[0] == emp_id:

            employees.remove(emp)

            database.save_all(employees)

            print("Employee Deleted Successfully.")

            found = True
            break

    if not found:
        print("Employee Not Found.")

def employee_menu():

    while True:

        print("\nEmployee Module")
        print("1.Add")
        print("2.View")
        print("3.Search")
        print("4.Update")
        print("5.Delete")
        print("6.Back")

        choice = input("Enter Choice : ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employee()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            break

        else:
            print("Invalid Choice")

def load_departments():

    departments = []

    try:
        with open("department.txt", "r") as file:

            for line in file:
                dept_id, dept_name = line.strip().split(",")
                departments.append([dept_id, dept_name])

    except FileNotFoundError:
        print("Department file not found.")

    return departments
