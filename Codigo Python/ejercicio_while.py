def usuario():
    nomUsuario = input("Introduce un nombre de usuario: ")
    nomUsuario = str(nomUsuario)
    return nomUsuario

def contrasena():
    numContrasena = input("Introduce la contraseña: ")
    numContrasena = str(numContrasena)
    return numContrasena

print("**********************INICIA*********************")

print("\n***********************************************")

usuarioInicial=usuario()
contrasenaInicial=contrasena()
#tamano= len (contrasena)

primerUsuario = usuarioInicial
primerContrasena = contrasenaInicial
minisculas = [char for char in contrasenaInicial if char.islower()]
cuantasmin = len(minisculas)

while (len(contrasenaInicial) <8 or cuantasmin<1):
    print("Contraseña Incorrecta, vuelve a introducir la contraseña")
    #tamano= len (contrasenaInicial)
    minisculas = [char for char in contrasenaInicial if char.islower()]
    cuantasmin = len(minisculas)
    print(str(cuantasmin))
    contrasenaInicial=contrasena()

 
if (contrasenaInicial.isupper):
    print("Contraseña correcta")
else:
    print("Vuelve aintroducir la contraseña")
print("fin de bucle")

print("Su primer usuario era : "+ primerUsuario +"\nSu primera contraseña era : " +primerContrasena)

minisculas = [char for char in contrasenaInicial if char.islower()]
cuantasmin = len(minisculas)
print(cuantasmin)