'''I. Realizar un programa que pida por pantalla un nombre de usuario y una contraseña. El nombre del usuario será 
cualquiera, pero la contraseña deberá tener las siguientes características mínimas:

Deberá tener mínimo 8 caracteres.
Deberá incluir al menos una letra mayúscula.
Deberá incluir al menos una letra minúscula.
Deberá incluir al menos un número.
Si no se cumplen los requisitos el programa seguirá pidiendo una contraseña nueva.

II. A continuación se le preguntará qué datos quiere cambiar mediante una letra. Si elige la letra n se cambiará 
el nombre, si elige la letra c se cambiará la contraseña, y si elige la letra t se cambiará tanto el nombre como 
la contraseña. Al final del programa se mostrarán tanto el nombre y la contraseña originales como los cambiados.

'''
def usuario():
    while True:
        nomUsuario = input("Introduce un nombre de usuario: ").strip()
        if nomUsuario == "":
            print("El usuario no puede estar vacío. Inténtalo de nuevo.")
        else:
            return nomUsuario

def contrasena():
    while True:
        numContrasena = input("\nIntroduce la contraseña: ").strip()
        if numContrasena == "":
            print("La contraseña no puede estar vacía.")
        else:
            print("\n***********************************************************")
            return numContrasena

def comprobarContrasena(): #Valida la contraseña , si no tiene mas de 8 letras, que tenga 1 minus, 1 Mayus y 1 numero
    validarContrasena = False
    while (validarContrasena == False):
        contrasenaInicial=contrasena()
        minusculas = [letra for letra in contrasenaInicial if letra.islower()]
        mayusculas = [letra for letra in contrasenaInicial if letra.isupper()]
        numero = [letra for letra in contrasenaInicial if letra.isdigit()]
        if len (contrasenaInicial)<8 or len(minusculas)<1 or len(mayusculas)<1 or len(numero)<1:
            print("La longitud de tu contraseña es : "+ str(len(contrasenaInicial)))
            print("La cantidad de MINISCULAS en tu contraseña es : "+str (len(minusculas)))
            print("La cantidad de MAYUSCULAS en tu contraseña es : "+str (len(mayusculas)))
            print("La cantidad de NUMEROS en tu contraseña es : "+str (len(numero)))
            print("\nCONTRASEÑA INCORRECTA, VUELVE A INTRODUCIR LA CONTRASEÑA")
            print("************************************************************")

        else:
            validarContraseña=True
            print("TU CONTRASEÑA SE HA AÑADIDO CORRECTAMENTE")
            return contrasenaInicial

  
print("**********************INICIA*********************")

#EJECUTA EL CODIGO PIDIENDO EL NOMBRE
usuarioInicial=usuario()
#contrasenaInicial=contrasena()
#EJECUTA EL CODIGO PIDIENDO LA CONTRASEÑA Y VALIDANDOLA
primerContrasena=comprobarContrasena()

    #tamano= len (contrasenaInicial)
    #minisculas = [char for char in contrasenaInicial if char.islower()]
    #cuantasmin = len(minisculas)
    #print(str(cuantasmin))
    #contrasenaInicial=contrasena()
#print("fin de bucle")
print("\nUsuario: "+usuarioInicial)
print("\nContraseña: "+primerContrasena)

usuarioOriginal = usuarioInicial
contrasenaOriginal = primerContrasena

print("\n*************************MENU*************************")
 
opcion = input("¿Quieres modificar algun dato introducido?\nn: Modificar Usuario\nc: Modificar Contraseña\nt: Modificar Usuario y Contraseña\n").lower()

match opcion:
    case "n":
        usuarioInicial = usuario()
        #usuarioNuevo = usuarioInicial
        print("Tu anterior usuario era: "+usuarioOriginal+"\nTu nuevo usuario es: "+usuarioInicial)
        
    case "c":
        nuevaContrasena = comprobarContrasena()
        #ultimaContrasena = nuevaContrasena
        print("Tu anterior contraseña era: "+contrasenaOriginal+"\nTu nueva contraseña es: "+nuevaContrasena)

    case "t":
        usuarioInicial = usuario()
        #usuarioNuevo = usuarioInicial
        nuevaContrasena = comprobarContrasena()
        #ultimaContrasena = nuevaContrasena
        print("\nTu anterior usuario era: "+usuarioOriginal+"\nTu nuevo usuario es: "+usuarioInicial)
        print("Tu anterior contraseña era: "+contrasenaOriginal+"\nTu nueva contraseña es: "+nuevaContrasena)

    case _:
        print("OPCION NO VALIDA")

#print("Su primer usuario era : "+ primerUsuario +"\nSu primera contraseña era : " +primerContrasena)

