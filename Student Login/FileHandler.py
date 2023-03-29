from Student import Student
filename:str = "student.csv"

def saveFile(students:list)->None:
    file = open(filename,"w")
    [file.write(f"{student}\n") for student in students]
    file.close()

def loadFile()->list:
    file = open(filename, "r")
    students:list = []
    for item in file:
        student = item.strip("\n").split(" ")
        students.append(Student(student[0],student[1],student[2],student[3],student[4]))
    file.close()
    return students