from Connection import Connection_to_mysql

connection = Connection_to_mysql()

# print(connection)
if connection:
    print('Database Connected Successfully...')

    cursor = connection.cursor()

    query = 'select * from table1;'
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
    print('Connection Closed!...')

else:
    print('Database Connection Failed!!')
