import sqlite3
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email On Users (email)")
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
                  (f"User{i}", f"example{i}@mail.com", f'{i * 10}', '1000'))

cursor.execute("UPDATE Users SET balance = ? WHERE  id % ? ", ("500", "2"))

for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

cursor.execute("SELECT * FROM Users WHERE age != ?",  (60,))
users = cursor.fetchall()
for user in users:
    print(user)
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
cursor.execute("SELECT COUNT(*) FROM Users")
total_1 = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance = cursor.fetchone()[0]
print(avg_balance)
connection.commit()
connection.close()