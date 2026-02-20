Perfecto, te dejo un README listo para entregar (copiar y pegar en tu repo). Está alineado con todo lo que te piden 👇

⸻

:::writing{variant=standard id=58213}

🗳️ eVote System

Aplicación web para la gestión de procesos electorales digitales.

Permite registrar votantes, emitir votos de forma segura y visualizar resultados en tiempo real, aplicando control de acceso por roles.

⸻

📌 Funcionalidades

✅ Caso 1 – Listado de elecciones
	•	Visualización de elecciones disponibles
	•	Filtros por:
	•	Estado: upcoming, active, closed
	•	Fecha
	•	Nombre

✅ Caso 2 – Emisión de voto
	•	Solo usuarios con rol votar
	•	Solo en elecciones activas
	•	Solo un voto por elección
	•	Registro de timestamp

✅ Caso 3 – Resultados
	•	Solo usuarios con rol admin
	•	Muestra:
	•	Cantidad de votos por candidato
	•	Total de votos
	•	Porcentaje
	•	Ordenados de mayor a menor

⸻

🛠️ Tecnologías utilizadas
	•	Backend: Python + Flask
	•	Base de datos: MySQL
	•	Frontend: HTML + Bootstrap + JavaScript (Fetch API)

⸻

⚙️ Instalación
	1.	Clonar el repositorio:

git clone https://github.com/GermanTornello/Final_programacion2.git
cd Final_programacion2

	2.	Crear entorno virtual (opcional):

python -m venv venv
venv\Scripts\activate   # Windows

	3.	Instalar dependencias:

pip install flask flask-cors mysql-connector-python

	4.	Configurar la base de datos:

	•	Crear base de datos en MySQL
	•	Importar las tablas necesarias:
	•	users
	•	elections
	•	candidates
	•	votes

	5.	Ejecutar el backend:

python app.py

Servidor disponible en:

http://localhost:5000

	6.	Ejecutar el frontend:

Desde la carpeta donde están los HTML:

python -m http.server 8000

Frontend disponible en:

http://localhost:8000


⸻

🔗 Endpoints

🔐 Login

POST /login

Body:

{
  "email": "admin@test.com",
  "password": "1234"
}


⸻

🗳️ Obtener candidatos

GET /candidates/<election_id>


⸻

🗳️ Votar

POST /vote

Body:

{
  "election_id": 1,
  "candidate_id": 2
}

Restricciones:
	•	Usuario autenticado
	•	Rol votar
	•	Solo una vez por elección
	•	Elección activa

⸻

📊 Resultados

GET /results/<election_id>

Requiere:
	•	Usuario autenticado
	•	Rol admin

Respuesta:

{
  "total_votes": 10,
  "results": [
    {
      "name": "Lista A",
      "votes": 6,
      "percentage": 60
    }
  ]
}


⸻

🚪 Logout

POST /logout


⸻

🧪 Pruebas
	1.	Iniciar backend y frontend
	2.	Iniciar sesión
	3.	Emitir un voto
	4.	Ingresar como admin
	5.	Acceder a:

http://localhost:8000/results.html?election_id=1


⸻

👤 Credenciales

Admin
	•	Email: admin@test.com
	•	Password: 1234

Votante
	•	Email: user@test.com
	•	Password: 1234

⸻

🧱 Arquitectura
	•	Separación backend / frontend
	•	Uso de sesiones para autenticación
	•	API REST
	•	Control de acceso por roles
	•	Validaciones en backend

⸻

📌 Notas
	•	El sistema no permite votar más de una vez por elección
	•	Los resultados se calculan dinámicamente
	•	El acceso a resultados está restringido a administradores

⸻
