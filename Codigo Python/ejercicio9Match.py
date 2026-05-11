'''I. Realizar un programa usando SWITCH (MATCH) que pregunte al usuario el 
momento del día con una letra (m-mañana, t-tarde, n-noche), el sexo con otra 
letra (m-masculino, f-femenino). El programa dirá: buenos días, tardes, o noches 
(según el momento) señor o señora (según el sexo).'''

momento = input("Ingresa momento del dia (m-mañana, t-tarde, n-noche): ")
sexo = input("Ingresa sexo (m-masculino, f-femenino): ")

match momento:
    case "m":
        saludo = "Buenos días"
    case "t":
        saludo = "Buenas tardes"
    case "n":
        saludo = "Buenas noches"
    case _:
        saludo = "Dato no valido"

match sexo:
    case "m":
        persona = "señor"
    case "f":
        persona = "señora"
    case _:
        persona = "persona"

print(saludo + " " + persona)