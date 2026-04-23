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
print(usuarioInicial + contrasenaInicial)

while (len(contrasenaInicial) <8):
    tamano= len (contrasenaInicial)
    print(str(tamano))
    contrasenaInicial=contrasena()
    print(contrasenaInicial)

print("fin de bucle")

print("Su primer usuario era : "+ primerUsuario +"\nSu primera contraseña era : " +primerContrasena)