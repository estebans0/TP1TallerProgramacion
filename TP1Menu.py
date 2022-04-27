# Elaborado por Juan Ceballos y Esteban Solano
# Fecha de Creación: 11/04/2022 06:02pm
# Fecha de última Modificación: 11/04/2022 02:13pm
# Versión: 3.9.2

# Importación de librerías
from TP1Funciones import *

# Definición de Validaciones
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
    if isinstance(pfrase, str):
        if isinstance(pllave, str):
            return cifPorLlave(pfrase, pllave)
        return "Ingrese una llave válida."
    return "Ingrese un mensaje válido."

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
    if isinstance(pfrase, str):
        if isinstance(pcifra, int):
            return sustVignere(pfrase, pcifra)
        return "Ingrese una cifra numérica."
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
    if isinstance(ppalabra, str):
        return palabraInv(ppalabra)
    return "Ingrese una palabra válida."

def mensajeInvAux(pfrase):
    """
    Funcionamiento: Valida que la entrada cumpla con la condiciones necesarias.
    Entradas:
    pfrase(str): La frase ingresada por el usuario.
    Salidas:
    mensajeInv(): La salida de la función.
    (str): El mensaje de error correspondiente.
    """
    if isinstance(pfrase, str):
        return mensajeInv(pfrase)
    return "Ingrese una frase válida."

def cifBinarioAux(pfrase):
    """
    Funcionamiento: Valida que la entrada cumpla con la condiciones necesarias.
    Entradas:
    pfrase(str): La frase ingresada por el usuario.
    Salidas:
    cifBinario(): La salida de la función.
    (str): El mensaje de error correspondiente.
    """
    if isinstance(pfrase, str):
        return cifBinario(pfrase)
    return "Ingrese una frase válida."

# Programa Principal
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
        return "Ingrese unvalores válidos."

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

def menu():
    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario.
    Entradas: NA
    Salidas: Resultado según lo solicitado.
    """
    print("\n**************************")
    print("Tarea Programada 1")
    print("**************************")
    print("1. Cifrado César")
    print("2. Cifrado por llave")
    print("3. Sustitución Vignére")
    print("4. Sustitución XOR y llave")
    print("5. Palabra inversa")
    print("6. Mensaje inverso")
    print("7. Cifrado telefónico")
    print("8. Cifrado binario")
    print("0. Terminar")
    opcion = int(input("\nEscoja una opción: "))
    if opcion >=0 and opcion <=8:
        if opcion == 1:
            "En desarrollo..."
        elif opcion == 2 :
            opcionCifPorLlave()
        elif opcion == 3:
            opcionSustVignere()
        elif opcion == 4:
            "En desarrollo..."
        elif opcion == 5:
            opcionPalabraInv()
        elif opcion == 6:
            opcionMensajeInv()
        elif opcion == 7:
            "En desarrollo..."
        elif opcion == 8:
            opcionCifBinario()
        else:
            return
    else:
        print ("Opción inválida, indique una opción según las opciones indicadas.")
    menu()

#Programa Principal
menu()