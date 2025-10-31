# Imagen base oficial de Python 3.11
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Evitar archivos .pyc y habilitar logs directos
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar dependencias del sistema necesarias (opcional)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivo de dependencias
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Exponer el puerto que usará Flask
EXPOSE 5000

# Variable de entorno para Flask
ENV FLASK_APP=main.py

# Comando por defecto para ejecutar la app
CMD ["python", "main.py"]
