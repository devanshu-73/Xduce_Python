from Connection import Connection_to_mysql

connection = Connection_to_mysql()

# print(connection)
if connection:
    print('Database Connected Successfully...')

    cursor = connection.cursor()

    # query = 'select * from table1;'
# ============================================================================
    # # Creating Table Into Database Practice

    # query = 'create table table2 (id int primary key,name varchar(255) not null);'
    # cursor.execute(query)
# ============================================================================
    # # Inserting Into Table
    
    query = "insert into table2 values (001,'Devanshu'),(002,'Yash'),(003,'Sahil');"
    cursor.execute(query)
# ============================================================================
    query = 'select * from table2;'
    cursor.execute(query)
# ============================================================================

    rows = cursor.fetchall()
    # print(rows)

    for row in rows:
        print(row)
    
    cursor.close()
    connection.close()
    print('Connection Closed!...')

else:
    print('Database Connection Failed!!')
