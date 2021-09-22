import sqlite3

conn = sqlite3.connect(r'C:\ALL_CODES\python_projects\IMPORTANT\SQLite3\databases\new_database.db')
c = conn.cursor()
c.execute("SELECT * FROM tasks")

for x in c.fetchall():
    print(x)

conn.commit()
conn.close()