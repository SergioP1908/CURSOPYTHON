import os
os.system("cls")

# Los bucles son partes del programa que se repiten

# Podemos encontrarnos con dos tipos de bucles:

# Los bucles finitos o determinados: aquellos que se repiten un numero 
# fijo de veces. Se construyen con FOR.

# Los bucles no finitos o indeterminados: aquellos que se repiten un numero 
# variable de veces. Se construyen con WHILE.

numero = input("Introduce un numero par distinto de cero: ")
numero = int(numero)        # 3

resto = numero % 2          # 1

while ((numero == 0) or (resto != 0)):
    print("No has escrito un numero correcto")
    numero = input("Introduce un numero par distinto de cero: ")
    numero = int(numero)       # 4
    resto = numero % 2          # 0


print("El numero " + str(numero) + " es par y distinto de cero.")

