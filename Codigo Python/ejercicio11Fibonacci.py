'''Realizar un programa que imprima por pantalla tantos números 
de la serie de Fibonacci como diga el usuario. Se puede usar un 
array o no, a criterio del programador. Al ejecutarse debe 
preguntar “Cuantos números desea imprimir? (mínimo 2 números)”, 
leer el número que introduce el usuario e imprimir la serie numérica 
EN HORIZONTAL. El número deberá ser positivo y mayor que 2. Si no cumple 
los requisitos el programa seguirá pidiendo un número.
'''

n = int(input("Cuantos numeros desea imprimir? (minimo 2 numeros): "))

while n < 2:
    n = int(input("Error. Debe ser mayor o igual a 2. Intente de nuevo: "))

a = 0
b = 1

print("Serie de Fibonacci:")

if n >= 1:
    print(a, end=" ")
if n >= 2:
    print(b, end=" ")

for i in range(3, n + 1):
    c = a + b
    print(c, end=" ")
    a = b
    b = c