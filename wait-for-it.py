import pymysql
import time
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de la base de datos
db_config = {
    'host': 'db',
    'user': 'root',
    'password': os.getenv('MYSQL_ROOT_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE')
}

# Esperar a que la base de datos esté lista
def wait_for_db():
    while True:
        try:
            # Intentar conectarse a la base de datos
            conn = pymysql.connect(**db_config)
            conn.close()
            print("Base de datos lista. Iniciando aplicación...")
            break
        except pymysql.MySQLError as e:
            print(f"Esperando por la base de datos... Error: {e}")
            time.sleep(1)

if __name__ == '__main__':
    wait_for_db()
    # Iniciar la aplicación Flask
    os.system('python run.py')
