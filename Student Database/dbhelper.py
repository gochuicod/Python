from mysql.connector import connect

conn = connect (host="localhost",user="gochuicod",password="20259388",database="pythondb")

def addRecord(table:str,**kwargs)->bool:
    values:list = list(kwargs.values())
    keys:list = list(kwargs.keys())
    fields:list = ",".join(keys)
    data:list = []
    for index in range(0,len(values)):
        if(keys[index] == "course"): data.append(f"{values[index].upper()}")
        else: data.append(f"{values[index].title()}")
    data:str = "','".join(data)

    cursor = conn.cursor()
    sql:str = f"insert into {table} ({fields}) values ('{data}')"
    cursor.execute(sql)
    if cursor.rowcount > 0:
        conn.commit()
        cursor.close()
        return True
    else: return False

def getRecord(table:str,**kwargs)->tuple:
    values = list(kwargs.values())
    keys = list(kwargs.keys())

    cursor = conn.cursor()
    sql:str = f"select * from {table} where {keys[0]}='{values[0]}'"
    cursor.execute(sql)
    if cursor.rowcount > 0: conn.commit()
    return cursor.fetchall()

def getAllRecords(table:str)->tuple:
    cursor = conn.cursor()
    sql:str = f"select * from {table}"
    cursor.execute(sql)
    if cursor.rowcount > 0: conn.commit()
    return cursor.fetchall()

def updateRecord(table:str,**kwargs)->None:
    values:list = list(kwargs.values())
    keys:list = list(kwargs.keys())
    fields:list = []
    for index in range(1,len(values)):
        fields.append(f"{keys[index]}='{values[index]}'")
        
    cursor = conn.cursor()
    sql:str = f"update {table} set {', '.join(fields)} where student_id={values[0]}"
    cursor.execute(sql)
    if cursor.rowcount > 0: conn.commit()
    cursor.close()

def deleteRecord(table:str,**kwargs)->None:
    values:list = list(kwargs.values())

    cursor = conn.cursor()
    sql:str = f"delete from {table} where student_id={values[0]}"
    cursor.execute(sql)
    if cursor.rowcount > 0: conn.commit()
    cursor.close()