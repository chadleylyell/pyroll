import time
import os
import platform

print("System version " + str(platform.python_version()))

login = False
admin = False

pins = os.listdir("/Users/lbattaglioli/PycharmProjects/PyPay/employees")
pin_in = input("Enter your employee PIN: ")


def first_login():
    if login:
        employeeID = pin_in
        timeCardPath = "/Users/lbattaglioli/PycharmProjects/PyPay/employees/" + employeeID + ".txt"
        with open(timeCardPath, "r") as timeCard:
            name = timeCard.readline().rstrip()
        print("Hello, " + name + ". Please select one of the options.")
        print("1. Clock In\n2. Clock Out\n3. View Time Card\n4. Logoff")
        option = int(input("> "))
        if option == 1:
            clock_in()
        if option == 2:
            clock_out()
        if option == 3:
            view_hours()
        if option == 4:
            logoff()


def login_script():
    if login:
        print("Please select one of the options.")
        print("1. Clock In\n2. Clock Out\n3. View Time Card\n4. Logoff")
        option = int(input("> "))
        if option == 1:
            clock_in()
        if option == 2:
            clock_out()
        if option == 3:
            view_hours()
        if option == 4:
            logoff()


def view_hours():
    if login:
        employeeID = pin_in
        found = False
        for pin in pins:
            if employeeID + ".txt" == pin:
                timeCardPath = "/Users/lbattaglioli/PycharmProjects/PyPay/employees/" + employeeID + ".txt"
                found = True
                timeCard = open(timeCardPath, mode="r")
                print("Here's your time card " + str(timeCard.readline().rstrip()) + ".")
                print(timeCard.read())
        if not found:
            print("We're sorry, you're information could not be accessed.")


def clock_in():
    date = time.ctime()
    if login:
        employeeID = pin_in
        found = False
        for pin in pins:
            if employeeID + ".txt" == pin:
                timeCardPath = "/Users/lbattaglioli/PycharmProjects/PyPay/employees/" + employeeID + ".txt"
                found = True
                timeCard = open(timeCardPath, mode="a")
                print("You've successfully clocked in on: " + str(date))
                timeCard.write("in: " + date + "\n")

        if not found:
            print("We're sorry, an error occurred. Please contact HR.")


def clock_out():
    date = time.ctime()
    if login:
        employeeID = pin_in
        found = False
        for pin in pins:
            if employeeID + ".txt" == pin:
                timeCardPath = "/Users/lbattaglioli/PycharmProjects/PyPay/employees/" + employeeID + ".txt"
                found = True
                timeCard = open(timeCardPath, mode="a")
                print("You've successfully clocked out on: " + str(date))
                timeCard.write("out: " + date + "\n")
                timeCard.write("-------------------------\n")

        if not found:
            print("We're sorry, an error occurred. Please contact HR.")


def admin_script():
    if admin:
        print("Welcome admin. Would you like to view an employee time card? Y/N")
        option = input("> ").upper()
        
        if option == "N":
            print("Logging off system.")
        while option == "Y":
            employeeID = input("Enter the employee ID: ")
            found = False
            for pin in pins:
                if employeeID + ".txt" == pin:
                    timeCardPath = "/Users/lbattaglioli/PycharmProjects/PyPay/employees/" + employeeID + ".txt"
                    found = True
                    timeCard = open(timeCardPath, mode="r")
                    print(timeCard.read())
            if not found:
                print("No employee with that ID.")
    
            print("Do you want to view another time card? Y/N")
            proceed = input("> ").upper()
            if proceed == "N":
                print("Logging off system.")
                break


def logoff():
    employeeID = pin_in
    timeCardPath = "/Users/lbattaglioli/PycharmProjects/PyPay/employees/" + employeeID + ".txt"
    with open(timeCardPath, "r") as timeCard:
        name = timeCard.readline().rstrip()
    print("Goodbye, " + name + ".")


if pin_in == "admin3023":
        admin = True
        admin_script()
while not admin:
    found = False
    for pin in pins:
        if pin_in + ".txt" == pin:
            login = True
            found = True
    if found == True:
        first_login()
        break
    if not found:
        pin_in = input("Employee ID not valid. Enter your employee PIN: ")

#   valid: 
#       clock in or out
#   invalid: 
#       reenter pin
