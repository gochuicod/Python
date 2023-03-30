from Person import Person

class Student(Person):
    def __init__(self,student_id:str,firstname:str,lastname:str,course:str,level:str):
        super().__init__(firstname,lastname)
        self.student_id = student_id
        self.course = course
        self.level = level

    def getFirstname(self): return super().getFirstname()
    def getLastname(self): return super().getLastname()
    def getStudentID(self): return self.student_id
    def getCourse(self): return self.course
    def getLevel(self): return self.level