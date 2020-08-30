import string
from Lexema import *
from tkinter import messagebox 

class Analisis_CSS(object):
    """description of class"""
    Token = list()
    Reservada = ["color", "background-color", "background-image", "border", "Opacity", "background", "text-align", "font-family", "font-style", "font-weight", "font-size", "font", "padding-left", "padding-right", "padding-bottom", "padding-top", "padding", "display", "line-height", "width", "height", "margin-top", "margin-right", "margin-bottom", "margin-left", "margin", "border-style", "display", "position", "bottom", "top", "right", "left", "float", "clear", "max-width", "min-width", "max-height", "min-height"]
    
    def Analisis(self, entrada):
        self.Token.clear()
        estado = 1
        numToken = 1
        palabra = ""
        en = str(entrada)
        lineas = en.split('\n')
        fila = 0
        while fila < len(lineas):
            primero = ""
            letra = list(lineas[fila])
            columna = 0
            while columna < len(letra):

                if estado == 1:
                    if letra[columna] != ' ' and letra[columna] != '\n' and letra[columna] != '\t':
                        palabra += letra[columna]

                    if letra[columna] == '/':
                        estado = 2
                        columna += 1

                    if letra[columna].isalpha():
                        estado = 3
                        columna += 1

                    if letra[columna].isnumeric():
                        estado = 4
                        columna += 1

                    if letra[columna] == '#':
                        estado = 6
                        columna += 1

                    if letra[columna] == '\"':
                        estado = 7
                        columna += 1

                    if estado <= 1:
                        self.agregar(numToken, fila, columna, palabra, "Es un Simbolo")
                        numToken+=1
                        palabra = ""
                        estado = 1

                if estado == 2:
                    if letra[columna] == '*':
                        estado = 8
                        primero = "no"

                if estado == 3:
                    if letra[columna].isalpha():
                        palabra += letra[columna]

                    elif letra[columna].isnumeric() or letra[columna] == '-' or letra[columna] == '_':
                        estado = 9

                    else:




                if estado == 4:

                if estado == 5:

                if estado == 6:

                if estado == 7:

                if estado == 8:

                if estado == 9:

                if estado == 10:

                if estado == 11:

                if estado == 12:

                if estado == 13:

                if estado == 14:

                if estado == 15:

                if estado == 16:

                if estado == 17:

                if estado == 18:


                columna += 1

            fila += 1

    def agregar(self,num, fila , columna, lex, des):
        nuevo = Lexema(num, fila, columna, lex, des)
        self.Token.append(nuevo)


