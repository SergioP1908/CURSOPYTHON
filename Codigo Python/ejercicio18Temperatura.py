import os
os.system("cls")
import csv
import mysql.connector

#CONEXIÓN DE BASE DE DATOS
conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", db="tiempo")
cursor1=conexion1.cursor()
print("conexion correcta")
#QUERY UTILIZADA PARA INGRESAR DATOS EN LA TABLA VERANO
query = """LOAD DATA INFILE "C:/Users/Usuario/Desktop/PYTHON/ejercicio18.csv" IGNORE INTO TABLE verano
		FIELDS TERMINATED BY  ';'			
		LINES TERMINATED BY '\n'
        IGNORE 1 LINES"""
#EJECUTAR LA CONSULTA Y GUARDAR
cursor1.execute(query)
conexion1.commit() # Confirma los datos que se quiere ingresar en la base de datos

"""#LECTURA DE BASE DE DATOS EN UNA TABLA
opcion = "verano"

cursor1.execute("select * from " + opcion + ";")

longitud = 0
for fila in cursor1:
    ancho = len(fila)
    print(fila)
    longitud += 1"""

#MOSTRAR LA BASE DE DATOS EN EL TERMINAL
print("***********************************************************************")

#SELECCIONA TODOS LOS DATOS DE LA BASE DE DATOS A PYTHON
cursor1.execute("SELECT * FROM verano;")

# Guardamos todas las filas en una lista para poder procesarlas una a una
filas = cursor1.fetchall()

print("--- PROCESANDO FILAS CON PYTHON ---")
#LEEMOS EL CAMPO DE CADA FILA
for fila in filas:
    
    
    #PRIMARY KEY DE LA BASE DE DATOS 
    fecha_registro = fila[0]
    
    # EXTRAE DATOS DE LA COLUMNA 2 HASTA LA COLUMNA 7 DE CADA UNA DE LAS FILAS
    temperaturas_ciudades = fila[2:7] # Esto extrae: (19.2, 30.5, 27.5, 14.9, 31.3)
    
    # CALCULAMOS EL PROMEDIO DE CADA UNA DE LAS TEMPERATURAS DIVIDIDO POR LA CANTIDAD DE CUDADES
    promedio = sum(temperaturas_ciudades) / len(temperaturas_ciudades)
    
    # SE ESTABLECE 2 DECIMALES
    promedio = round(promedio, 2)
    clima =""
    if promedio>25:
        clima = "caliente"
    elif promedio<=25 and promedio >=20:
        clima = "Templado"
    elif promedio<20:
        clima= "frio"

    print(clima)
# HACER EL UPDATE EN LA BASE DE DATOS PARA TEMP_MEDIA Y CLASIFICACION
    query_update = "UPDATE verano SET temp_media = "+str(promedio)+ " WHERE fecha = '"+str(fecha_registro)+"';"
    query_update_clima = "UPDATE verano SET clasificacion = '"+clima+ "' WHERE fecha = '"+str(fecha_registro)+"';"
# Creamos un cursor temporal
    cursor_actualizar = conexion1.cursor()

    cursor_actualizar.execute(query_update)
    cursor_actualizar.execute(query_update_clima)

    cursor_actualizar.close()
    
#LECTURA DE BASE DE DATOS EN UNA TABLA
opcion = "verano"

cursor1.execute("select * from " + opcion + ";")

longitud = 0
for fila in cursor1:
    ancho = len(fila)
    print(fila)
    longitud += 1

#MOSTRAR LA BASE DE DATOS EN EL TERMINAL
print("\nEn la tabla " + opcion + " tienes " + str(ancho)+ " campos y " + str(longitud) + " registros \n")

# 4. CONFIRMAR TODOS LOS CAMBIOS Y CERRAR
conexion1.commit()
cursor1.close()
conexion1.close()

print("\n¡Todos los registros han sido actualizados desde Python!")
print("DATOS INGRESADOS CORRECTAMENTE")
