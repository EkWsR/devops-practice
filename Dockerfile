# Usar una imagen base de Python
FROM python:3.8-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar requirements.txt e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]