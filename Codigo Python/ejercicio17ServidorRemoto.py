import os
os.system("cls")
import csv
import mysql.connector

#CONEXIÓN DE BASE DE DATOS
conexion1=mysql.connector.connect(host="192.168.1.51", user="alumno", passwd="mipassword", db="ejercicio17")
cursor1=conexion1.cursor()
print("conexion correcta")

#LECTURA DE BASE DE DATOS EN UNA TABLA
opcion = "datos"

cursor1.execute("select * from " + opcion + ";")

longitud = 0
for fila in cursor1:
    ancho = len(fila)
    print(fila)
    longitud += 1

#MOSTRAR LA BASE DE DATOS EN EL TERMINAL
print("\nEn la tabla " + opcion + " tienes " + str(ancho)+ " campos y " + str(longitud) + " registros \n")

#SELECCIONA LA BASE DE DATOS 
cursor1.execute("SELECT * FROM " + opcion)
#SELECCIONA EL ENCABEZADO DE LA BASE DE DATOS
encabezados = [i[0] for i in cursor1.description]

datos_tabla = cursor1.fetchall()
#CREA LA RUTA DONDE SE EXPORTARA LOS DATOS
ruta = "C:/Users/Usuario/Desktop/PYTHON/Doc_Exportado/resultados.csv"

archivo = open(ruta, "w", newline="")
#CREA LA SEPARACION DE LOS DIFERENTES DATOS EN EL ARCHIVO CREADO
escritor = csv.writer(archivo, delimiter=";")
#ESCRIBE LOS ENCABEZADOS
escritor.writerow(encabezados)
#ESCRIBE LOS DATOS DE LA TABLA
escritor.writerows(datos_tabla)

#QUERY PARA CONTAR LA CANTIDAD DE CLIENTES
cursor1.execute("SELECT COUNT(estatus) FROM datos where estatus ='cliente'")

resultado = cursor1.fetchone()

totalClientes = resultado[0]

print("La cantidad total de clientes es: " + str(totalClientes))

#QUERY PARA LA SUMA TOTAL DE FACTURACION DE LOS CLIENTES
cursor1.execute("SELECT SUM(facturacion) FROM datos where estatus ='cliente'")

resultado1 = cursor1.fetchone()

totalFacturacion = round(resultado1[0],2)

print("El total de facturqacion  es: " + str(totalFacturacion))

#QUERY PARA LA SUMA TOTAL DE FACTURACION SI SON PROVEEDORES
cursor1.execute("SELECT SUM(facturacion) FROM datos WHERE estatus = 'proveedor' ")

resultado2 = cursor1.fetchone()

totalProveedor = round(resultado2[0],2)

print("El total de facturacion de proveedores  es: " + str(totalProveedor))

#QUERY PARA CONTAR LOS CLIENTES CUANDO EL ESTATUS ES PROVEEDOR
cursor1.execute("SELECT COUNT(ESTATUS) FROM datos WHERE estatus = 'proveedor' ")

resultado3 = cursor1.fetchone()

totalProveedorStatus = resultado3[0]

print("El total de clientes proveedores  es: " + str(totalProveedorStatus))

#QUERY PARA SUMAR EL BENEFICIO TOTAL
cursor1.execute("SELECT SUM(facturacion) FROM datos  ")

resultado4 = cursor1.fetchone()

totalBeneficio = round(resultado4[0],2)

print("El beneficio total  es: " + str(totalBeneficio))

#QUERY PARA CONTAR LOS CLIENTES MOROSOS
cursor1.execute("SELECT COUNT(facturacion) FROM datos WHERE facturacion <0 and estatus = 'cliente' ")

resultado5 = cursor1.fetchone()

totalClientesMorosos = resultado5[0]

print("El total de clientes morosos  es: " + str(totalClientesMorosos))

#QUERY MEDIA FACTURACION DE CLIENTES
cursor1.execute("SELECT AVG(facturacion) FROM datos WHERE estatus ='cliente'  ")

resultado6 = cursor1.fetchone()

totalMediaClientes = round(resultado6[0],2)

print("La media de facturacion de clientes es: " + str(totalMediaClientes))

#QUERY PROVEEDORES MOROSOS
cursor1.execute("SELECT COUNT(estatus) FROM datos WHERE estatus ='proveedor' and facturacion <0 ")

resultado7 = cursor1.fetchone()

totalProveedorMoroso = resultado7[0]

print("La cantidad de proveedores morosos es: " + str(totalProveedorMoroso))

#QUERY CLIENTE MADRID
cursor1.execute("SELECT COUNT(EMPRESA) FROM datos WHERE estatus ='CLIENTE' and POBLACION = 'MADRID' ")

resultado8 = cursor1.fetchone()

totalClienteMadrid = resultado8[0]

print("La cantidad de cliente Madrid es: " + str(totalClienteMadrid))

#LO GUARDA EN EL CSV DEL ARCHIVO EXCEL
escritor.writerow([]) 
escritor.writerow(["", "", "", "", "ClientesTotal:", totalClientes])
escritor.writerow(["", "", "", "", "Facturacion Total:", totalFacturacion])
escritor.writerow(["", "", "", "", "Numero Facturacion Proveedores:", totalProveedor])
escritor.writerow(["", "", "", "", "Numero Total de Proveedores:", totalProveedorStatus])
escritor.writerow(["", "", "", "", "Beneficio Total:", totalBeneficio])
escritor.writerow(["", "", "", "", "Numero Total Clientes Morosos:", totalClientesMorosos])
escritor.writerow(["", "", "", "", "Facturacion Cliente:", totalMediaClientes])
escritor.writerow(["", "", "", "", "Numero Total Proveedor Morosos:", totalProveedorMoroso])
escritor.writerow(["", "", "", "", "Numero Total cliente Madrid:", totalClienteMadrid])
archivo.close()
conexion1.close()

print("Archivo guardado en: " + ruta)
print("Conexion cerrada")