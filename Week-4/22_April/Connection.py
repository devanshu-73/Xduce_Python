import pymysql

def Connection_to_mysql():    
    connection = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password ='root',
        database = 'practice',
        port = 3306,
        autocommit = True
    )
    return connection