from Person import Person

class Student(Person):
    def __init__(self,id:str,firstname:str,lastname:str,course:str,level:str)->None:
        self.id = id
        super().__init__(firstname,lastname)
        self.course = course
        self.level = level

    def __eq__(self,id)->bool: return self.id == id
    def __str__(self)->str: return f"{self.id} {super().__str__()} {self.course} {self.level}"