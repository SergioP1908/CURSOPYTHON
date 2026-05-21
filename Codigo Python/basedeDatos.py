import mysql.connector

# Conexión
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="coche"
)

cursor = conexion.cursor()

# Crear tabla
sql = """
CREATE TABLE IF NOT EXISTS datos (
    matricula VARCHAR(7) PRIMARY KEY,
    marca VARCHAR(10),
    modelo VARCHAR(10),
    anio VARCHAR(4),
    color VARCHAR(10)
)
"""

cursor.execute(sql)

print("Tabla creada correctamente")

conexion.close()