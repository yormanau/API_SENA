from flask import Flask, render_template, request, jsonify, session
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = "123"

def get_db():
    return sqlite3.connect("db/app.db")


# --- LOGIN FORM ---
@app.route("/login")
def login():
    return render_template("login.html")


# --- REGISTER FORM ---
@app.route("/register")
def register():
    return render_template("register.html")


# --- API LOGIN ---
@app.route("/api/login", methods=["POST"])
def api_login():
    username = request.form["username"]
    password = request.form["password"].encode("utf-8")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return jsonify({
            "success": False,
            "message": "¡Credenciales incorrectas!"
        }), 401

    stored_hashed_password = row[0]

    if isinstance(stored_hashed_password, str):
        stored_hashed_password = stored_hashed_password.encode("utf-8")

    # Verificar contraseña
    if bcrypt.checkpw(password, stored_hashed_password):
        session["username"] = username
        return jsonify({
            "success": True,
            "title" : "Exito",
            "message": "Inicio de sesión exitoso",
        })
    else:
        return jsonify({
            "success": False,
            "message": "¡Credenciales incorrectas!"
        }), 401


# --- API REGISTER ---
@app.route("/api/register", methods=["POST"])
def api_register():
    username = request.form["username"]
    password = request.form["password"].encode("utf-8")

    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt()).decode("utf-8")

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({
            "success": False,
            "message": "Ese usuario ya existe"
        }), 400

    conn.close()

    return jsonify({
        "success": True,
        "title": "Exito",
        "message": "Se ha creado tu cuenta correctamente.",
    })

@app.route("/success-login")
def success_login():
    from flask import session
    return render_template(
        "success.html",
        title="Bienvenido",
        message="Inicio de sesión exitoso.",
        username=session.get("username")
    )



if __name__ == "__main__":
    app.run(debug=True)
