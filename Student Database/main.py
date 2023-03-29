from mysql.connector import errorcode
import platform, mysql.connector
from tabulate import tabulate
from pwinput import pwinput
from os import system

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
        1:addStudent,
        2:findStudent,
        3:updateStudent,
        4:deleteStudent,
        5:showStudents,
        0:closeProgram
    }
    return options.get(option)()

def addStudent()->None:
    clearScreen()
    print(tabulate([["Add Student"]],tablefmt="rounded_grid"))
    try:
        values = (
            input("\nFirstname: ").title(),
            input("Lastname: ").title(),
            input("Course: ").upper(),
            input("Level: ")
        )
        cursor.execute("insert into students (firstname,lastname,course,level) values (%s,%s,%s,%s)",values)
        pythondb.commit()
        print("\nStudent added.")
    except: print("\nData exceeds number of characters")

def findStudent()->None:
    clearScreen()
    print(tabulate([["Find Student"]],tablefmt="rounded_grid"))
    try:
        id:int = int(input("\nEnter ID: "))
        print(f"\n{tabulate([str(exist(id)).split()],tablefmt='rounded_grid')}")
    except: print("\nStudent doesn't exist")

def updateStudent()->None:
    clearScreen()
    print(tabulate([["Update Student"]],tablefmt="rounded_grid"))
    try:
        id:int = int(input("\nStudent ID: "))
        if(exist(id)):
            print(f"\n{tabulate([str(exist(id)).split()],tablefmt='rounded_grid')}")
            values = (
                input("\nFirstname: ").title(),
                input("Lastname: ").title(),
                input("Course: ").upper(),
                input("Level: ")
            )
            cursor.execute(f"update students set firstname='{values[0]}', lastname='{values[1]}', course='{values[2]}', level='{values[3]}' where id={id}")
            pythondb.commit()
            print("\nStudent updated.")
    except: print("\nInput(s) do not suffice the conditions.")

def deleteStudent()->None:
    clearScreen()
    print(tabulate([["Delete Student"]],tablefmt="rounded_grid"))
    id:int = int(input("\nEnter ID: "))
    try:
        print(f"\n{tabulate([exist(id).split()],tablefmt='rounded_grid')}")
        sql = f"delete from students where id = '{id}'"
        cursor.execute(sql)
        pythondb.commit()
    except: print("\nStudent doesn't exist")

def exist(id:int)->None:
    sql = f"select * from students where id = '{id}'"
    cursor.execute(sql)
    return ' '.join(map(str,cursor.fetchall()[0]))

def showStudents()->None:
    clearScreen()
    print(tabulate([["Student List"]],tablefmt="rounded_grid"))
    cursor.execute("select * from students")
    result = cursor.fetchall()
    temp:list = []
    if(len(result) != 0):
        [temp.append(list(item)) for item in result]
        print(tabulate(temp,headers=["ID","Firstname","Lastname","Course","Level"],colalign=("center",),tablefmt="rounded_grid"))
    else: cursor.execute("truncate students")

def closeProgram()->None:
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

try:
    pythondb = mysql.connector.connect(
        host="localhost",
        user="gochuicod",
        password="20259388",
        database="pythondb"
    )
    cursor = pythondb.cursor()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    main()
    pythondb.close()