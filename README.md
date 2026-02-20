🗳️ eVote System

Sistema de votación online desarrollado con Flask + MySQL + JavaScript que permite:
	•	Registro y login de usuarios
	•	Panel administrador
	•	Creación y gestión de elecciones
	•	Gestión de candidatos
	•	Votación segura (un voto por usuario)
	•	Visualización de resultados con porcentajes

⸻

🚀 Tecnologías utilizadas
	•	Python 3
	•	Flask
	•	Flask-CORS
	•	MySQL
	•	HTML5
	•	CSS3
	•	JavaScript (Fetch API)
	•	Sessions (Flask)

⸻

🔐 Roles del sistema

👤 Usuario (votar)
	•	Registrarse
	•	Iniciar sesión
	•	Ver elecciones activas
	•	Votar (solo una vez por elección)

👑 Administrador
	•	Crear elecciones
	•	Definir fechas
	•	Agregar candidatos
	•	Cambiar estado (upcoming / active / closed)
	•	Ver resultados
	•	Eliminar elecciones

⸻

📂 Estructura del proyecto

eVote/
│
├── app.py
├── db.py
├── routes/
│   └── elections.py
├── templates/
│   ├── login.html
│   ├── admin.html
│   ├── index.html
│   └── register.html
└── static/


⸻

⚙️ Configuración

1️⃣ Clonar repositorio

git clone https://github.com/GermanTornello/Final_programacion2.git
cd Final_programacion2


⸻

2️⃣ Crear entorno virtual

python -m venv venv
venv\Scripts\activate


⸻

3️⃣ Instalar dependencias

pip install flask flask-cors mysql-connector-python


⸻

4️⃣ Configurar base de datos

Crear base de datos en MySQL:

CREATE DATABASE evote;
USE evote;

Crear tablas principales:

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100),
    role ENUM('admin','votar')
);

CREATE TABLE elections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    start_date DATE,
    end_date DATE,
    status ENUM('upcoming','active','closed')
);

CREATE TABLE candidates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    election_id INT,
    FOREIGN KEY (election_id) REFERENCES elections(id)
);

CREATE TABLE votes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    election_id INT,
    candidate_id INT,
    timestamp DATETIME,
    UNIQUE(user_id, election_id)
);


⸻

5️⃣ Crear usuario administrador

INSERT INTO users (email, password, role)
VALUES ('admin@test.com', '1234', 'admin');


⸻

▶️ Ejecutar el proyecto

python app.py

Servidor disponible en:

http://127.0.0.1:5000


⸻

🧠 Flujo del sistema
	1.	Usuario se registra
	2.	Inicia sesión
	3.	Admin crea elección
	4.	Admin agrega candidatos
	5.	Admin activa elección
	6.	Usuario vota
	7.	Admin cierra elección
	8.	Admin visualiza resultados

⸻

🔒 Seguridad implementada
	•	Control de sesión con Flask
	•	Validación de roles
	•	Restricción de un voto por usuario por elección
	•	Protección de endpoints administrativos

⸻

📊 Resultados

Los resultados muestran:
	•	Total de votos
	•	Cantidad de votos por candidato
	•	Porcentaje de votos

⸻

🎯 Posibles mejoras futuras
	•	Encriptar contraseñas con bcrypt
	•	Estado automático según fecha
	•	Dashboard con gráficos
	•	Dockerización
	•	Deploy en la nube

⸻

👨‍💻 Autor

Germán Tornello
Proyecto Final – Programación II

⸻