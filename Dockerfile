FROM python:3.10-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir cryptography

# Copiar el resto de los archivos de la aplicación
COPY . .

# Exponer el puerto donde Flask servirá la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "wait-for-it.py"]
