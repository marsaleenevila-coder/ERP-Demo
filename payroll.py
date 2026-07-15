import database

# -----------------------------
# Generate Payroll ID
# -----------------------------
def generate_payroll_id():

    try:
        file = open("payroll.txt", "r")

        last_id = 0

        for line in file:
            data = line.strip().split(",")
            last_id = int(data[0][1:])

        file.close()

        return f"P{last_id + 1:03d}"

    except FileNotFoundError:
        return "P001"


# -----------------------------
# Generate Payroll
# -----------------------------
def generate_payroll():

    employees = database.load_employees()

    if len(employees) == 0:
        print("No Employee Records Found.")
        return

    print("-" * 80)
    print(f"{'ID':<10}{'Name':<20}{'Department':<15}{'Salary':>10}")
    print("-" * 80)

    for emp in employees:
        print(f"{emp[0]:<10}{emp[1]:<20}{emp[2]:<15}{emp[4]:>10.2f}")

    print("-" * 80)

    emp_id = int(input("Enter Employee ID : "))

    found = False

    for emp in employees:

        if emp[0] == emp_id:

            payroll_id = generate_payroll_id()

            basic = emp[4]

            hra = float(input("Enter HRA : "))
            da = float(input("Enter DA : "))
            allowance = float(input("Enter Allowance : "))

            pf = float(input("Enter PF : "))
            esi = float(input("Enter ESI : "))
            pt = float(input("Enter Professional Tax : "))
            income_tax = float(input("Enter Income Tax : "))

            gross = basic + hra + da + allowance

            deduction = pf + esi + pt + income_tax

            net_salary = gross - deduction

            month = input("Enter Month : ")
            year = input("Enter Year : ")

            file = open("payroll.txt", "a")

            file.write(
                f"{payroll_id},{emp[0]},{emp[1]},{emp[2]},"
                f"{basic},{hra},{da},{allowance},"
                f"{gross},{pf},{esi},{pt},{income_tax},"
                f"{deduction},{net_salary},{month},{year}\n"
            )

            file.close()

            print("\nPayroll Generated Successfully.")

            found = True
            break

    if not found:
        print("Employee Not Found.")


# -----------------------------
# View Payroll
# -----------------------------
def view_payroll():

    try:

        file = open("payroll.txt", "r")

        print("-" * 120)
        print(f"{'PID':<8}{'EmpID':<8}{'Name':<15}{'Dept':<12}{'Basic':>10}{'Gross':>12}{'Deduction':>15}{'Net Salary':>15}")
        print("-" * 120)

        for line in file:

            data = line.strip().split(",")

            print(f"{data[0]:<8}{data[1]:<8}{data[2]:<15}{data[3]:<12}{float(data[4]):>10.2f}{float(data[8]):>12.2f}{float(data[13]):>15.2f}{float(data[14]):>15.2f}")

        print("-" * 120)

        file.close()

    except FileNotFoundError:

        print("No Payroll Records Found.")


# -----------------------------
# Payroll Menu
# -----------------------------
def payroll_menu():

    while True:

        print("\nPayroll Module")
        print("1. Generate Payroll")
        print("2. View Payroll")
        print("3. Search Payroll")
        print("4. Update Payroll")
        print("5. Generate Salary Slip")
        print("6. Back")

        choice = input("Enter Choice : ")

        if choice == "1":
            generate_payroll()

        elif choice == "2":
            view_payroll()

        elif choice == "3":
            search_payroll()

        elif choice == "4":
            update_payroll()

        elif choice == "5":
            salary_slip()

        elif choice == "6":
            break

        else:
            print("Invalid Choice")

def search_payroll():

    while True:

        print("\nSearch Payroll")
        print("-" * 30)
        print("1. Search by Payroll ID")
        print("2. Search by Employee ID")
        print("3. Search by Employee Name")
        print("4. Search by Month & Year")
        print("5. Back")

        choice = input("Enter Choice : ")

        if choice == "1":

            payroll_id = input("Enter Payroll ID : ").upper()

            search_file(0, payroll_id)

        elif choice == "2":

            emp_id = input("Enter Employee ID : ")

            search_file(1, emp_id)

        elif choice == "3":

            emp_name = input("Enter Employee Name : ").title()

            search_file(2, emp_name)

        elif choice == "4":

            month = input("Enter Month : ").title()
            year = input("Enter Year : ")

            search_month_year(month, year)

        elif choice == "5":

            break

        else:

            print("Invalid Choice.")

def search_file(position, value):

    found = False

    try:

        with open("payroll.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if data[position] == value:

                    display_payroll(data)

                    found = True

        if not found:
            print("Payroll Record Not Found.")

    except FileNotFoundError:

        print("Payroll File Not Found.")

def search_month_year(month, year):

    found = False

    try:

        with open("payroll.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if data[15] == month and data[16] == year:

                    display_payroll(data)

                    found = True

        if not found:

            print("Payroll Record Not Found.")

    except FileNotFoundError:

        print("Payroll File Not Found.")

def update_payroll():

    payroll_id = input("Enter Payroll ID : ").upper()

    payrolls = []

    found = False

    try:

        with open("payroll.txt", "r") as file:

            for line in file:

                payrolls.append(line.strip().split(","))

        for data in payrolls:

            if data[0] == payroll_id:

                found = True

                print("\nCurrent Payroll Details")
                print("-" * 40)
                print("Employee Name :", data[2])
                print("Basic Salary  :", data[4])

                data[5] = input("New HRA : ")
                data[6] = input("New DA : ")
                data[7] = input("New Allowance : ")

                data[9] = input("New PF : ")
                data[10] = input("New ESI : ")
                data[11] = input("New Professional Tax : ")
                data[12] = input("New Income Tax : ")

                data[15]=input("New Month :")
                data[16]=input("New Year :")

                basic = float(data[4])
                hra = float(data[5])
                da = float(data[6])
                allowance = float(data[7])

                pf = float(data[9])
                esi = float(data[10])
                pt = float(data[11])
                income_tax = float(data[12])

                month = data[15]
                year = float(data[16])

                gross = basic + hra + da + allowance
                deduction = pf + esi + pt + income_tax
                net_salary = gross - deduction

                data[8] = str(gross)
                data[13] = str(deduction)
                data[14] = str(net_salary)

                break

        if found:

            with open("payroll.txt", "w") as file:

                for record in payrolls:
                    file.write(",".join(record) + "\n")

            print("\nPayroll Updated Successfully.")

        else:

            print("Payroll ID Not Found.")

    except FileNotFoundError:

        print("Payroll File Not Found.")

def salary_slip():

    payroll_id = input("Enter Payroll ID : ").upper()

    found = False

    try:

        file = open("payroll.txt","r")

        for line in file:

            data = line.strip().split(",")

            if data[0] == payroll_id:

                found = True

                print("\n")
                print("="*60)
                print("              XYZ TECHNOLOGIES PVT LTD")
                print("                  SALARY SLIP")
                print("="*60)

                print(f"Payroll ID     : {data[0]}")
                print(f"Employee ID    : {data[1]}")
                print(f"Employee Name  : {data[2]}")
                print(f"Department     : {data[3]}")
                print(f"Month          : {data[15]}")
                print(f"Year           : {data[16]}")

                print("-"*60)

                print("EARNINGS")
                print(f"Basic Salary         : {float(data[4]):10.2f}")
                print(f"HRA                  : {float(data[5]):10.2f}")
                print(f"DA                   : {float(data[6]):10.2f}")
                print(f"Allowance            : {float(data[7]):10.2f}")

                print("-"*60)

                print(f"Gross Salary         : {float(data[8]):10.2f}")

                print("-"*60)

                print("DEDUCTIONS")
                print(f"PF                   : {float(data[9]):10.2f}")
                print(f"ESI                  : {float(data[10]):10.2f}")
                print(f"Professional Tax     : {float(data[11]):10.2f}")
                print(f"Income Tax           : {float(data[12]):10.2f}")

                print("-"*60)

                print(f"Total Deduction      : {float(data[13]):10.2f}")

                print("="*60)

                print(f"NET SALARY           : {float(data[14]):10.2f}")

                print("="*60)

                break

        file.close()

        if not found:

            print("Payroll Record Not Found.")

    except FileNotFoundError:

        print("Payroll File Not Found.")

def display_payroll(data):

    print("-" * 60)

    print("Payroll ID        :", data[0])
    print("Employee ID       :", data[1])
    print("Employee Name     :", data[2])
    print("Department        :", data[3])
    print("Basic Salary      :", data[4])
    print("HRA               :", data[5])
    print("DA                :", data[6])
    print("Allowance         :", data[7])
    print("Gross Salary      :", data[8])
    print("PF                :", data[9])
    print("ESI               :", data[10])
    print("Professional Tax  :", data[11])
    print("Income Tax        :", data[12])
    print("Total Deduction   :", data[13])
    print("Net Salary        :", data[14])
    print("Month             :", data[15])
    print("Year              :", data[16])

    print("-" * 60)

