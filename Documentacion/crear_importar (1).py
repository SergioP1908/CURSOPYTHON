# Paquete de Python necesario para conectarnos a MySQL.

# Utilizaremos el programa 'pip' que vimos anteriormente para instalar el paquete necesario 
# para interconectar 'Python' y 'MySQL'. Desde la línea de comandos ejecutamos el programa pip con el siguiente paquete a instalar:

        # pip install mysql-connector

# Luego de ejecutar el programa pip podemos ver que nos informa de la instalación del paquete 'mysql-connector': 

        # python.exe -m pip install --upgrade pip

# Añadir la siguiente línea en la configuracion de JSON:

        # "python.analysis.extraPaths": ["./src", "./lib"],

import os

os.system("cls")

import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", db="")
cursor1=conexion1.cursor()

cursor1.execute("drop database if exists coches;")
cursor1.execute("create database coches character set utf8 collate utf8_spanish_ci;")
cursor1.execute("use coches;")
cursor1.execute("create table datos (marca varchar(10), modelo varchar(10), anyo varchar(4), color varchar(10), matricula varchar(7) PRIMARY KEY);")
cursor1.execute("insert into datos values ('Suzuki','Jimny', '2020', 'Gris','0547NHB');")

cursor1.execute("LOAD DATA INFILE 'C:/ejemplos/base_datos/base_coches.csv' INTO TABLE datos FIELDS TERMINATED BY  '\t' LINES TERMINATED BY '\n'")

conexion1.commit()       # IMPORTANTE ACTUALIZAR SIEMPRE LA BASE DE DATOS


        # Insercion de registros controlando errores de repeticion de matricula o matriculas vacias

opcion = input("Quieres introducir algun registro mas? (S/N): ")

opcion = opcion.upper()

while (opcion == "S"):
    marca = input("Escribe la marca del vehiculo: ")
    modelo = input("Escribe el modelo del vehiculo: ")
    anyo = input("Escribe el año de matriculación: ")
    color = input("Escribe el color del vehiculo: ")
    matricula = input("Escribe la matricula del vehiculo: ")
    
    if (matricula != ""):
        
        cursor1.execute("select * from datos where matricula='" + matricula + "';")
        
        # Contamos cuantos registros tiene la tabla de respuesta guardada en cursor1
        
        cuantos = 0
        for indice in cursor1:
            cuantos += 1
       
        if (cuantos == 0):
                cursor1.execute("insert into datos values ('" + marca + "','" + modelo + "', '" + anyo + "', '" + color + "','" + matricula +"');")
                print("Registro insertado correctamente.\n")
                
                conexion1.commit()                # IMPORTANTE ACTUALIZAR SIEMPRE LA BASE DE DATOS
        else:
            print("Esa matrícula ya existe en la tabla.\n")
                
    else:
        print("La matrícula no puede estar vacía.\n")

    opcion = input("Quieres introducir algun registro mas? (S/N): ")

    opcion = opcion.upper()


# Muestra del listado de tablas


print("En la base de datos tienes las siguientes tablas: ")     

cursor1.execute("show tables")

longitud = 0
for tabla in cursor1:
    print(tabla)
    longitud += 1

print("En la base de datos tienes " + str(longitud) + " tablas\n")

opcion = input("Escribe el nombre de la tabla que quieres ver: ")



cursor1.execute("select * from " + opcion + ";")

longitud = 0
for fila in cursor1:
    ancho = len(fila)
    print(fila)
    longitud += 1


print("\nEn la tabla " + opcion + " tienes " + str(ancho)+ " campos y " + str(longitud) + " registros \n")



conexion1.close()           # IMPORTANTE CERRAR SIEMPRE LA BASE DE DATOS

