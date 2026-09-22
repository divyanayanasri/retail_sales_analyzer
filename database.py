import mysql.connector
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "My_Password",   
    "database": "retail_sales_db",
}


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


def execute_query(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    conn.commit()
    cursor.close()
    conn.close()


def fetch_query(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
