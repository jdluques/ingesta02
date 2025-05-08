import mysql.connector
import pandas as pd
import boto3

# Reemplaza esto con la IP privada de la MV donde corre MySQL
MYSQL_HOST = '172.31.29.213'  # <-- reemplaza esto
MYSQL_PORT = 8005

DB_CONFIG = {
    'host': MYSQL_HOST,
    'port': MYSQL_PORT,
    'user': 'root',
    'password': 'utec',
    'database': 'bd_api_employees'
}

CSV_FILENAME = 'data_mysql.csv'
BUCKET_NAME = 'jdls-output-1'
S3_KEY = 'data_mysql.csv'

def conectar_mysql():
    return mysql.connector.connect(**DB_CONFIG)

def exportar_a_csv(conexion):
    query = "SELECT * FROM employees"
    df = pd.read_sql(query, conexion)
    df.to_csv(CSV_FILENAME, index=False)
    print(f"✅ Datos exportados a {CSV_FILENAME}")

def subir_a_s3():
    s3 = boto3.client('s3')
    s3.upload_file(CSV_FILENAME, BUCKET_NAME, S3_KEY)
    print(f"✅ Archivo {CSV_FILENAME} subido al bucket S3 '{BUCKET_NAME}'")

def main():
    try:
        conexion = conectar_mysql()
        exportar_a_csv(conexion)
        subir_a_s3()
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            conexion.close()

if __name__ == "__main__":
    main()
