'''I. Escribe un programa que pida al usuario los siguientes datos: días, horas y minutos, 
y le conteste con la cantidad de segundos totales que son esos datos.'''

dias = input("Ingresa la cantidad de dias: ")
horas = input("Ingresa la cantidad de horas: ")
minutos = input("Ingresa la cantidad de minutos: ")

if dias != "" and horas != "" and minutos != "":
    
    dias = int(dias)
    horas = int(horas)
    minutos = int(minutos)

    segundosTotales = (dias * 86400) + (horas * 3600) + (minutos * 60)

    print("La cantidad total de segundos es: " + str(segundosTotales))

else:
    print("No puedes dejar campos vacios")