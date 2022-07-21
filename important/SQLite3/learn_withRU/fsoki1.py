import sqlite3

conn = sqlite3.connect(r'C:\ALL_CODES\python_projects\IMPORTANT\SQLite3\databases\fsoki1.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    pass TEXT,
    cash INT
)""")

conn.commit()

user_login = input("Login: ")
user_pass = input("Password: ")

c.execute("SELECT * FROM users")
if c.fetchone() is None:
    c.execute("INSERT INTO users VALUES (?, ?, ?)", (user_login, user_pass, 0))
    conn.commit()
else:
    print("This note is execute")
    for value in c.execute("SELECT * FROM users"):
        print("EMAIL\t\t\tPASSWORD\t\tCASH")
        print(value[0], "\t", value[1], "\t\t", value[2])

conn.close()