'''I. Escribe un programa que pida al usuario que introduzca los segundos, y le conteste 
diciéndole el número de días, horas, minutos y segundos que son.'''

segundos = input("Ingresa la cantidad de segundos: ")

if segundos != "":

    segundos = int(segundos)

    dias = segundos // 86400
    resto = segundos % 86400

    horas = resto // 3600
    resto = resto % 3600

    minutos = resto // 60
    segundos = resto % 60

    print("Dias: " + str(dias))
    print("Horas: " + str(horas))
    print("Minutos: " + str(minutos))
    print("Segundos: " + str(segundos))

else:
    print("No puedes dejar el campo vacio")