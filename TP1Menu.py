# Elaborado por Juan Ceballos y Esteban Solano
# Fecha de Creación: 11/04/2022 06:02pm
# Fecha de última Modificación: 30/04/2022 07:45am
# Versión: 3.9.2

# Importación de librerías
from TP1Funciones import *

# Definición de Validaciones
def cifCesarAux(pfrase):
    """
    Funcionamiento: Valida que la entrada cumpla con la condiciones necesarias.
    Entradas:
    -pfrase(str): El mensaje a ser cifrado.
    Salidas:
    cifCesar(): La salida de la función.
    (str): El mensaje de error correspondiente.
    """
    opcion = 0
    while opcion != 1 and opcion != 2:
        if isinstance(pfrase, str):
            print(f"\nSu cifrado es: {cifCesar(pfrase)}")
            opcion = int(input("\n¿Desea descifrar el mensaje (1) o regresar al menú principal (2)?: "))
            if opcion == 1:
                return f"\nSu descifrado es: {descifCesar(cifCesar(pfrase))}"
            elif opcion == 2:
                break
        return "Ingrese un mensaje válido."
    return ""

def cifPorLlaveAux(pfrase, pllave):
    """
    Funcionamiento: Valida que la entrada cumpla con la condiciones necesarias.
    Entradas:
    -pfrase(str): El mensaje a ser cifrado.
    -pllave(str): La palabra clave que definirá cuantos espacios se deben adelantar las letras del mensaje.
    Salidas:
    cifPorLlave(): La salida de la función.
    (str): El mensaje de error correspondiente.
    """
    opcion = 0
    while opcion != 1 and opcion != 2:
        if isinstance(pfrase, str):
            if isinstance(pllave, str):
                print(f"\nSu cifrado es: {cifPorLlave(pfrase, pllave)}")
                opcion = int(input("\n¿Desea descifrar el mensaje (1) o regresar al menú principal (2)?: "))
                if opcion == 1:
                    return f"\nSu descifrado es: {descifPorLlave(cifPorLlave(pfrase, pllave), pllave)}"
                elif opcion == 2:
                    break
            return "Ingrese una llave válida."
        return "Ingrese un mensaje válido."
    return ""

def sustVignereAux(pfrase, pcifra):
    """
    Funcionamiento: Valida que la entrada cumpla con la condiciones necesarias.
    Entradas:
    -pfrase(str): El mensaje a ser cifrado.
    -pcifra(int): La cifra numérica que definirá cuantos espacios se deben adelantar las letras del mensaje.
    Salidas:
    sustVignere(): La salida de la función.
    (str): El mensaje de error correspondiente.
    """
    opcion = 0
    while opcion != 1 and opcion != 2:
        if isinstance(pfrase, str):
            if isinstance(pcifra, int):
                print(f"\nSu cifrado es: {sustVignere(pfrase, pcifra)}")
                opcion = int(input("\n¿Desea descifrar el mensaje (1) o regresar al menú principal (2)?: "))
                if opcion == 1:
                    return f"\nSu descifrado es: {descifSustVignere(sustVignere(pfrase, pcifra), pcifra)}"
                elif opcion == 2:
                    break
            return "Ingrese una cifra numérica."
        return "Ingrese un mensaje válido."
    return ""

def xorYLlaveAux(pfrase, pllave):
    """
    Funcionamiento: Valida que la entrada cumpla con la condiciones necesarias.
    Entradas:
    pfrase(str): El mensaje ingresado por el usuario.
    pllave(str): La palabra clave la cual servirá para realizar el calculo XOR.
    Salidas:
    xorYLlave(): La salida de la función.
    (str): El mensaje de error correspondiente.
    """
    if isinstance(pfrase, str):
        if isinstance(pllave, str):
            return xorYLlave(pfrase, pllave)
        return "Ingrese una llave válida."
    return "Ingrese un mensaje válido."

def palabraInvAux(ppalabra):
    """
    Funcionamiento: Valida que la entrada cumpla con la condiciones necesarias.
    Entradas:
    ppalabra(str): La palabra ingresada por el usuario.
    Salidas:
    palabraInv(): La salida de la función.
    (str): El mensaje de error correspondiente.
    """
    opcion = 0
    while opcion != 1 and opcion != 2:
        if isinstance(ppalabra, str):
            print(f"\nSu cifrado es: {palabraInv(ppalabra)}")
            opcion = int(input("\n¿Desea descifrar el mensaje (1) o regresar al menú principal (2)?: "))
            if opcion == 1:
                return f"\nSu descifrado es: {palabraInv(palabraInv(ppalabra))}"
            elif opcion == 2:
                break
        return "\nIngrese una palabra válida."
    return ""

def mensajeInvAux(pfrase):
    """
    Funcionamiento: Valida que la entrada cumpla con la condiciones necesarias.
    Entradas:
    pfrase(str): La frase ingresada por el usuario.
    Salidas:
    mensajeInv(): La salida de la función.
    (str): El mensaje de error correspondiente.
    """
    opcion = 0
    while opcion != 1 and opcion != 2:
        if isinstance(pfrase, str):
            print(f"\nSu cifrado es: {mensajeInv(pfrase)}")
            opcion = int(input("\n¿Desea descifrar el mensaje (1) o regresar al menú principal (2)?: "))
            if opcion == 1:
                return f"\nSu descifrado es: {mensajeInv(mensajeInv(pfrase))}"
            elif opcion == 2:
                break
        return "Ingrese una frase válida."
    return ""

def cifBinarioAux(pfrase):
    """
    Funcionamiento: Valida que la entrada cumpla con la condiciones necesarias.
    Entradas:
    pfrase(str): La frase ingresada por el usuario.
    Salidas:
    cifBinario(): La salida de la función.
    (str): El mensaje de error correspondiente.
    """
    opcion = 0
    while opcion != 1 and opcion != 2:
        if isinstance(pfrase, str):
            print(f"\nSu cifrado es: {cifBinario(pfrase)}")
            opcion = int(input("\n¿Desea descifrar el mensaje (1) o regresar al menú principal (2)?: "))
            if opcion == 1:
                return f"\nSu descifrado es: {descifBinario(cifBinario(pfrase))}"
            elif opcion == 2:
                break
        return "Ingrese una frase válida."
    return ""

def cifCodTelAux(pfrase):
    """
    Funcionamiento: Valida que la entrada cumpla con la condiciones necesarias.
    Entradas:
    pfrase(str): La frase ingresada por el usuario.
    Salidas:
    cifCodTel(): La salida de la función.
    (str): El mensaje de error correspondiente.
    """
    opcion = 0
    while opcion != 1 and opcion != 2:
        if isinstance(pfrase, str):
            print(f"\nSu cifrado es: {cifCodTel(pfrase)}")
            opcion = int(input("\n¿Desea descifrar el mensaje (1) o regresar al menú principal (2)?: "))
            if opcion == 1:
                return f"\nSu descifrado es: {descifCodTel(cifCodTel(pfrase))}"
            elif opcion == 2:
                break
        return "Ingrese una frase válida."
    return ""

# Programa Principal
def opcionCifCesar():
    """
    Funcionamiento: Recibe la entrada para realizar el cifrado César.
    Salidas: NA
    """
    try:
        print ("\n------------------------")
        print ("Cifrado César")
        print ("------------------------")
        frase = input("Ingrese el mensaje que desea cifrar: ")
        return print(cifCesarAux(frase))
    except ValueError:
        return "Ingrese valores válidos."

def opcionCifPorLlave():
    """
    Funcionamiento: Recibe la entrada para realizar el cifrado por llave.
    Salidas: NA
    """
    try:
        print ("\n------------------------")
        print ("Cifrado por llave")
        print ("------------------------")
        frase = input("Ingrese el mensaje que desea cifrar: ")
        llave = input("Ingrese la llave que usará para cifrar su mensaje: ")
        return print(cifPorLlaveAux(frase, llave))
    except ValueError:
        return "Ingrese valores válidos."

def opcionSustVignere():
    """
    Funcionamiento: Recibe la entrada para realizar la sustitución Vignére.
    Entradas: NA
    Salidas: NA
    """
    try:
        print ("\n------------------------")
        print ("Sustitución Vignére")
        print ("------------------------")
        frase = input("Ingrese el mensaje que desea cifrar: ")
        cifra = int(input("Ingrese la cifra que usará para cifrar su mensaje: "))
        return print(sustVignereAux(frase, cifra))
    except ValueError:
        return "Ingrese valores válidos."

def opcionXorYLlave():
    """
    Funcionamiento: Recibe la entrada para realizar el cifrado XOR y llave.
    Entradas: NA
    Salidas: NA
    """
    try:
        print ("\n------------------------")
        print ("XOR y llave")
        print ("------------------------")
        frase = input("Ingrese el mensaje que desea cifrar: ")
        llave = input("Ingrese la llave que usará para cifrar su mensaje: ")
        return print(xorYLlaveAux(frase, llave))
    except ValueError:
        return "Ingrese un valor válido."

def opcionPalabraInv():
    """
    Funcionamiento: Recibe la entrada para realizar el cifrado de palabra inversa.
    Entradas: NA
    Salidas: NA
    """
    try:
        print ("\n------------------------")
        print ("Palabra inversa")
        print ("------------------------")
        palabra = input("Ingrese una palabra: ")
        return print(palabraInvAux(palabra))
    except ValueError:
        return "Ingrese una palabra válida."

def opcionMensajeInv():
    """
    Funcionamiento: Recibe la entrada para realizar el cifrado de mensaje inverso.
    Entradas: NA
    Salidas: NA
    """
    try:
        print ("\n------------------------")
        print ("Mensaje inverso")
        print ("------------------------")
        frase = input("Ingrese una frase: ")
        return print(mensajeInvAux(frase))
    except ValueError:
        return "Ingrese una frase válida."

def opcionCifBinario():
    """
    Funcionamiento: Recibe la entrada para realizar el cifrado binario.
    Entradas: NA
    Salidas: NA
    """
    try:
        print ("\n------------------------")
        print ("Cifrado binario")
        print ("------------------------")
        frase = input("Ingrese una frase: ")
        return print(cifBinarioAux(frase))
    except ValueError:
        return "Ingrese una frase válida."

def opcionCifCodTel():
    """
    Funcionamiento: Recibe la entrada para realizar el cifrado de código telefónico.
    Entradas: NA
    Salidas: NA
    """
    try:
        print ("\n------------------------")
        print ("Cifrado de código telefónico")
        print ("------------------------")
        frase = input("Ingrese una frase: ")
        return print(cifCodTelAux(frase))
    except ValueError:
        return "Ingrese una frase válida."

def menu():
    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario.
    Entradas: NA
    Salidas: Resultado según lo solicitado.
    """
    try:
        print("\n************************************")
        print("Tarea Programada 1")
        print("************************************")
        print("1. Cifrado César")
        print("2. Cifrado por llave")
        print("3. Sustitución Vignére")
        print("4. Sustitución XOR y llave")
        print("5. Palabra inversa")
        print("6. Mensaje inverso")
        print("7. Cifrado de código telefónico")
        print("8. Cifrado binario")
        print("0. Terminar")
        opcion = int(input("\nEscoja una opción: "))
        if opcion >=0 and opcion <=8:
            if opcion == 1:
                opcionCifCesar()
            elif opcion == 2 :
                opcionCifPorLlave()
            elif opcion == 3:
                opcionSustVignere()
            elif opcion == 4:
                opcionXorYLlave()
            elif opcion == 5:
                opcionPalabraInv()
            elif opcion == 6:
                opcionMensajeInv()
            elif opcion == 7:
                opcionCifCodTel()
            elif opcion == 8:
                opcionCifBinario()
            else:
                print("\n¡Muchas gracias por usar el sistema!")
                return
        else:
            print ("Opción inválida, indique una opción según las opciones indicadas.")
        menu()
    except ValueError:
        print("Debe ingresar únicamente un valor numérico entero entre 0 y 8.")

#Programa Principal
menu()