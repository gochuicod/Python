class Person():
    def __init__(self,firstname:str,lastname:str)->None:
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self)->str: return f"{self.firstname} {self.lastname}"