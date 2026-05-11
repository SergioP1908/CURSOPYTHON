'''I. Se entrega un fichero de datos llamado "alumnos.txt". Importar el fichero a 
una tabla en Python y realizar los siguientes  cálculos:

Edad media de los alumnos mayores de 18 años y menores de 65 (incluyendo 18 y 65).
Número de alumnos de Madrid, Guadalajara y Soria, indicando cada valor por separado.

II. A continuación solicitar al operador los siguientes datos:

Rango de Edad: dos valores numéricos enteros que nos delimiten el rango de edad.
Provincia: dos provincias en la que buscaremos el rango de edad.
Se trata de generar un filtro a través de la edad y dos provincias. Si en la tabla 
existen registros que cumplan las condiciones, los datos encontrados se copiaran a 
un fichero de salida llamado "resultado.csv". En caso de que no haya registros se 
mostrará por pantalla el mensaje "No hay registros con ese filtro".

III. Guardar los documentos .CSV y el programa .PY en tu carpeta como Ejercicio 13.'''


ruta = r"D:\Curso_Programación\CURSO PYTHON\CURSOPYTHON\Documentacion\alumnos.txt"

archivo = open(ruta, "r", encoding="cp1252")
lineas = archivo.readlines()
archivo.close()

# =========================
# PARTE I
# =========================

edades_validas = []

madrid = 0
guadalajara = 0
soria = 0

for i in range(1, len(lineas)):

    datos = lineas[i].strip().split("\t")

    # Evitar errores por líneas mal separadas
    if len(datos) < 5:
        continue

    edad = int(datos[2])
    provincia = datos[4]

    # Edad media entre 18 y 65
    if edad >= 18 and edad <= 65:
        edades_validas.append(edad)

    # Contar provincias
    if provincia == "Madrid":
        madrid += 1
    elif provincia == "Guadalajara":
        guadalajara += 1
    elif provincia == "Soria":
        soria += 1

# Media de edad
if len(edades_validas) > 0:
    media = sum(edades_validas) / len(edades_validas)
    print("Edad media (18-65): " + str(round(media, 2)))
else:
    print("No hay alumnos en ese rango")

print("Madrid: " + str(madrid))
print("Guadalajara: " + str(guadalajara))
print("Soria: " + str(soria))


# =========================
# PARTE II
# =========================

edad_min = int(input("\nEdad minima: "))
edad_max = int(input("Edad maxima: "))

prov1 = input("Primera provincia: ")
prov2 = input("Segunda provincia: ")

resultado = []

for i in range(1, len(lineas)):

    datos = lineas[i].strip().split("\t")

    if len(datos) < 5:
        continue

    edad = int(datos[2])
    provincia = datos[4]

    if edad >= edad_min and edad <= edad_max:
        if provincia == prov1 or provincia == prov2:
            resultado.append(lineas[i])

# Guardar resultados
if len(resultado) > 0:

    salida = open("resultado.csv", "w", encoding="cp1252")

    salida.write(lineas[0])  # cabecera

    for r in resultado:
        salida.write(r)

    salida.close()

    print("resultado.csv creado correctamente")

else:
    print("No hay registros con ese filtro")