import pyodbc
import pandas

SERVER = r'DEVANSHU-DTS\SQL'
DATABASE = 'DETAILS'
USERNAME = 'sa'
PASSWORD = 'XDuce@123'


try:
    connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
    conn = pyodbc.connect(connectionString)
    print('Connected SuccessFully....')
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE CLASS (SID INT IDENTITY(101,1) PRIMARY KEY,SNAME VARCHAR(20));"
    )
    cursor.execute(
        "INSERT INTO CLASS (SNAME) VALUES ('DEVANSHU'),('MOHSIN');"
    )
    cursor.commit()
    print('SuccessFully Executed....')
except Exception as e:
    print("Error:", e)
