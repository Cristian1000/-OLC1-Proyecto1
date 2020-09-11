import string
from Lexema import *
import os
from tkinter import messagebox 

class Analisis_HTML(object):
    """description of class"""
    Token = list()
    Reservadas = ["html", "head", "title", "body", "h1", "h2", "h3", "h4", "h5", "h6", "p", "br", "img", "a", "href", "ul", "ol", "li", "style", "src", "table", "th", "tr", "td", "caption", "colgroup", "col", "thead", "tbody", "tfoot", "link", "rel"]
    Simbolos = ["<", ">", "/", "="]
    nuevo = ""

    def Analisis_L(self, entrada):
        self.Token.clear()
        estado = 1
        numToken = 1
        palabra = ""
        self.Ruta(entrada)
        en = str(entrada)
        lineas = en.split('\n')
        fila = 2
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

                    if ver == "":
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
            self.agregar(numToken, fila, columna+1,'\n', "Salto de linea")
            fila += 1

    def agregar(self,num, fila , columna, lex, des):
        nuevo = Lexema(num, fila, columna, lex, des)
        self.Token.append(nuevo)

    def Regresar_Lista(self):
        return self.Token

    def Ruta(self, texto):
        buscar = 0
        estado = 1
        en = str(texto)
        lineas = en.split('\n')
        listo = ""
        while buscar < len(lineas) and listo == "":
            primero = ""
            lineas[buscar] += "          "
            letra = list(lineas[buscar])
            columan = 0
            while columan < len(letra) and listo == "":
                if estado == 1:
                    if letra[columan].isalpha():
                        self.nuevo += letra[columan]

                    if letra[columan] == ':':
                        if self.nuevo == "PATHW":
                            estado = 2
                            columan += 2
                            self.nuevo = ""
                        else:
                            self.nuevo = ""
                            columan = len(letra)

                if estado == 2:
                    if letra[columan] != '-':
                        self.nuevo += letra[columan]
                    else:
                        buscar = len(lineas)
                        listo = "ya"
                columan += 1
            buscar += 1
        print(self.nuevo)

    def Crear_archivo(self):
        nuevo_Archivo = ""
        for a in self.Token:
            nuevo_Archivo += a.get_Lexema()

        os.system('mkdir ' + self.nuevo)
        elf.escribir2 = open(self.nuevo+'\\Index.html', "w", encoding="utf-8")
        self.escribir2.write(automata)
        self.escribir2.close()