# dbconnection.py
import pymysql

def get_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Shyamala@123',
        database='mydb'
    )
    return conn