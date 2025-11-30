from flask import Flask, render_template, request, jsonify, session
import sqlite3
import bcrypt

app = Flask(__name__)

# Clave secreta para manejar sesiones de Flask
app.secret_key = "123"

# ------------------------------------------------------------
# Función para obtener la conexión a la base de datos SQLite
# ------------------------------------------------------------
def get_db():
    return sqlite3.connect("db/app.db")


# ------------------------------------------------------------
# RUTA: Página de login (formulario HTML)
# ------------------------------------------------------------
@app.route("/login")
def login():
    return render_template("login.html")


# ------------------------------------------------------------
# RUTA: Página de registro (formulario HTML)
# ------------------------------------------------------------
@app.route("/register")
def register():
    return render_template("register.html")


# ------------------------------------------------------------
# API LOGIN (maneja los datos enviados por login.js)
# ------------------------------------------------------------
@app.route("/api/login", methods=["POST"])
def api_login():
    # Obtener datos del formulario
    username = request.form["username"]
    password = request.form["password"].encode("utf-8")  # Convertir a bytes

    # Buscar usuario en la base de datos
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()

    # Si no existe el usuario, devolver error
    if not row:
        return jsonify({
            "success": False,
            "message": "El usuario no existe."
        }), 401

    # Contraseña almacenada en BD
    stored_hashed_password = row[0]

    # Si está en string, convertir a bytes
    if isinstance(stored_hashed_password, str):
        stored_hashed_password = stored_hashed_password.encode("utf-8")

    # Validar contraseña con bcrypt
    if bcrypt.checkpw(password, stored_hashed_password):
        # Guardar usuario en sesión
        session["username"] = username

        return jsonify({
            "success": True,
            "title": "Éxito",
            "message": "Inicio de sesión exitoso",
        })
    else:
        # Contraseña incorrecta
        return jsonify({
            "success": False,
            "message": "Usuario o contraseña incorrecta."
        }), 401


# ------------------------------------------------------------
# API REGISTER (maneja los datos enviados por register.js)
# ------------------------------------------------------------
@app.route("/api/register", methods=["POST"])
def api_register():
    # Obtener datos del formulario
    username = request.form["username"]
    password = request.form["password"].encode("utf-8")

    # Encriptar contraseña
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt()).decode("utf-8")

    conn = get_db()
    cursor = conn.cursor()

    try:
        # Insertar usuario en BD
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )
        conn.commit()

    except sqlite3.IntegrityError:
        # Error: usuario duplicado
        return jsonify({
            "success": False,
            "message": "El usuario ya existe"
        }), 400

    conn.close()

    # Respuesta exitosa
    return jsonify({
        "success": True,
        "title": "Éxito",
        "message": "Se ha creado tu cuenta correctamente.",
    })


# ------------------------------------------------------------
# RUTA: Página de home después del login
# ------------------------------------------------------------
@app.route("/home")
def success_login():
    return render_template(
        "home.html",
        title="Bienvenido",
        message="¡Es un gusto tenerte de vuelta!",
        username=session.get("username")  # Mostrar usuario en pantalla
    )


# ------------------------------------------------------------
# Ejecutar servidor en modo debug
# ------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
