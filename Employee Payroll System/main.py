from tabulate import tabulate
from pwinput import pwinput
from FileHandler import *
from os import system
import platform

employees:list = loadEmployees()
positions:list = loadPositions()
payroll:list = loadPayroll()

def main():
    option:int = 5
    if(login()):
        while(option != 0):
            mainMenu()
            try:
                option = int(input("\nEnter option(0...4): "))
                menuOption(option)
            except:
                print("\nInvalid Input!")
            finally:
                input("\nPress any key to continue...")
    else: print("\nInvalid User!\n\nProgram Terminated")


def mainMenu()->None:
    clearScreen()
    print(tabulate([["Main Menu"],["1. Find Employee"],["2. Display All Employee"],["3. Add number of day(s) worked"],["4. Generate Payroll"],["0. Quit"]],colalign=("center",),tablefmt="rounded_grid"))

def findEmployee()->None:
    clearScreen()
    print(tabulate([["Find Employee"]],tablefmt="rounded_grid"))
    id:list = exist(input("\nEnter employee ID to find: "))

    if(id): print(f"\n{tabulate([id[0][:3] + id[0][5::2]],headers=['ID','Firstname','Lastname','Position','Salary'],numalign='center',stralign='center',tablefmt='rounded_grid')}")
    else: print("\nEmployee does not exist.")

def exist(id:str)->bool: # checks if an id exists with the parameter string id
    for employee in employees:
        for position in positions:
            if(employee[0] == id and (employee[len(employee)-1] == position[0])):
                return [employee+position] # returns the current employee and position
    return False

def displayEmployees()->None:
    clearScreen()
    print(tabulate([["List of Employees"]],tablefmt="rounded_grid"))
    table:list = []

    for employee in employees:
        for position in positions: # iterates through employees and positions
            if(employee[len(employee)-1] == position[0]): # checks if current employee position code matches the given list of positions' code
                table.append(employee[:len(employee)-1] + position[1:])

    print(tabulate(table,headers=["ID","Firstname","Lastname","Position","PosNo","Salary"],numalign="center",stralign="center",tablefmt="rounded_grid")) # displays the list of employees in a table format

def addDaysWorked()->None:
    clearScreen()
    print(tabulate([["Add Worked Day(s)"]],tablefmt="rounded_grid"))
    id:list = exist(input("\nIDNO: "))

    if(id):
        print(f"\n{tabulate([id[0][:3] + id[0][5:]],headers=['ID','Firstname','Lastname','Position','PosNo','Salary'],numalign='center',stralign='center',tablefmt='rounded_grid')}")

        daysWorked:int = int(input("\nEnter Day(s) Worked: "))
        totalSalary:float = float(id[0][len(id[0])-1]) * daysWorked # takes salary index from current position of the list
        
        print(f"\n{tabulate([['Total Salary','{:,}'.format(totalSalary)]],numalign='center',stralign='center',tablefmt='rounded_grid')}")
        id[0][len(id[0])-1] = '{:,}'.format(totalSalary)

        payroll.append(' '.join(id[0][:3]+id[0][5:])) # appends temporary employee to the global variable payroll

def generatePayroll()->None:
    clearScreen()
    print(tabulate([["Generate Payroll"]],tablefmt="rounded_grid"))
    temp:list = []
    [temp.append(str(item).split(" ")) for item in payroll]
    print(tabulate(temp,headers=["ID","Firstname","Lastname","Position","PosNo","Salary"],numalign='center',stralign='center',tablefmt="rounded_grid"))
    savePayroll(payroll)

def menuOption(option:int)->None:
    options={
        1:findEmployee,
        2:displayEmployees,
        3:addDaysWorked,
        4:generatePayroll,
        0:closeProgram
    }
    return options.get(option)()

def closeProgram()->bool:
    print("\nProgram Terminated")
    return False

def clearScreen()->None:
    if(platform.system() == "Windows"): system("cls")
    else: system("clear")

def login()->bool:
    clearScreen()
    print(tabulate([["Login"]],tablefmt="rounded_grid"))
    username:str = input("username: ")
    password:str = pwinput(prompt="password: ", mask="*")
    if username == "admin" and password == "user": return True
    return False

if __name__ == "__main__": main()