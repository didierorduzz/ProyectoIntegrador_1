import oracledb

# Inicializa el cliente de Oracle
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_26")  # Ajusta esta ruta si tu carpeta es diferente

def get_connection():
    return oracledb.connect(
        user="proyecto01",
        password="proyecto01",  # Reemplaza con tu contraseña real si la cambiaste
        dsn="localhost/XE"
    )