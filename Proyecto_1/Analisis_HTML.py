import string
from Lexema import *
from tkinter import messagebox 

class Analisis_HTML(object):
    """description of class"""
    Token = list()
    Reservadas = ["html", "head", "title", "body", "h1", "h2", "h3", "h4", "h5", "h6", "p", "br", "img", "a", "href", "ul", "ol", "li", "style", "src", "table", "th", "tr", "td", "caption", "colgroup", "col", "thead", "tbody", "tfoot", "link", "rel"]
    Simbolos = ["<", ">", "/", "="]

    def Analisis_L(self, entrada):
        self.Token.clear()
        estado = 1
        numToken = 1
        palabra = ""
        en = str(entrada)
        lineas = en.split('\n')
        fila = 0
        while fila < len(lineas):
            primero = ""
            lineas[fila] += "          "
            letra = list(lineas[fila].lower())
            columna = 0
            while columna < len(letra):
                if estado == 1:
                    ver = ""
                    if letra[columna] != ' ' and letra[columna] != '\t' and letra[columna] != '\n':
                        palabra += letra[columna]

                    if palabra in  self.Simbolos:
                        self.agregar(numToken, fila, columna, palabra, "Es un Simbolo")
                        numToken+=1
                        palabra = ""
                        estado = 1
                        ver = "en"

                    if letra[columna].isalpha() and ver == "":
                        estado = 2
                        columna += 1
                        ver = "en"

                    if letra[columna].isnumeric() and ver == "":
                        estado = 3
                        columna += 1
                        ver = "en"

                    if letra[columna] == '\"' and ver == "":
                        ver = "en"
                        estado = 5
                        columna += 1

                    if letra[columna] == '\'' and ver == "":
                        ver = "en"
                        estado = 7
                        columna += 1

                    if ver == "" and letra[columna] != ' ' and letra[columna] != '\t' and letra[columna] != '\n':
                        columna+=1
                        estado = 4

                if estado == 2:
                    ver = ""
                    if letra[columna].isalpha() or letra[columna].isnumeric():
                        palabra += letra[columna]
                        ver = "en"

                    if ver == "":
                        if palabra in self.Reservadas:
                            self.agregar(numToken, fila, columna, palabra, "Es una palabra reservada")
                            numToken+=1
                            palabra = ""
                            estado = 1
                            ver = "en"
                            columna -= 1

                        if letra[columna] == '<':
                            self.agregar(numToken, fila, columna, palabra, "Es una cadena")
                            numToken+=1
                            palabra = ""
                            estado = 1
                            ver = "en"
                            columna -= 1

                        if ver == "":
                            palabra += letra[columna]
                            estado = 4
                            columna += 1

                if estado == 3:
                    ver = ""
                    if letra[columna] != '<':
                        palabra += letra[columna]
                        ver = "en"

                    if ver == "":
                        self.agregar(numToken, fila, columna, palabra, "Es una cadena")
                        numToken+=1
                        palabra = ""
                        estado = 1
                        columna -= 1

                if estado == 4:
                    palabra += letra[columna]
                    estado = 3
                if estado == 5:
                    if letra[columna] != '\"':
                        palabra += letra[columna]

                    if letra[columna] == '\"':
                        palabra += letra[columna]
                        self.agregar(numToken, fila, columna, palabra, "Es una cadena")
                        numToken+=1
                        palabra = ""
                        estado = 1

                if estado == 6:
                    estado = 1
                if estado == 7:
                    if letra[columna] != '\'':
                        palabra += letra[columna]

                    if letra[columna] == '\'':
                        palabra += letra[columna]
                        self.agregar(numToken, fila, columna, palabra, "Es una cadena")
                        numToken+=1
                        palabra = ""
                        estado = 1
                print(palabra + ' ' + str(estado))
                columna += 1
            fila += 1

    def agregar(self,num, fila , columna, lex, des):
        nuevo = Lexema(num, fila, columna, lex, des)
        self.Token.append(nuevo)

    def Regresar_Lista(self):
        return self.Token
