import pyodbc
import pandas as pd

SERVER = r'DEVANSHU-DTS\SQL'
DATABASE = 'DETAILS'
USERNAME = 'sa'
PASSWORD = 'XDuce@123'

try:
    connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
    conn = pyodbc.connect(connectionString)
    print('Connected successfully....')
    
    cursor = conn.cursor()

    # Check if the table CLASS exists before creating it
    if not cursor.tables(table='CLASS', tableType='TABLE').fetchone():
        cursor.execute(
            "CREATE TABLE CLASS (SID INT IDENTITY(101,1) PRIMARY KEY,SNAME VARCHAR(20));"
        )

    cursor.execute(
        "INSERT INTO CLASS (SNAME) VALUES ('DEVANSHU'),('MOHSIN');"
    )

    query = cursor.execute("SELECT * FROM CLASS;")
    data = query.fetchall()
    print(data)    

    df = pd.DataFrame(data, columns=[desc[0] for desc in query.description])

    print(df)
    conn.commit()
    print('Successfully executed....')
    
except Exception as e:
    print("Error:", e)
