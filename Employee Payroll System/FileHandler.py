def loadEmployees()->list:
    file = open("employee.csv","r")
    employees:list = []
    [employees.append(item.strip("\n").split(" ")) for item in file] # strips current string's newline, splits it and then appends to a temporary list
    file.close()
    return employees

def loadPositions()->list:
    file = open("position.csv","r")
    positions:list = []
    [positions.append(item.strip("\n").split(" ")) for item in file]
    file.close()
    return positions

def loadPayroll()->list:
    file = open("payroll.csv","r")
    employee:list = []
    [employee.append(item.strip("\n")) for item in file]
    file.close()
    return employee

def savePayroll(employeeData:list)->None:
    file = open("payroll.csv","w")
    [file.write(f"{employee}\n") for employee in employeeData] # rewrites current data with new one
    file.close()