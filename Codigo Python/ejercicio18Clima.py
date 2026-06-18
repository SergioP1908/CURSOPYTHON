import os

os.system("cls")

from datetime import date                           # Para trabajar con fechas
from datetime import datetime                       # Para trabajar con horas
from datetime import timedelta                      # Para operar con dias

import mysql.connector

import numpy as np



# Paso 1: Creamos la estructura de la base de datos y la tabla con sus campos, e importamos la informacion del fichero de origen

conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", db="tiempo", allow_local_infile=True)
cursor1=conexion1.cursor()


cursor1.execute("drop database if exists tiempo;")
cursor1.execute("create database tiempo character set latin1 collate latin1_spanish_ci;")
cursor1.execute("use tiempo;")
cursor1.execute("create table verano (`fecha` DATE PRIMARY KEY, `dia` VARCHAR(15), `alcorcon` FLOAT, `mostoles` FLOAT, `leganes` FLOAT, `fuenlabrada` FLOAT, `getafe` FLOAT, `temp_media` FLOAT, `clasificacion` VARCHAR(10));")

cursor1.execute("LOAD DATA LOCAL INFILE 'ejercicio18.csv' INTO TABLE verano FIELDS TERMINATED BY ';' LINES TERMINATED BY '\n'")



# Paso 2: Guardamos la tabla en Python desde la tabla que esta en la base de datos

cursor1.execute("select * from verano")

tabla =[]

for fila in cursor1:
    tabla.append(fila)

filas = len(tabla)

if filas > 0:                               # Imprimimos la tabla en el terminal si no esta vacia

    print("Dataframe de Python\n")

    columnas = len(tabla[0])

    for i in range(filas):
            linea = ""
            
            for j in range(columnas):

              
                linea = linea + ("{0:10s}{1}".format(str(tabla[i][j])," | "))
                
            print(linea) 
            
else:
    
    print("La tabla no tiene registros")

# -----------------------------------------------------------------------------------------------------------------------------------

# Paso 3: Creacion y uso de la tabla mendiante NumPy


nueva = np.array(tabla)  # Tambien podemos convertir un Dataframe en un Array de NumPy


filas = len(nueva)

if filas > 0:                               # Imprimimos la tabla en el terminal si no esta vacia

    print("\n\nArray de Numpy\n")
    
    columnas = len(nueva[0])

    for i in range(filas):
            linea = ""
            
            for j in range(columnas):

                if j == 7:
                     media = (nueva[i][2] + nueva[i][3] + nueva[i][4] + nueva[i][5] + nueva[i][6]) / 5
                     media = round(media, 2)
                     nueva[i][7] = media

                if j == 8:
                    if nueva[i][7] < 20:
                          nueva[i][8] = "Frio"
                    elif nueva[i][7] > 25:
                         nueva[i][8] = "Cálido"
                    else:
                         nueva[i][8] = "Templado"
              
                linea = linea + ("{0:10s}{1}".format(str(nueva[i][j])," | "))
                
            # MODO 1 ORDEN SQL:    update verano set temp_media = 25.7, clasificacion = 'Templado' where fecha= '2023-09-01';
        
        
            modifica = "UPDATE verano SET temp_media=" + str(nueva[i][7]) + ", clasificacion='" + nueva[i][8] + "' WHERE fecha='" + nueva[i][0].strftime("%Y-%m-%d")  + "';"

            cursor1.execute(modifica)
        
            conexion1.commit()       # IMPORTANTE ACTUALIZAR SIEMPRE LA BASE DE DATOS
            

            # MODO 2 ORDEN SQL A PRUEBA DE INYECCION SQL:

            modifica = "UPDATE verano SET temp_media = %s, clasificacion = %s WHERE fecha = %s;"
            
            cursor1.execute(modifica, (round(nueva[i][7], 2), nueva[i][8], nueva[i][0].strftime("%Y-%m-%d")))

            conexion1.commit()       # IMPORTANTE ACTUALIZAR SIEMPRE LA BASE DE DATOS

            print(linea)              
            
else:
    
    print("La tabla no tiene registros")


cursor1.close()
conexion1.close()


# Paso 4: Creacion de los ficheros CSV con las clasificaciones usando NumPy


calido = np.array([nueva[0]])       # Crea un array vacío con el mismo tipo/forma copiando la primera fila
templado = np.array([nueva[0]])     # Crea un array vacío con el mismo tipo/forma copiando la primera fila
frio = np.array([nueva[0]])         # Crea un array vacío con el mismo tipo/forma copiando la primera fila

filas = len(nueva)

if filas > 0:
     columnas = len(nueva[0])

     for i in range(filas):
        if nueva[i][8] == "Cálido":
            calido = np.append(calido, [nueva[i]], axis=0)
        elif nueva[i][8] == "Frio":
            frio = np.append(frio, [nueva[i]], axis=0)
        elif nueva[i][8] == "Templado":
            templado = np.append(templado, [nueva[i]], axis=0)

calido = np.delete(calido, 0, axis=0)           # Borramos la primera fila copiada
templado = np.delete(templado, 0, axis=0)       # Borramos la primera fila copiada
frio = np.delete(frio, 0, axis=0)               # Borramos la primera fila copiada

cabecera = np.array([["Fecha","Dia","Alcorcón","Móstoles","Leganés","Fuenlabrada","Getafe", "Media","Clasificacion"]])

calido = np.concatenate((cabecera, calido), axis=0)
templado = np.concatenate((cabecera, templado), axis=0)
frio = np.concatenate((cabecera, frio), axis=0)

np.savetxt("C:/Users/Usuario/Desktop/PYTHON/calido.csv", calido, delimiter=';', fmt=['%s','%s','%s','%s','%s','%s','%s','%s','%s'])
np.savetxt("C:/Users/Usuario/Desktop/PYTHON/frio.csv", frio, delimiter=';', fmt=['%s','%s','%s','%s','%s','%s','%s','%s','%s'])
np.savetxt("C:/Users/Usuario/Desktop/PYTHON/templado.csv", templado, delimiter=';', fmt=['%s','%s','%s','%s','%s','%s','%s','%s','%s'])

# --- IMPRIMIR CÁLIDO ---
filas_calido = len(calido) # Medimos el tamaño real con cabecera incluida

if filas_calido > 0: 

    print("\n\nArray de temperaturas cálidas en Numpy\n")
    
    columnas = len(calido[0])

    for i in range(filas_calido): # <--- Usamos el tamaño correcto
            linea = ""
            
            for j in range(columnas):
                linea = linea + ("{0:14s}{1}".format(str(calido[i][j])," | "))

            print(linea) 


# --- IMPRIMIR TEMPLADO ---
filas_templado = len(templado) # Medimos el tamaño real con cabecera incluida

if filas_templado > 0: 

    print("\n\nArray de temperaturas templadas en Numpy\n")
    
    columnas = len(templado[0])

    for i in range(filas_templado): # <--- Usamos el tamaño correcto
            linea = ""
            
            for j in range(columnas):
                linea = linea + ("{0:14s}{1}".format(str(templado[i][j])," | "))

            print(linea) 


# --- IMPRIMIR FRÍO ---
filas_frio = len(frio) # Medimos el tamaño real con cabecera incluida

print("\n\nArray de temperaturas frías en Numpy\n")

if filas_frio > 0: 
  
    columnas = len(frio[0])

    for i in range(filas_frio): # <--- Usamos el tamaño correcto
            linea = ""
            
            for j in range(columnas):
                linea = linea + ("{0:14s}{1}".format(str(frio[i][j])," | "))

            print(linea)

# Paso 5: Creacion del fichero datos.CSV usando NumPy


cabecera = np.array([["Ciudad","Media_Septiembre","Media_Octubre","Nº dias frios","Nº dias templados","Nº dias cálidos"]])

ciudades = np.array(["","","Alcorcon","Mostoles","Leganes","Fuenlabrada", "Getafe"])

resultado = np.array([["", 0, 0, 0, 0, 0]])

# Recorremos la tabla completa para extraer los datos por columnas

filas = len(nueva)

if filas > 0:
     
     columnas = len(nueva[0])
          
     for j in range(columnas):

        if (j>=2 and j<=6):

            sumasep = 0
            sumaoct = 0

            cuentasep = 0
            cuentaoct = 0
            mediasep = 0
            mediaoct = 0

            frios = 0
            templados = 0
            calidos = 0

            for i in range(filas):
                                
                if (nueva[i][j] < 20):
                    frios += 1
                elif (nueva[i][j] > 25):
                    calidos +=1
                else:
                    templados += 1
                
                if (nueva[i][0].month) == 9:

                    sumasep = sumasep + nueva[i][j]
                    cuentasep +=1

                elif (nueva[i][0].month) == 10:
                        
                    sumaoct = sumaoct + nueva[i][j]
                    cuentaoct +=1

            mediasep = round(sumasep / cuentasep, 2)
            mediaoct = round(sumaoct / cuentaoct, 2)

            resultado = np.append(resultado, [[ciudades[j], mediasep, mediaoct, frios, templados, calidos]], axis=0)
                




os.system("cls")

resultado = np.delete(resultado, 0, axis=0)               # Borramos la primera fila copiada

resultado = np.concatenate((cabecera, resultado), axis=0)

np.savetxt("C:/Users/Usuario/Desktop/PYTHON/datos.csv", resultado, delimiter=';', fmt=['%s','%s','%s','%s','%s','%s'])

print(resultado)