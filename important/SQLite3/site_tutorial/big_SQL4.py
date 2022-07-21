import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as er:
        print(er)
    return conn

def select_all_tasks(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()
    for row in rows:
        print(row)


def select_task_by_priority(conn, priority):
    c = conn.cursor()
    c.execute("SELECT * FROM tasks WHERE priority = ?", (priority,))
    rows = c.fetchall()
    for row in rows:
        print(row)

def main():
    database = r"C:\ALL_CODES\python_projects\IMPORTANT\SQLite3\databases\new_database.db"
    conn = create_connection(database)

    with conn:
        print("\n1) Query task by priority:\n")
        select_task_by_priority(conn, 1)
        print("\n2) Query all tasks:\n")
        select_all_tasks(conn)

if __name__ == '__main__':
    main()
