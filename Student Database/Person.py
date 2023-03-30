class Person:
    def __init__(self,firstname:str,lastname:str):
        self.firstname = firstname
        self.lastname = lastname

    def getFirstname(self)->tuple: return (self.firstname)
    def getLastname(self)->tuple: return (self.lastname)