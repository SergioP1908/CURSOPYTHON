'''I. Realizar un programa que pregunte al usuario el momento del día 
con una letra (m-mañana, t-tarde, n-noche), el sexo con otra letra 
(m-masculino, f-femenino). El programa dirá: buenos días, tardes, o noches 
(según el momento) señor o señora (según el sexo).'''

momento = input("Ingresa momento del dia (m-mañana, t-tarde, n-noche): ")
sexo = input("Ingresa sexo (m-masculino, f-femenino): ")

if momento == "m":
    if sexo == "m":
        print("Buenos días señor")
    else:
        print("Buenos días señora")

elif momento == "t":
    if sexo == "m":
        print("Buenas tardes señor")
    else:
        print("Buenas tardes señora")

elif momento == "n":
    if sexo == "m":
        print("Buenas noches señor")
    else:
        print("Buenas noches señora")

else:
    print("Dato ingresado no valido")