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
                    ver = ""

                    if letra[columna] != ' ' and letra[columna] != '\n' and letra[columna] != '\t':
                        palabra += letra[columna]

                    if letra[columna] == '/':
                        estado = 2
                        columna += 1
                        palabra = ""
                        ver = "en"

                    if letra[columna].isalpha() and ver == "":
                        estado = 3
                        columna += 1
                        ver = "en"

                    if letra[columna].isnumeric() and ver == "":
                        estado = 4
                        columna += 1
                        ver = "en"

                    if letra[columna] == '#' and ver == "":
                        estado = 6
                        columna += 1
                        ver = "en"

                    if letra[columna] == '\"' and ver == "":
                        estado = 7
                        columna += 1
                        ver = "en"


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
                    ver = ""
                    if letra[columna].isalpha():
                        palabra += letra[columna]
                        ver = "en"

                    elif letra[columna].isnumeric() or letra[columna] == '-' or letra[columna] == '_':
                        
                        palabra += letra[columna]
                        estado = 9
                        columna +=1
                        ver = "en"

                    elif ver == "":
                        if palabra in self.Reservada:
                            self.agregar(numToken, fila, columna, palabra, "Es una Palabra reservada")
                            numToken+=1
                            palabra = ""
                            estado = 1
                            columna -= 1
                        else:
                            self.agregar(numToken, fila, columna, palabra, "Es un ID")
                            numToken+=1
                            palabra = ""
                            estado = 1
                            columna -= 1

                if estado == 4:
                    ver = ""
                    if letra[columna].isnumeric(): 
                        palabra += letra[columna]
                        ver = "en"
                    if letra[columna] == '.':
                        estado = 11
                        columna += 1
                        ver = "en"
                        palabra += letra[columna]
                    if letra[columna].isalpha():
                        palabra += letra[columna]
                        estado = 10
                        columna += 1
                        ver = "en"
                    if letra[columna] == '%':
                        self.agregar(numToken, fila, columna, palabra, "Es un Número de porcentaje")
                        numToken+=1
                        palabra = ""
                        estado = 1
                        ver = "en"
                    
                    if ver == "":
                        self.agregar(numToken, fila, columna, palabra, "Es un Número")
                        numToken+=1
                        palabra = ""
                        estado = 1
                        columna -= 1

                if estado == 5:
                    estado = 1

                if estado == 6:
                    if letra[columna].isalpha() or letra[columna].isnumeric():
                        palabra += letra[columna]
                        estado = 13
                        columna += 1

                if estado == 7:
                    palabra += letra[columna]
                    if letra[columna] == '\"':
                        estado = 1
                        self.agregar(numToken, fila, columna, palabra, "Es un Simbolo")
                        numToken+=1
                        palabra = ""
                        columna -= 1

                if estado == 8:
                    if letra[columna] == '*':
                        estado = 15
                        

                if estado == 9:
                    if letra[columna].isalpha() or letra[columna].isnumeric() or letra[columna] == '_':
                        palabra += letra[columna]
                        
                    else:
                        if palabra in self.Reservada:
                            self.agregar(numToken, fila, columna, palabra, "Es una Palabra reservada")
                            numToken+=1
                            palabra = ""
                            estado = 1
                            columna -= 1
                        else:
                            self.agregar(numToken, fila, columna, palabra, "Es un ID")
                            numToken+=1
                            palabra = ""
                            estado = 1
                            columna -= 1

                if estado == 10:
                    if letra[columna].isalpha():
                        palabra += letra[columna]
                        estado = 1
                        self.agregar(numToken, fila, columna, palabra, "Es un Número")
                        numToken+=1
                        palabra = ""
                        estado = 1

                if estado == 11:
                    if letra[columna].isnumeric():
                        palabra += letra[columna]
                        estado = 16
                        columna += 1

                if estado == 12:
                    estado = 1
                if estado == 13:
                    if letra[columna].isalpha() or letra[columna].isnumeric():
                        palabra += letra[columna]
                    else:
                        self.agregar(numToken, fila, columna, palabra, "Es un Color")
                        numToken+=1
                        palabra = ""
                        estado = 1
                        columna -= 1

                if estado == 14:
                    estado = 1
                if estado == 15:
                    if letra[columna] == '/':
                        estado = 1
                if estado == 16:
                    ver = ""
                    if letra[columna].isalpha():
                        palabra += letra[columna]
                        estado = 10
                        ver = "en"

                    if letra[columna] == '%':
                        palabra += letra[columna]
                        ver = "en"
                        self.agregar(numToken, fila, columna, palabra, "Es un Número Porcentual")
                        numToken+=1
                        palabra = ""
                        estado = 1
                    if letra[columna].isnumeric():
                        ver = "en"
                        palabra += letra[columna]
                    if ver == "":
                        self.agregar(numToken, fila, columna, palabra, "Es un Número Real")
                        numToken+=1
                        palabra = ""
                        columna -= 1
                        estado = 1

                if estado == 17:
                    estado = 1
                if estado == 18:
                    estado = 1


                columna += 1

            fila += 1

    def agregar(self,num, fila , columna, lex, des):
        nuevo = Lexema(num, fila, columna, lex, des)
        self.Token.append(nuevo)

    def Regresar_Lista(self):
        return self.Token

