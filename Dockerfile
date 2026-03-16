# Usamos una imagen oficial y ligera de Python
FROM python:3.10-slim

# Evitamos que Python genere archivos basura y permitimos ver logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Creamos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos las dependencias y las instalamos
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código de nuestro proyecto
COPY . /app/

# Exponemos el puerto que usará Render
EXPOSE 8000

# Comando para arrancar la aplicación con Gunicorn
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]