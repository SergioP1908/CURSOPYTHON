
import os
import random

# Ejemplo: Crear un array de numeros cuadrados perfectos, pidiendole al usuario 
# un tamaño positivo, inferior a 20 posiciones.


# While: se usa principalmente para generar bucles indeterminados o variables

while True:

    
    os.system("cls")

    # tamanyo = 0

    # while (tamanyo < 1) or (tamanyo > 20):
    #    tamanyo = int(input("Introduce un numero positivo mayor que 1 y menor o igual a 20: "))

    tamanyo = random.randint(1, 20)

    numeros = []

    numeros = list()

    # numeros = [2,6,8,9,7,5,3]

    # numeros = list([2,6,8,9,7,5,3])

    for indice in range(tamanyo):
        valor = (indice+1)**2
        numeros.append(valor)

    print(numeros)


    while True:
        buscar = int(input("Introduce un numero positivo mayor que 1 y menor o igual a " + str(max(numeros)) + ": "))

        if buscar >= 1 and buscar <= max(numeros):
            break
        
    if buscar in numeros:
        print("El número " + str(buscar) + " esta en la lista y es un cuadrado perfecto")
    else:
        print("El número " + str(buscar) + " no es un cuadrado perfecto")

    repetir = input("Quieres repetir el programa? (s/n): ")

    if (repetir == "n"):
        break
