PRUEBA TECNICA FULLSTACK JUNIOR WIZZ LIFE

Este proyecto consiste en el desarrollo de un servicio backend para gestionar las tareas de un equipo. El sistema permite registrar usuarios, autenticarse y realizar un CRUD completo de tareas vinculadas a cada cuenta.

ENLACES DEL PROYECTO

Repositorio en GitHub: https://github.com/Simboraido/prueba-wizz
URL del servicio en Render: https://prueba-wizz.onrender.com

REQUERIMIENTOS TECNICOS

Framework: Django y Django REST Framework

Autenticacion: JSON Web Tokens (JWT)

Contenedorizacion: Docker

Despliegue: Render

Servidor de produccion: Gunicorn

GUIA DE EJECUCION

Ejecucion local:

Clonar el repositorio: git clone https://github.com/Simboraido/prueba-wizz

Crear un entorno virtual: python -m venv venv

Activar el entorno virtual e instalar dependencias: pip install -r requirements.txt

Ejecutar las migraciones de base de datos: python manage.py migrate

Iniciar el servidor: python manage.py runserver

Ejecucion con Docker:

Construir la imagen: docker build -t wizz-backend .

Ejecutar el contenedor: docker run -p 8000:8000 wizz-backend

ESTANDARIZACION DE ENDPOINTS

Rutas de Autenticacion:

POST /signup/ : Registro de usuarios.

POST /signin/ : Autenticacion y obtencion de token.

Rutas de Tareas (Requieren Token):

GET /tasks/ : Listar tareas (incluye filtros por estado y busqueda).

POST /tasks/ : Crear una nueva tarea.

GET /tasks/{id}/ : Obtener detalle de una tarea.

PATCH /tasks/{id}/ : Actualizar informacion o estado.

DELETE /tasks/{id}/ : Eliminar una tarea.

DECISIONES TECNICAS RELEVANTES

Arquitectura: Se implementaron aplicaciones independientes (users y tasks) para asegurar la modularidad y el orden del codigo.

Seguridad: Se utilizo JWT para el manejo de sesiones de forma stateless, optimizando el consumo de recursos en el servidor.

Despliegue: Se incluyo un Dockerfile configurado para entorno de produccion utilizando Gunicorn, cumpliendo con los estandares de disponibilidad exigidos.

USO DE HERRAMIENTAS DE INTELIGENCIA ARTIFICIAL

Se utilizaron herramientas de Inteligencia Artificial para el apoyo en la configuracion del entorno y la estructuracion de la documentacion. El desarrollo fue supervisado y validado en su totalidad para garantizar que la implementación cumple con los requisitos técnicos y funcionales solicitados.