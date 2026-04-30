import random

numeros = []
tamano = 10

for numRandom in range(tamano):
    ingresarNum=random.randint(-100, 100)
    if(ingresarNum!=0 and ingresarNum not in numeros):
     numeros.append(ingresarNum)

print(numeros)

#Numero menor introducido
menor =min(numeros)
#numero mayor introducido
mayor = max (numeros)
#suma de todos los numeros
sumTotal = sum (numeros)
#media de los numeros introducidos
media = sumTotal/len(numeros)
#Mostrar resultado en consola
print("El numero menor es: "+ str(menor))
print("El numero mayor es: "+ str(mayor))
print("La suma total de todos los numeros es: "+ str(sumTotal))
print("La media de los numeros es: "+ str(media))

sumaPositivos = sum(num for num in numeros if num >0)
print("La suma de numeros positivos es: "+str(sumaPositivos))

sumaNegativos = sum(num for num in numeros if num <0)
print("La suma de numeros negativos es: "+ str(sumaNegativos))

numeros.sort()
print(numeros)