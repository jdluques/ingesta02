FROM python:3.11-slim

# Crea directorio para el código
WORKDIR /programas/ingesta2

# Copia el script al contenedor
COPY ingesta.py .

# Instala dependencias
RUN pip install --no-cache-dir mysql-connector-python pandas boto3

# Comando por defecto al correr el contenedor
CMD ["python", "./ingesta.py"]
