from mysql.connector import connect
from tabulate import tabulate
from Student import Student
from pwinput import pwinput
from os import system
import platform
from dbhelper import *
from user_model import *

pythondb = connect (
    host="localhost",
    user="gochuicod",
    password="20259388",
    database="pythondb"
)

def main()->None:
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
    print(tabulate([["Main Menu"],["1. Add Student"],["2. Find Student"],["3. Update Student"],["4. Delete Student"],["5. Display Students"],["0. Quit"]],colalign=("center",),tablefmt="rounded_grid"))

def menuOption(option:int)->None:
    options={
        1:add,
        2:find,
        3:update,
        4:delete,
        5:show,
        0:closeProgram
    }
    return options.get(option)()  

def add()->None:
    clearScreen()
    print(tabulate([["Add Student"]],tablefmt="rounded_grid"))
    student = Student (
        input("\nStudent ID: "),
        input("Firstname: "),
        input("Lastname: "),
        input("Course: "),
        input("Level: ")
    )
    addStudent (
        student_id=student.getStudentID(),
        firstname=student.getFirstname(),
        lastname=student.getLastname(),
        course=student.getCourse(),
        level=student.getLevel()
    )
    print("\nStudent Added.")

def find()->None:
    clearScreen()
    print(tabulate([["Find Student"]],tablefmt="rounded_grid"))
    student = findStudent(student_id=input("\nEnter Student ID: ").title())
    if student: print("\n"+tabulate(student,tablefmt="rounded_grid",colalign=("center",)*len(student)))
    else: print("\nStudent not found.")

def update()->None:
    clearScreen()
    print(tabulate([["Update Student"]],tablefmt="rounded_grid"))
    student_id = input("\nEnter Student ID: ")
    student = findStudent(student_id=student_id)
    if student:
        print("\n"+tabulate(student,tablefmt="rounded_grid",colalign=("center",)*len(student)))
        updateStudent(
            student_id=student_id,
            firstname=input("\nFirstname: ").title(),
            lastname=input("Lastname: ").title(),
            course=input("Course: ").upper(),
            level=input("Level: ")
        )
        print("\nStudent updated.")
    else: print("\nStudent not found.")
    

def delete()->None:
    clearScreen()
    print(tabulate([["Delete Student"]],tablefmt="rounded_grid"))
    student_id = input("\nEnter Student ID: ")
    student = findStudent(student_id=student_id)
    print("\n"+tabulate(student,tablefmt="rounded_grid",colalign=("center",)*len(student)))
    prompt = input("\nAre you sure you want to delete this student? (yes/no): ").lower()
    if prompt == "yes" or prompt == "y":
        deleteStudent(student_id=student_id)
        print("\nStudent Deleted.")

def show()->None:
    clearScreen()
    print(tabulate([["Student List"]],tablefmt="rounded_grid"))
    headers=["Student ID","Firstname","Lastname","Course","Level"]
    print(tabulate(getAllStudents(),headers=headers,tablefmt="rounded_grid",colalign=("center",)*len(headers)))

def closeProgram()->bool:
    print("\nProgram Terminated")
    return False

def clearScreen()->None:
    if(platform.system() == "Windows"): system("cls")
    else: system("clear")

def login()->bool:
    clearScreen()
    username:str = input("username: ")
    password:str = pwinput(prompt="password: ", mask="*")
    if username == "admin" and password == "user": return True
    return False

if __name__ == '__main__': main()