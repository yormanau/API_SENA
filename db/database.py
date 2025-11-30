import sqlite3

# Conexión a la base de datos.
# Si no existe la carpeta "db" o el archivo "app.db", SQLite los creará.
# NOTA: Asegúrate de que la carpeta "db/" sí exista.
conn = sqlite3.connect("db/app.db")

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear la tabla 'users' si no existe.
# Esta tabla almacenará usuarios registrados con:
# - id: clave primaria autoincremental
# - username: nombre único del usuario
# - password: contraseña cifrada con bcrypt
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
""")

print("Tabla creada correctamente")

# Guardar cambios en la base de datos
conn.commit()

# Cerrar la conexión
conn.close()
