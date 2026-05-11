'''I. Suponiendo que pi = 3.1416, escribe un programa que pida al usuario que 
introduzca el radio, y presente por pantalla el cálculo del perímetro de la 
circunferencia (P=2*pi*r), el área del círculo (A=pi*r2), y el volumen de la esfera (V = (4*pi*r3)/3) 
redondeando a dos decimales.'''

pi = 3.1416

radio = input("Ingresa el radio: ")

if radio != "":
    radio = float(radio)

    perimetro = 2 * pi * radio
    area = pi * (radio ** 2)
    volumen = (4 * pi * (radio ** 3)) / 3

    print("Perimetro de la circunferencia: " + str(round(perimetro, 2)))
    print("Area del circulo: " + str(round(area, 2)))
    print("Volumen de la esfera: " + str(round(volumen, 2)))
else:
    print("No puedes dejar el campo vacio")