import employee
import department
import payroll
import attendance
import leave

while True:
    print("\n===== ERP SYSTEM =====")
    print("1. Employee")
    print("2. Department")
    print("3. Payroll")
    print("4. Attendance")
    print("5. Leave")
    print("6. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        employee.employee_menu()

    elif choice == "2":
        department.department_menu()

    elif choice == "3":
        payroll.payroll_menu()

    elif choice == "4":
        attendance.attendance_menu()

    elif choice == "5":
        leave.leave_menu()

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")

def attendance_report():

    emp_id = input("Enter Employee ID : ")

    month = input("Enter Month (MM) : ")

    year = input("Enter Year (YYYY) : ")

    present = 0
    absent = 0
    leave = 0
    halfday = 0
    wfh = 0

    employee_name = ""
    department = ""

    try:

        file = open("attendance.txt", "r")

        for line in file:

            data = line.strip().split(",")

            # Skip deleted records
            if len(data) >= 9 and data[8] == "Deleted":
                continue

            if data[1] == emp_id:

                date = data[4]

                day, mon, yr = date.split("-")

                if mon == month and yr == year:

                    employee_name = data[2]
                    department = data[3]

                    if data[5] == "Present":
                        present += 1

                    elif data[5] == "Absent":
                        absent += 1

                    elif data[5] == "Leave":
                        leave += 1

                    elif data[5] == "Half Day":
                        halfday += 1

                    elif data[5] == "WFH":
                        wfh += 1

        file.close()

        total = present + absent + leave + halfday + wfh

        if total == 0:

            print("No Attendance Records Found.")
            return

        attendance_percentage = (
            (present + wfh + (halfday * 0.5)) / total
        ) * 100

        print("\n")
        print("=" * 55)
        print("           ATTENDANCE REPORT")
        print("=" * 55)

        print("Employee ID      :", emp_id)
        print("Employee Name    :", employee_name)
        print("Department       :", department)
        print("Month / Year     :", month, "/", year)

        print("-" * 55)

        print(f"Present Days     : {present}")
        print(f"Absent Days      : {absent}")
        print(f"Leave Days       : {leave}")
        print(f"Half Days        : {halfday}")
        print(f"WFH Days         : {wfh}")

        print("-" * 55)

        print(f"Working Days     : {total}")
        print(f"Attendance %     : {attendance_percentage:.2f}%")

        print("=" * 55)

    except FileNotFoundError:

        print("Attendance File Not Found.")