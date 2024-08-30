import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    dbname='my_database',
    user='your_user',
    password='your_password',
    host='localhost'
)
conn.autocommit = False
cur = conn.cursor()

def read_all_records():
    try:
        cur.execute("SELECT * FROM my_table")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Error: {e}")

def read_record(record_id):
    try:
        cur.execute("SELECT * FROM my_table WHERE id = %s", (record_id,))
        row = cur.fetchone()
        print(row)
    except Exception as e:
        print(f"Error: {e}")

def create_record(name):
    try:
        cur.execute("INSERT INTO my_table (name) VALUES (%s)", (name,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")

def delete_record(record_id):
    try:
        cur.execute("DELETE FROM my_table WHERE id = %s", (record_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")

def close_connection():
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_record('Alice')
    create_record('Bob')
    print("All records:")
    read_all_records()
    print("Read record with ID 1:")
    read_record(1)
    delete_record(1)
    print("All records after deletion:")
    read_all_records()
    close_connection()
