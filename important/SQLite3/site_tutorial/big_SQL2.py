# Inserting data to SQL tables
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as er:
        print(er)

    return conn

def create_project(conn, project):
    sql = ("INSERT INTO projects(name, begin_date, end_date) VALUES(?, ?, ?)")
    c = conn.cursor()
    c.execute(sql, project)
    conn.commit()
    return c.lastrowid


def create_task(conn, task):
    sql = "INSERT INTO tasks(name, priority, status_id, project_id, begin_date, end_date) VALUES(?, ?, ?, ?, ?, ?)"
    c = conn.cursor()
    c.execute(sql, task)
    conn.commit()
    return c.lastrowid


def main():
    database = r'C:\ALL_CODES\python_projects\IMPORTANT\SQLite3\databases\new_database.db'

    conn = create_connection(database)
    with conn:
        project = ('APP', '2021-08-19', '2065-08-19')
        project_id =create_project(conn, project)

        task_1 = ('Analyze app', 1, 1, project_id, '2020-05-11', '2021-07-15')
        task_2 = ('Confirm user', 1, 1, project_id, '2016-02-21', '2017-03-10')

        create_task(conn, task_1)
        create_task(conn, task_2)


if __name__ == '__main__':
    main()
