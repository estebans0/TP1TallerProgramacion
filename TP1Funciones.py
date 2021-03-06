# Elaborado por Juan Ceballos y Esteban Solano
# Fecha de Creación: 03/04/2022 01:20pm
# Fecha de última Modificación: 30/04/2022 07:45am
# Versión: 3.9.2

# Importación de librerías
import secrets

# Librería de funciones
def esPar(pnum):
    """
    Funcionalidad: Determina si un número entero es par o impar.
    Entradas:
    -pnum(int): El número ingresado por el usuario para ser validado.
    Salidas:
    -True(bool): Indica que el número es par.
    -False(bool): Indica que el número es impar.
    """
    if pnum % 2 == 0:
        return True
    else:
        return False

# Definición de Funciones
def cifCesar(pfrase):
    """
    Funcionalidad: Crea un cifrado al adelantar las letras del mensaje 3 posiciones.
    Entradas:
    -pfrase(str): El mensaje a ser cifrado.
    Salidas:
    -cifrado(str): El mensaje convertido a cifrado.
    """
    pfrase = pfrase.upper()
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cifrado = ""
    for i in pfrase:
        letraPos = 0
        for j in alfabeto: # Determina la posición de cada letra de la frase en el alfabeto y le asigna un valor numérico
            if i == j:
                break
            letraPos += 1
        if i in alfabeto:
            if letraPos > 25: # En caso de superar la cantidad de letras del alfabeto, restar 26
                letraPos -= 26
            cifrado += alfabeto[letraPos+3] # Añade al cifrado la posicion la letra + 3
        else: # Añade al cifrado un espacio en blanco y reseta el indice
            cifrado += " "
    return cifrado

def descifCesar(pcifrado):
    """
    Funcionalidad: Descifra el cifrado del cifrado por llave al retroceder 3 posiciones las letras del cifrado.
    Entradas:
    -pcifrado(str): El mensaje a ser descifrado.
    Salidas:
    -frase(str): El mensaje descifrado.
    """
    pcifrado = pcifrado.lower()
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    frase = ""
    for i in pcifrado:
        letraPos = 0
        for j in alfabeto: # Determina la posición de cada letra de la frase en el alfabeto y le asigna un valor numérico
            if i == j:
                break
            letraPos += 1
        if i in alfabeto:
            if letraPos > 25: # En caso de superar la cantidad de letras del alfabeto, restar 26
                letraPos -= 26
            frase += alfabeto[letraPos-3] # Añade al cifrado la posicion la letra - 3
        else: # Añade al cifrado un espacio en blanco y reseta el indice
            frase += " "
    return frase

def cifPorLlave(pfrase, pllave):
    """
    Funcionalidad: Crea un cifrado al adelantar las letras del mensaje según el valor de una llave (palabra clave).
    Entradas:
    -pfrase(str): El mensaje a ser cifrado.
    -pllave(str): La palabra clave que definirá cuantos espacios se deben adelantar las letras del mensaje.
    Salidas:
    -cifrado(str): El mensaje convertido a cifrado según la llave.
    """
    pfrase = pfrase.lower()
    letraPos = 0
    llaveValor = 0
    indice = 0
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cifrado = ""
    for i in pfrase:
        letraPos = 0
        llaveValor = 0
        if indice == len(pllave): # Si el indice de la llave es igual a su longitud se resetea
            indice = 0
        for j in alfabeto: # Determina la posición de cada letra de la frase en el alfabeto y le asigna un valor numérico
            if i == j:
                break
            letraPos += 1
        for j in alfabeto: # Determina el valor de la letra de la llave
            llaveValor += 1
            if pllave[indice] == j:
                break
        if i in alfabeto: # Verifica si el caracter evaluado se encuentra dentro del alfabeto
            letraPos += llaveValor
            indice += 1
            if letraPos > 25: # En caso de superar la cantidad de letras del alfabeto, restar 26
                letraPos -= 26
            cifrado += alfabeto[letraPos] # Añade al cifrado la posicion la letra + el valor de la llave
        else: # Añade al cifrado un espacio en blanco y reseta el indice
            cifrado += " "
            indice = 0
    return cifrado

def descifPorLlave(pcifrado, pllave):
    """
    Funcionalidad: Descifra el cifrado del cifrado por llave al retroceder las letras del cifrado según la llave.
    Entradas:
    -pcifrado(str): El mensaje a ser descifrado.
    -pllave(str): La palabra clave que definirá cuantos espacios se deben retroceder las letras del mensaje.
    Salidas:
    -frase(str): El mensaje descifrado.
    """
    letraPos = 0
    llaveValor = 0
    indice = 0
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    frase = ""
    for i in pcifrado:
        letraPos = 0
        llaveValor = 0
        if indice == len(pllave): # Si el indice de la llave es igual a su longitud se resetea
            indice = 0
        for j in alfabeto: # Determina la posición de cada letra de la frase en el alfabeto y le asigna un valor numérico
            if i == j:
                break
            letraPos += 1
        for j in alfabeto: # Determina el valor de la letra de la llave
            llaveValor += 1
            if pllave[indice] == j:
                break
        if i in alfabeto: # Verifica si el caracter evaluado se encuentra dentro del alfabeto
            letraPos -= llaveValor
            indice += 1
            if letraPos > 25: # En caso de superar la cantidad de letras del alfabeto, restar 26
                letraPos -= 26
            frase += alfabeto[letraPos] # Añade al cifrado la posicion la letra + el valor de la llave
        else: # Añade al cifrado un espacio en blanco y reseta el indice
            frase += " "
            indice = 0
    return frase

def sustVignere(pfrase, pcifra):
    """
    Funcionalidad: Crea un cifrado al adelantar alternadamente las letras del mensaje según el valor de una cifra numérica.
    Entradas:
    -pfrase(str): El mensaje a ser cifrado.
    -pcifra(int): La cifra numérica que definirá cuantos espacios se deben adelantar las letras del mensaje.
    Salidas:
    -cifrado(str): El mensaje convertido a cifrado según la cifra numérica.
    """
    pfrase = pfrase.lower()
    cifra = str(pcifra)
    letraPos = 0
    contador = 1
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cifrado = ""
    for i in pfrase:
        letraPos = 0
        for j in alfabeto: # Determina la posición de cada letra de la frase en el alfabeto
            if i == j:
                break
            letraPos += 1
        if letraPos > 25: # En caso de superar la cantidad de letras del alfabeto, restar 26
            letraPos -= 26
        if i in alfabeto: # Determina si la letra es par o impar para saber cual cifra utilizar
            if esPar(contador) == False:
                letraPos += int(cifra[0])
            elif esPar(contador) == True:
                letraPos += int(cifra[-1])
            contador += 1
            cifrado += alfabeto[letraPos] # Añade al cifrado la posicion de cada letra obtenida en el alfabeto + el digito de la cifra
        else: # Añade al cifrado un espacio en blanco
            cifrado += " "
    return cifrado

def descifSustVignere(pcifrado, pcifra):
    """
    Funcionalidad: Descifra el cifrado de la sustitución Vignére al retroceder las letras del cifrado según la cifra numérica.
    Entradas:
    -pcifrado(str): El mensaje a ser descifrado.
    -pllave(str): La palabra clave que definirá cuantos espacios se deben retroceder las letras del mensaje.
    Salidas:
    -frase(str): El mensaje descifrado.
    """
    cifra = str(pcifra)
    letraPos = 0
    contador = 1
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    frase = ""
    for i in pcifrado:
        letraPos = 0
        for j in alfabeto: # Determina la posición de cada letra de la frase en el alfabeto
            if i == j:
                break
            letraPos += 1
        if letraPos > 25: # En caso de superar la cantidad de letras del alfabeto, restar 26
            letraPos -= 26
        if i in alfabeto: # Determina si la letra es par o impar para saber cual cifra utilizar
            if esPar(contador) == False:
                letraPos -= int(cifra[0])
            elif esPar(contador) == True:
                letraPos -= int(cifra[-1])
            contador += 1
            frase += alfabeto[letraPos] # Añade al cifrado la posicion de cada letra obtenida en el alfabeto + el digito de la cifra
        else: # Añade al cifrado un espacio en blanco
            frase += " "
    return frase

def xorYLlave(pfrase, pllave):
    """
    Funcionalidad: Crea un cifrado usando el método XOR y llave.
    Entradas:
    -pfrase(str): El mensaje a ser cifrada.
    -pllave(str): La palabra clave la cual servirá para realizar el calculo XOR.
    Salidas:
    -(str): El cifrado.
    """
    asciiAXor = 0
    indiceLlave = 0
    cifrado = []
    for i in range(len(pfrase)):
        asciiAXor = ord(pfrase[i]) ^ ord(
            pllave[indiceLlave])  # Convierte las entradas tipo string a sus valores ASCII y realiza la operación ^.
        indiceLlave += 1
        cifrado += chr(asciiAXor)
        if indiceLlave >= len(pllave):  # Resetea el valor de la llave una vez haya alcanzado su largo.
            indiceLlave = 0
    return cifrado

def palabraInv(ppalabra): # Se puede reutilizar función para el descifrado
    """
    Funcionalidad: Crea un cifrado al invertir el orden de las palabras.
    Entradas:
    -ppalabra(str): La palabra a ser cifrada.
    Salidas:
    -cifrado(str): La palabra inversa.
    """
    cifrado = ""
    indice = -1
    ppalabra = ppalabra.split(" ")
    for i in ppalabra:
        while indice >= -len(i):
            cifrado += i[indice]
            indice -= 1
        indice = -1
        cifrado += " "
    return cifrado

def mensajeInv(pfrase): # Se puede reutilizar función para el descifrado
    """
    Funcionalidad: Crea un cifrado al invertir el mensaje ingresado.
    Entradas:
    -pfrase(str): El mensaje a ser cifrado.
    Salidas:
    -cifrado(str): El mensaje inverso.
    """
    cifrado = ""
    indice = -1
    for i in pfrase:
        cifrado += pfrase[indice]
        indice -= 1
    return cifrado

def cifBinario(pfrase):
    """
    Funcionalidad: Crea un cifrado al convertir la frase ingresada a valores binarios.
    Entradas:
    -pfrase(str): El mensaje a ser cifrado.
    Salidas:
    -cifrado(str): El mensaje convertido a binario.
    """
    pfrase = pfrase.lower()
    cifrado = ""
    for i in pfrase:
        for j in i:
            if j == " ":
                cifrado += "* "
            elif j == "a":
                cifrado += "00000 "
            elif j == "b":
                cifrado += "00001 "
            elif j == "c":
                cifrado += "00010 "
            elif j == "d":
                cifrado += "00011 "
            elif j == "e":
                cifrado += "00100 "
            elif j == "f":
                cifrado += "00101 "
            elif j == "g":
                cifrado += "00110 "
            elif j == "h":
                cifrado += "00111 "
            elif j == "i":
                cifrado += "01000 "
            elif j == "j":
                cifrado += "01001 "
            elif j == "k":
                cifrado += "01010 "
            elif j == "l":
                cifrado += "01011 "
            elif j == "m":
                cifrado += "01100 "
            elif j == "n":
                cifrado += "01101 "
            elif j == "o":
                cifrado += "01110 "
            elif j == "p":
                cifrado += "01111 "
            elif j == "q":
                cifrado += "10000 "
            elif j == "r":
                cifrado += "10001 "
            elif j == "s":
                cifrado += "10010 "
            elif j == "t":
                cifrado += "10011 "
            elif j == "u":
                cifrado += "10100 "
            elif j == "v":
                cifrado += "10101 "
            elif j == "w":
                cifrado += "10110 "
            elif j == "x":
                cifrado += "10111 "
            elif j == "y":
                cifrado += "11000 "
            elif j == "z":
                cifrado += "11001 "
    return cifrado

def descifBinario(pcifrado):
    """
    Funcionalidad: Descifra el cifrado del cifrado binario.
    Entradas:
    -pcifrado(str): El mensaje cifrado en binario.
    Salidas:
    -frase(str): El mensaje descifrado.
    """
    frase = ""
    cifrado = pcifrado.split(" ")
    for i in cifrado:
        if i == "*":
            frase += " "
        elif i == "00000":
            frase += "a"
        elif i == "00001":
            frase += "b"
        elif i == "00010":
            frase += "c"
        elif i == "00011":
            frase += "d"
        elif i == "00100":
            frase += "e"
        elif i == "00101":
            frase += "f"
        elif i == "00110":
            frase += "g"
        elif i == "00111":
            frase += "h"
        elif i == "01000":
            frase += "i"
        elif i == "01001":
            frase += "j"
        elif i == "01010":
            frase += "k"
        elif i == "01011":
            frase += "l"
        elif i == "01100":
            frase += "m"
        elif i == "01101":
            frase += "n"
        elif i == "01110":
            frase += "o"
        elif i == "01111":
            frase += "p"
        elif i == "10000":
            frase += "q"
        elif i == "10001":
            frase += "r"
        elif i == "10010":
            frase += "s"
        elif i == "10011":
            frase += "t"
        elif i == "10100":
            frase += "u"
        elif i == "10101":
            frase += "v"
        elif i == "10110":
            frase += "w"
        elif i == "10111":
            frase += "x"
        elif i == "11000":
            frase += "y"
        elif i == "11001":
            frase += "z"
    return frase

def cifCodTel(pfrase):
    """
    Funcionalidad: Crea un cifrado al asignar a cada letra un valor de código telefónico.
    Entradas:
    -pfrase(str): El mensaje a ser cifrado.
    Salidas:
    -cifrado(str): El mensaje convertido a cifrado.
    """
    pfrase = pfrase.lower()
    abecedario = ""
    cifrado = ""
    num = 0
    posLetra = 0
    for i in pfrase:
        if i in "abcdefghijklmnopqrstuvwxyz":
            posLetra = 0
            if i in "abc":
                abecedario = "abc"
                num = "2"
            elif i in "def":
                abecedario = "def"
                num = "3"
            elif i in "ghi":
                abecedario = "ghi"
                num = "4"
            elif i in "jkl":
                abecedario = "jkl"
                num = "5"
            if i in "mno":
                abecedario = "mno"
                num = "6"
            elif i in "pqrs":
                abecedario = "pqrs"
                num = "7"
            elif i in "tuv":
                abecedario = "tuv"
                num = "8"
            elif i in "wxyz":
                abecedario = "wxyz"
                num = "9"
            for j in abecedario:
                posLetra += 1
                if i == j:
                    break
            cifrado += num+str(posLetra)+" "
        elif i == " ":
            cifrado += "* "
    return cifrado

def descifCodTel(pcifrado):
    """
    Funcionalidad: Descifra el cifrado del cifrado por código telefónico.
    Entradas:
    -pcifrado(str): El mensaje cifrado en código telefónico.
    Salidas:
    -frase(str): El mensaje descifrado.
    """
    pcifrado = pcifrado.split(" ")
    abecedario = ""
    frase = ""
    posLetra = 0
    for i in pcifrado:
        if i.isdigit():
            posLetra = 0
            if i[0] == "2":
                abecedario = "abc"
            elif i[0] == "3":
                abecedario = "def"
            elif i[0] == "4":
                abecedario = "ghi"
            elif i[0] == "5":
                abecedario = "jkl"
            if i[0] == "6":
                abecedario = "mno"
            elif i[0] == "7":
                abecedario = "pqrs"
            elif i[0] == "8":
                abecedario = "tuv"
            elif i[0] == "9":
                abecedario = "wxyz"
            for j in abecedario:
                posLetra += 1
                if posLetra == int(i[1]):
                    break
            frase += j
        elif i == "*":
            frase += " "
    return frase