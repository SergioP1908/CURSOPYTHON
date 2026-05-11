'''I. Escribe un programa que pregunte al usuario los dos lados de un rectángulo y presente 
por pantalla el cálculo del perímetro (suma de los lados) y el área (base por altura) redondeando a dos decimales.'''

ladoAncho = input("Ingresa el lado ancho del rectangulo: ")
ladoLargo = input("Ingresa el lado largo del rectangulo: ")

if (ladoAncho !="" and ladoLargo !=""):
    perimetro = 2*(int(ladoAncho) + int(ladoLargo))
    area = int(ladoAncho) * int(ladoLargo)

    print("******************************************"+"\nEl perimetro de rectangulo es: "+str(perimetro)+
          "\nEl area del rectangulo es: "+str(area))
else:
    print("No se pueden dejar campos vacios")
   

