# 📋 Prueba Técnica: Gestión de Tareas - Wizz Life

Este proyecto consiste en un servicio backend diseñado para gestionar las tareas de un equipo, permitiendo el registro de usuarios, autenticación y un CRUD completo de tareas con filtros avanzados.

---

## 🛠️ Requerimientos Técnicos y Tecnologías
* [cite_start]**Lenguaje:** Python 3.10+ [cite: 30]
* [cite_start]**Framework:** Django 5.x & Django REST Framework [cite: 30]
* [cite_start]**Autenticación:** JSON Web Tokens (JWT) [cite: 28]
* [cite_start]**Base de Datos:** SQLite (Configurada para persistencia local) [cite: 41]
* [cite_start]**Contenedorización:** Docker & Gunicorn [cite: 32]

---

## [cite_start]🚀 Guía de Ejecución [cite: 51]

### [cite_start]1. Ejecución Local (Desarrollo) [cite: 52]
Para levantar el proyecto en tu máquina local:
1. **Clonar el repositorio:** `git clone https://github.com/Simboraido/prueba-wizz`
2. **Crear entorno virtual:** `python -m venv venv`
3. **Activar entorno:** `.\venv\Scripts\activate` (Windows) o `source venv/bin/activate` (Linux/Mac)
4. **Instalar dependencias:** `pip install -r requirements.txt`
5. **Ejecutar migraciones:** `python manage.py migrate`
6. **Iniciar servidor:** `python manage.py runserver`

### [cite_start]2. Ejecución con Docker [cite: 52]
1. **Construir la imagen:** `docker build -t wizz-backend .`
2. **Correr el contenedor:** `docker run -p 8000:8000 wizz-backend`

---

## [cite_start]📌 Endpoints Estandarizados [cite: 14]

| Método | Endpoint | Descripción | Requiere Token |
| :--- | :--- | :--- | :--- |
| POST | `/signup/` | [cite_start]Registro de nuevo usuario [cite: 17] | No |
| POST | `/signin/` | [cite_start]Inicio de sesión (JWT) [cite: 19] | No |
| GET | `/tasks/` | [cite_start]Listar tareas (Filtros y ordenamiento) [cite: 21] | Sí |
| POST | `/tasks/` | [cite_start]Crear una nueva tarea [cite: 23] | Sí |
| GET | `/tasks/{id}/` | [cite_start]Detalle de una tarea específica [cite: 25] | Sí |
| PATCH | `/tasks/{id}/` | [cite_start]Actualizar una tarea [cite: 26] | Sí |
| DELETE| `/tasks/{id}/` | [cite_start]Eliminar una tarea [cite: 27] | Sí |

---

## [cite_start]🧠 Decisiones Técnicas Relevantes [cite: 53]
* [cite_start]**Separación de Apps:** Se utilizaron apps independientes (`users` y `tasks`) para mantener una arquitectura limpia, facilitando la separación de responsabilidades[cite: 37].
* [cite_start]**Seguridad:** Se implementó JWT para manejar la autenticación de forma stateless, lo que permite un escalado eficiente en contenedores[cite: 28].
* [cite_start]**Puntos Extra:** Se añadieron capacidades de filtrado por estado y búsqueda por texto en el listado de tareas[cite: 9].

---

## [cite_start]🤖 Uso de Herramientas de IA [cite: 54]
[cite_start]Para la realización de esta prueba se utilizaron herramientas de Inteligencia Artificial (Gemini) como apoyo en la configuración de entorno, resolución de errores de importación y estructuración de la documentación[cite: 55]. [cite_start]El código ha sido revisado, comprendido y validado íntegramente por el desarrollador para asegurar su cumplimiento con los requerimientos[cite: 57].