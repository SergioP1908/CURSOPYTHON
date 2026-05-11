'''I. Suponiendo que 1 euro = 1.33250 dólares, escribe un programa que pida 
al usuario un número de dólares y calcule el cambio en euros redondeando a 
dos decimales. Después pedirá al usuario un número de euros y calculará el 
cambio en dólares redondeando a dos decimales.'''

cambio = 1.33250

dolares = input("Ingresa la cantidad de dolares: ")

if dolares != "":
    euros = float(dolares) / cambio

    print("El cambio a euros es: " + str(round(euros, 2)))
else:
    print("No puedes dejar el campo vacio")


euros = input("Ingresa la cantidad de euros: ")

if euros != "":
    dolares = float(euros) * cambio

    print("El cambio a dolares es: " + str(round(dolares, 2)))
else:
    print("No puedes dejar el campo vacio")