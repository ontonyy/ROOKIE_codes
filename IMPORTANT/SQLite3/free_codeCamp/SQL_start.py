import sqlite3

conn = sqlite3.connect(r'C:\ALL_CODES\python_projects\IMPORTANT\SQLite3\databases\customer.db')

c = conn.cursor()

c.execute("SELECT * FROM customers")

print("NAME" + "\t\t\t EMAIL" + "\n-----" + "\t\t\t ------")
for x in c.fetchall():
    print(f"{x[0]} {x[1]} \t\t {x[2]}")

conn.commit()
conn.close()