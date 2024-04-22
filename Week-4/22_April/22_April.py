from Connection import Connection_to_mysql

connection = Connection_to_mysql()

print(connection)
if connection:
    print('Database Connected Successfully...')

    

else:
    print('Database Connection Failed!!')
