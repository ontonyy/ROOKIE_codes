# Updating data in SQL table
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as er:
        print(er)
    return conn


def update_task(conn, task):
    sql = """UPDATE tasks
            SET priority = ? ,
                begin_date = ? ,
                end_date = ? 
            WHERE id = ?"""
    c = conn.cursor()
    c.execute(sql, task)
    conn.commit()


def main():
    database = r"C:\ALL_CODES\python_projects\IMPORTANT\SQLite3\databases\new_database.db"

    conn = create_connection(database)
    with conn:
        update_task(conn, (2, '2015-01-04', '2015-01-06', 2))


if __name__ == '__main__':
    main()