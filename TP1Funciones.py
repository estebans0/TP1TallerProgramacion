# Elaborado por Juan Ceballos y Esteban Solano
# Fecha de Creación: 03/04/2022 01:20pm
# Fecha de última Modificación: 11/04/2022 05:57pm
# Versión: 3.9.2

# Definición de Funciones
def palabraInv(ppalabra):
    palabraInv = ""
    indice = -1
    for i in ppalabra:
        palabraInv += ppalabra[indice]
        indice -= 1
    return palabraInv

def mensajeInv(pfrase):
    mensajeInv = ""
    indice = -1
    frase = pfrase.split(" ")
    for i in frase:
        mensajeInv += str(palabraInv(frase[indice]))+" "
        indice -= 1
    return mensajeInv

def cifBinario(pfrase):
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