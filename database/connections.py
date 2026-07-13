import pymysql

def get_connection():
    connection= pymysql.connect(
        host='HOST',
        user='USER',
        password='PASSWORD',
        database='astronomical_archive',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection