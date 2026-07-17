import os
import pymysql

def get_connection():
    print("HOST:", os.getenv("DB_HOST"))
    print("PORT:", os.getenv("DB_PORT"))
    print("USER:", os.getenv("DB_USER"))
    print("DB:", os.getenv("DB_NAME"))

    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        ssl={"ssl": {}},
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=10,
    )
