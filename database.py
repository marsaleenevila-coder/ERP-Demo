import csv

employees = []
departments = []
attendance = []
leave = []
payroll = []

FILE_NAME = "employees.txt"

def load_employees():

    employees = []

    try:

        with open(FILE_NAME, "r") as file:

            reader = csv.reader(file)

            for row in reader:

                row[0] = int(row[0])
                row[4] = float(row[4])

                employees.append(row)

    except FileNotFoundError:

        pass

    return employees

def generate_employee_id():

    employees = load_employees()

    if len(employees) == 0:
        return 101

    return employees[-1][0] + 1

def save_employee(employee):

    #file = open(FILE_NAME, "a")

    #file.write(",".join(map(str, employee)) + "\n")

    #file.close()
    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(employee)

FILE_NAME = "employees.txt"

def save_all(employees):

    #file = open(FILE_NAME, "w")

    #for emp in employees:

        #file.write(",".join(map(str, emp)) + "\n")

    #file.close()
    with open(FILE_NAME, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerows(employees)

        

def get_all_employees():

    employees = []

    try:
        file = open(FILE_NAME, "r")

        for line in file:

            line = line.strip()

            if line:

                emp = line.split(",")

                emp[0] = int(emp[0])
                emp[4] = float(emp[4])

                employees.append(emp)

        file.close()

    except FileNotFoundError:

        pass

    return employees