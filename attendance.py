import database

def attendance_menu():

    while True:

        print("\nAttendance Module")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Search Attendance")
        print("4. Update Attendance")
        print("5. Delete Attendance")
        print("6. Attendance Report")
        print("7. Back")

        choice = input("Enter Choice : ")

        if choice == "1":
            mark_attendance()

        elif choice == "2":
            view_attendance()

        elif choice == "3":
            search_attendance()

        elif choice == "4":
            update_attendance()

        elif choice == "5":
            delete_attendance()

        elif choice == "6":
            attendance_report()

        elif choice == "7":
            break

        else:
            print("Invalid Choice")

def generate_attendance_id():

    try:

        file = open("attendance.txt","r")

        last_id = 0

        for line in file:

            data = line.strip().split(",")

            last_id = int(data[0][1:])

        file.close()

        return f"A{last_id+1:03d}"

    except FileNotFoundError:

        return "A001"
    
from datetime import datetime

def mark_attendance():

    employees = database.load_employees()

    if len(employees) == 0:

        print("No Employee Records Found.")
        return

    print("-"*70)
    print(f"{'ID':<10}{'Name':<20}{'Department':<15}")
    print("-"*70)

    for emp in employees:

        print(f"{emp[0]:<10}{emp[1]:<20}{emp[2]:<15}")

    print("-"*70)

    emp_id = int(input("Enter Employee ID : "))

    found = False

    for emp in employees:

        if emp[0] == emp_id:

            attendance_id = generate_attendance_id()

            date = input("Enter Date (DD-MM-YYYY): ")

            print("\nAttendance Status")
            print("1.Present")
            print("2.Absent")
            print("3.Leave")
            print("4.Half Day")
            print("5.Work From Home")

            option = input("Enter Choice : ")

            if option=="1":
                status="Present"
            elif option=="2":
                status="Absent"
            elif option=="3":
                status="Leave"
            elif option=="4":
                status="Half Day"
            elif option=="5":
                status="WFH"
            else:
                print("Invalid Status")
                return

            if status=="Present" or status=="WFH" or status=="Half Day":

                check_in=input("Check In Time : ")
                check_out=input("Check Out Time : ")

            else:

                check_in="-"
                check_out="-"

            file=open("attendance.txt","a")

            file.write(f"{attendance_id},{emp[0]},{emp[1]},{emp[2]},{date},{status},{check_in},{check_out}\n")

            file.close()

            print("Attendance Marked Successfully.")

            found=True

            break

    if not found:

        print("Employee Not Found.")

def view_attendance():

    try:

        file = open("attendance.txt", "r")

        print("-" * 110)
        print(f"{'Att ID':<10}{'Emp ID':<10}{'Employee Name':<20}{'Department':<15}{'Date':<15}{'Status':<15}{'In':<10}{'Out':<10}")
        print("-" * 110)

        for line in file:

            data = line.strip().split(",")

            print(f"{data[0]:<10}{data[1]:<10}{data[2]:<20}{data[3]:<15}{data[4]:<15}{data[5]:<15}{data[6]:<10}{data[7]:<10}")

        print("-" * 110)

        file.close()

    except FileNotFoundError:

        print("Attendance Records Not Found.")

def search_attendance():

    while True:

        print("\nSearch Attendance")
        print("1. Attendance ID")
        print("2. Employee ID")
        print("3. Employee Name")
        print("4. Date")
        print("5. Status")
        print("6. Back")

        choice = input("Enter Choice : ")

        if choice == "1":

            value = input("Enter Attendance ID : ").upper()
            search_file(0, value)

        elif choice == "2":

            value = input("Enter Employee ID : ")
            search_file(1, value)

        elif choice == "3":

            value = input("Enter Employee Name : ").title()
            search_file(2, value)

        elif choice == "4":

            value = input("Enter Date (DD-MM-YYYY): ")
            search_file(4, value)

        elif choice == "5":

            value = input("Enter Status : ").title()
            search_file(5, value)

        elif choice == "6":

            break

        else:

            print("Invalid Choice.")

def search_file(position, value):

    found = False

    try:

        file = open("attendance.txt", "r")

        print("-"*110)
        print(f"{'Att ID':<10}{'Emp ID':<10}{'Name':<20}{'Department':<15}{'Date':<15}{'Status':<15}{'In':<10}{'Out':<10}")
        print("-"*110)

        for line in file:

            data = line.strip().split(",")

            if data[8] == "Deleted":
                continue

            if data[position] == value:

                print(f"{data[0]:<10}{data[1]:<10}{data[2]:<20}{data[3]:<15}{data[4]:<15}{data[5]:<15}{data[6]:<10}{data[7]:<10}")

                found = True

        print("-"*110)

        file.close()

        if not found:

            print("Attendance Record Not Found.")

    except FileNotFoundError:

        print("Attendance File Not Found.")

def update_attendance():

    att_id = input("Enter Attendance ID : ").upper()

    records = []

    found = False

    try:

        file = open("attendance.txt", "r")

        for line in file:

            records.append(line.strip().split(","))

        file.close()

        for record in records:

            if record[0] == att_id:

                if record[8] == "Deleted":

                    print("Attendance Record has been deleted.")
                    return

                found = True

                print("\nCurrent Attendance Details")
                print("-"*50)

                print("Attendance ID :", record[0])
                print("Employee ID   :", record[1])
                print("Employee Name :", record[2])
                print("Department    :", record[3])
                print("Date          :", record[4])
                print("Status        :", record[5])
                print("Check In      :", record[6])
                print("Check Out     :", record[7])

                print("\nPress Enter to keep existing value.")

                new_date = input(f"Date ({record[4]}) : ")

                if new_date != "":
                    record[4] = new_date

                print("\nAttendance Status")
                print("1.Present")
                print("2.Absent")
                print("3.Leave")
                print("4.Half Day")
                print("5.Work From Home")

                option = input(f"Choice ({record[5]}) : ")

                if option == "":
                    status = record[5]

                elif option == "1":
                    status = "Present"

                elif option == "2":
                    status = "Absent"

                elif option == "3":
                    status = "Leave"

                elif option == "4":
                    status = "Half Day"

                elif option == "5":
                    status = "WFH"

                else:

                    print("Invalid Choice")
                    return

                record[5] = status

                if status in ["Present", "Half Day", "WFH"]:

                    checkin = input(f"Check In ({record[6]}) : ")

                    if checkin != "":
                        record[6] = checkin

                    checkout = input(f"Check Out ({record[7]}) : ")

                    if checkout != "":
                        record[7] = checkout

                else:

                    record[6] = "-"
                    record[7] = "-"

                break

        if found:

            file = open("attendance.txt", "w")

            for rec in records:

                file.write(",".join(rec) + "\n")

            file.close()

            print("\nAttendance Updated Successfully.")

        else:

            print("Attendance ID Not Found.")

    except FileNotFoundError:

        print("Attendance File Not Found.")

def delete_attendance():

    att_id = input("Enter Attendance ID : ").upper()

    records = []

    found = False

    try:

        file = open("attendance.txt", "r")

        for line in file:

            records.append(line.strip().split(","))

        file.close()

        for record in records:

            if record[0] == att_id:

                if record[8] == "Deleted":

                    print("Attendance Record Already Deleted.")
                    return

                print("\nAttendance Details")
                print("-"*40)

                print("Attendance ID :", record[0])
                print("Employee Name :", record[2])
                print("Date          :", record[4])
                print("Status        :", record[5])

                print("-"*40)

                confirm = input("Delete this record (Y/N)? ").upper()

                if confirm == "Y":

                    record[8] = "Deleted"

                    found = True

                    break

                else:

                    print("Delete Cancelled.")
                    return

        if found:

            file = open("attendance.txt", "w")

            for rec in records:

                file.write(",".join(rec) + "\n")

            file.close()

            print("Attendance Deleted Successfully.")

        else:

            print("Attendance ID Not Found.")

    except FileNotFoundError:

        print("Attendance File Not Found.")