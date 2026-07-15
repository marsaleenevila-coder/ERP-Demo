# =====================================
# ERP - Leave Management System
# =====================================

leaves = []


# -------------------------------------
# Apply Leave
# -------------------------------------

def apply_leave():

    leave = {}

    leave["leave_id"] = int(input("Enter Leave ID : "))

    leave["emp_id"] = int(input("Enter Employee ID : "))

    leave["employee_name"] = input("Enter Employee Name : ")

    leave["leave_type"] = input(
        "Enter Leave Type (Casual/Sick/Earned): "
    )

    leave["from_date"] = input("From Date : ")

    leave["to_date"] = input("To Date : ")

    leave["days"] = int(input("Number of Days : "))

    leave["reason"] = input("Reason : ")

    leave["status"] = "Pending"


    leaves.append(leave)


    print("\nLeave Applied Successfully")



# -------------------------------------
# View Leave
# -------------------------------------

def view_leave():

    if len(leaves) == 0:

        print("\nNo Leave Records Found")
        return


    print("\nLeave Details")

    print("-"*100)

    print(
        "ID\tEmp ID\tName\tType\tFrom\tTo\tDays\tStatus"
    )

    print("-"*100)


    for leave in leaves:

        print(
            leave["leave_id"],
            leave["emp_id"],
            leave["employee_name"],
            leave["leave_type"],
            leave["from_date"],
            leave["to_date"],
            leave["days"],
            leave["status"],
            sep="\t"
        )



# -------------------------------------
# Search Leave
# -------------------------------------

def search_leave():

    emp_id = int(input("\nEnter Employee ID : "))


    for leave in leaves:

        if leave["emp_id"] == emp_id:

            print("\nLeave Found")

            print(leave)

            return


    print("\nLeave Record Not Found")



# -------------------------------------
# Update Leave
# -------------------------------------

def update_leave():

    leave_id = int(input("\nEnter Leave ID : "))


    for leave in leaves:


        if leave["leave_id"] == leave_id:


            print("\nLeave Found")


            leave["leave_type"] = input(
                "New Leave Type : "
            )


            leave["from_date"] = input(
                "New From Date : "
            )


            leave["to_date"] = input(
                "New To Date : "
            )


            leave["days"] = int(
                input("New Days : ")
            )


            leave["reason"] = input(
                "New Reason : "
            )


            print("\nLeave Updated Successfully")

            return



    print("\nLeave Not Found")



# -------------------------------------
# Delete Leave
# -------------------------------------

def delete_leave():

    leave_id = int(input("\nEnter Leave ID : "))


    for leave in leaves:


        if leave["leave_id"] == leave_id:


            leaves.remove(leave)


            print("\nLeave Deleted Successfully")

            return



    print("\nLeave Not Found")



# -------------------------------------
# Approve / Reject Leave
# -------------------------------------

def update_leave_status():


    leave_id = int(input("\nEnter Leave ID : "))


    for leave in leaves:


        if leave["leave_id"] == leave_id:


            print("\n1. Approve")

            print("2. Reject")


            choice = int(input("Choice : "))


            if choice == 1:

                leave["status"] = "Approved"


            elif choice == 2:

                leave["status"] = "Rejected"


            else:

                print("Invalid Choice")

                return


            print("\nLeave Status Updated")

            return



    print("\nLeave Not Found")



# -------------------------------------
# Leave Menu
# -------------------------------------

while True:


    print("\n========== LEAVE MANAGEMENT ==========")


    print("1. Apply Leave")

    print("2. View Leave")

    print("3. Search Leave")

    print("4. Update Leave")

    print("5. Delete Leave")

    print("6. Approve / Reject Leave")

    print("7. Exit")


    choice = int(input("Enter Choice : "))


    if choice == 1:

        apply_leave()


    elif choice == 2:

        view_leave()


    elif choice == 3:

        search_leave()


    elif choice == 4:

        update_leave()


    elif choice == 5:

        delete_leave()


    elif choice == 6:

        update_leave_status()


    elif choice == 7:

        print("Exit Leave Module")

        break


    else:

        print("Invalid Choice")