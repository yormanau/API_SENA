import sqlite3

conn = sqlite3.connect("db/app.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
""")
print("Tabla creada correctamente")
conn.commit()
conn.close()
