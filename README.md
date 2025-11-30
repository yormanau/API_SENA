# Sistema de Login y Registro con Flask

Este proyecto implementa un sistema básico de autenticación utilizando
**Flask**, **SQLite**, **bcrypt**, **HTML/CSS** y **JavaScript**.

## 🚀 Características

-   Registro de usuarios con contraseñas encriptadas.
-   Inicio de sesión utilizando sesiones seguras.
-   API REST para login y registro.
-   Frontend con validación y *toasts* animados.
-   Base de datos SQLite.
-   Código limpio y estructurado.

## 📁 Estructura

    API/
    │── app.py
    │── db/app.db
    │── static/
    │     ├── css/styles.css
    │     └── js/
    │           ├── login.js
    │           ├── register.js
    │           └── toast.js
    └── templates/
          ├── login.html
          ├── register.html
          └── success.html

## 🔧 Instalación

``` bash
pip install flask bcrypt
```

## ▶ Ejecutar

``` bash
python app.py
```

## 🌐 Uso / Endpoints

Luego abre tu navegador en la dirección que Flask te indica al iniciar la aplicación, por ejemplo:
http://127.0.0.1:5000/
- `/login` — Página de inicio de sesión.
- `/register` — Página de registro de usuario.

## 🔐 Seguridad

-   Contraseñas encriptadas con bcrypt.
-   No se guarda información sensible en texto plano.
-   Sesiones seguras en Flask.

## 📄 Licencia

Proyecto educativo. Libre uso.
