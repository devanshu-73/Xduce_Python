import pyodbc

SERVER = r'DEVANSHU-DTS\SQL'
DATABASE = 'DETAILS'
USERNAME = 'sa'
PASSWORD = 'XDuce@123'

try:
    connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
    conn = pyodbc.connect(connectionString)
    print('Connected successfully....')
    
    cursor = conn.cursor()

    cursor.execute(
        "IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'dbo' AND TABLE_NAME = 'CLASS') CREATE TABLE CLASS (SID INT IDENTITY(101,1) PRIMARY KEY,SNAME VARCHAR(20));"
    )
    query = cursor.execute("SELECT * FROM CLASS;")
    data = query.fetchall()
    
    # "INSERT INTO CLASS (SNAME) VALUES ('DEVANSHU'),('MOHSIN');"
    print(data)
    conn.commit()
    print('Successfully executed....')
    
except Exception as e:
    print("Error:", e)
