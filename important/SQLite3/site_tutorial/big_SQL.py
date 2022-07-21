# Create SQL tables
import sqlite3
from sqlite3 import Error

def create_connect(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as er:
        print(er)
    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as er:
        print(er)


def main():
    database = r"C:\ALL_CODES\python_projects\IMPORTANT\SQLite3\databases\new_database.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id INT PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority INT,
                                    status_id INT NOT NULL,
                                    project_id INT NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

    conn = create_connect(database)
    if conn is not None:
        create_table(conn, sql_create_projects_table)
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! Cannot be maked database!")


if __name__ == '__main__':
    main()
