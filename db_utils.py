# db_utils.py
import mysql.connector
from dbconnection import DB_CONFIG

def get_connection():

    connection = mysql.connect(
        host=DB_CONFIG['localhost'],
        user=DB_CONFIG['root'],
        password=DB_CONFIG['Shyamala@123'],
        database=DB_CONFIG['mydb']
    )
    return connection

def get_conn():
    return mysql.connector.connect(**DB_CONFIG)

def insert_plate(plate_text, confidence, image_path=None):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO plates (plate_text, confidence, image_path) VALUES (%s,%s,%s)",
                (plate_text, confidence, image_path))
    conn.commit()
    cur.close()
    conn.close()

def insert_vehicle_count(vehicle_type, count):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO vehicle_counts (vehicle_type, count_in_frame) VALUES (%s,%s)",
                (vehicle_type, count))
    conn.commit()
    cur.close()
    conn.close()

def insert_action(action, reason):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO traffic_actions (action, reason) VALUES (%s,%s)",
                (action, reason))
    conn.commit()
    cur.close()
    conn.close()
