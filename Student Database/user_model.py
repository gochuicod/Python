from Student import Student
from dbhelper import *

table:str ="students"

def addStudent(**kwargs)->bool: return addRecord(table,**kwargs)
def findStudent(**kwargs)->bool: return getRecord(table,**kwargs)
def getAllStudents()->list: return getAllRecords(table)
def updateStudent(**kwargs)->bool: return updateRecord(table,**kwargs)
def deleteStudent(**kwargs)->bool: return deleteRecord(table,**kwargs)