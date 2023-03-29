from Person import Person
from Student import Student
from pwinput import pwinput
from FileHandler import *
from os import system
import platform

students:list = loadFile()

def main():
    option:int = 5
    if(login()):
        while(option != 0):
            mainMenu()
            try:
                option = int(input("Enter option(0...4): "))
                menuOption(option)
            except:
                print("\nInvalid Input!")
            finally:
                input("\nPress any key to continue...")
    else: print("\nInvalid User!\n\nProgram Terminated")


def mainMenu()->None:
    clearScreen()
    menu:tuple = (
        "---- Main Menu ----",
        "1. Add Student",
        "2. Find Student",
        "3. Delete Student",
        "4. Display Students",
        "5. Save Progress",
        "0. Quit",
        "-------------------"
    )
    [print(item) for item in menu]

def addStudent()->None:
    clearScreen()
    print("Add Student\n-----------")
    idno = input("IDNO: ")
    lastname = input("LASTNAME: ")
    firstname = input("FIRSTNAME: ")
    course = input("COURSE: ")
    level = input("LEVEL: ")
    students.append(Student(idno,firstname.capitalize(),lastname.capitalize(),course.upper(),level))

def findStudent()->None:
    id:str = input("\nEnter student ID to find: ")
    if(exist(id)): print(f"\nStudent {exist(id)} found")
    else: print("\nStudent does not exist.")

def deleteStudent()->None:
    clearScreen()
    print("Delete Student\n--------------")
    id:str = input("Student to remove(ID): ")
    prompt:str = input("Do you really want to remove this student(y/n)? ")
    if(prompt.lower() == "y"):
        print(f"\nStudent {(exist(id))} removed")
        students.remove(exist(id))

def showStudents()->None:
    clearScreen()
    print("Student List\n------------")
    [print(student) for student in students]

def menuOption(option:int)->None:
    options={
        1:addStudent,
        2:findStudent,
        3:deleteStudent,
        4:showStudents,
        5:saveStudents,
        0:closeProgram
    }
    return options.get(option)()

def saveStudents()->None:
    saveFile(students)
    print("\nFiles Saved.")

def closeProgram()->None:
    print("\nProgram Terminated")
    return False

def exist(id:str)->bool:
    for student in students:
        if(student.id == id):
            return student
    return False

def clearScreen():
    if(platform.system() == "Windows"): system("cls")
    else: system("clear")

def login()->bool:
    clearScreen()
    username:str = input("username: ")
    password:str = pwinput(prompt="password: ", mask="*")
    if username == "admin" and password == "user": return True
    return False

if __name__ == "__main__": main()