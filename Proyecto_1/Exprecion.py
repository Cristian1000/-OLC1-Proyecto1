import string
from Lexema import *
from Errores import *
from tkinter import messagebox 
import os
import webbrowser

class Exprecion(object):
    """description of class"""

    Token = list()
    errores = list()
    numero = 0
    ErrorSintactico = "Exprecion Correcta"

    def Analisis_L(self, entrada):
        self.Token.clear()
        self.errores.clear()
        estado = 1
        numToken = 1
        palabra = ""
        en = str(entrada)
        lineas = en.split('\n')
        fila = 0
        while fila < len(lineas):
            lineas[fila] += "     "
            letra = list(lineas[fila])
            columna = 0
            while columna < len(letra):
                if estado == 1:
                    ver = ""
                    if letra[columna] != ' ' and letra[columna] != '\n' and letra[columna] != '\t':
                        palabra += letra[columna]

                    if letra[columna].isalpha():
                        estado = 2
                        columna += 1
                        ver = "en"

                    if letra[columna].isnumeric() and ver == "":
                        estado = 3
                        columna += 1
                        ver = "en"

                    if ver == "" and letra[columna] != ' ' and letra[columna] != '\n' and letra[columna] != '\t':
                        if letra[columna] == '(':
                            self.agregar(3, fila, columna, letra[columna], "Es un paréntesis que abre")
                            palabra = ""
                            estado = 1

                        if letra[columna] == ')':
                            self.agregar(4, fila, columna, letra[columna], "Es un paréntesis que cierra")
                            palabra = ""
                            estado = 1

                        if letra[columna] == '+':
                            self.agregar(5, fila, columna, letra[columna], "Es un signo de suma")
                            palabra = ""
                            estado = 1

                        if letra[columna] == '-':
                            self.agregar(6, fila, columna, letra[columna], "Es un signo de resta")
                            palabra = ""
                            estado = 1

                        if letra[columna] == '*':
                            self.agregar(7, fila, columna, letra[columna], "Es un signo de Multiplicacion")
                            palabra = ""
                            estado = 1

                        if letra[columna] == '/':
                            self.agregar(8, fila, columna, letra[columna], "Es un signo de Divicion")
                            palabra = ""
                            estado = 1

                if estado == 2:
                    if letra[columna].isalpha() or letra[columna].isnumeric():
                        palabra += letra[columna]
                    else:
                        self.agregar(1, fila, columna, palabra, "Es un ID")
                        palabra = ""
                        estado = 1
                        columna -= 1

                if estado == 3:
                    ver = ""
                    if letra[columna].isnumeric():
                        palabra += letra[columna]
                        ver = "en"

                    if letra[columna] == '.' and ver == "":
                        palabra += letra[columna]
                        columna += 1
                        estado = 5
                        ver = "en"

                    if ver == "":
                        self.agregar(2, fila, columna, palabra, "Es un Numero")
                        palabra = ""
                        estado = 1
                        columna -= 1

                if estado == 4:
                    estado = 1
                if estado == 5:
                    if letra[columna].innumeric():
                        palabra += letra[columna]
                        estado = 6
                        columna += 1
                if estado == 6:
                    if letra[columna].isnumeric():
                        palabra += letra[columna]
                    else:
                        self.agregar(2, fila, columna, palabra, "Es un Número")
                        numToken+=1
                        palabra = ""
                        estado = 1
                        columna -= 1

                columna += 1
            fila += 1
        self.imprimir()
        self.preanalisis = self.Token[0].get_Numero()
        self.A()
        if len(self.errores) > 0:
            self.Crear_Html()

    def agregar(self,num, fila , columna, lex, des):
        nuevo = Lexema(num, fila, columna, lex, des)
        self.Token.append(nuevo)

    def imprimir(self):
        for a in self.Token:
            print(a.get_Lexema())  

    

    def parea(self, actual):
            if actual == self.preanalisis:
                self.numero += 1
                if self.numero < len(self.Token):
                    self.preanalisis = self.Token[self.numero].get_Numero()
            else:
                self.ErrorSintactico = "Exprecion incorrecta"
                if self.numero < len(self.Token):
                    self.Agregar_Error(self.Token[self.numero].get_Fila(), self.Token[self.numero].get_Columna(), self.Token[self.numero].get_Lexema(), "Error sintactico")
                else:
                    if actual == 1:
                        self.Agregar_Error(self.Token[self.numero-1].get_Fila(), self.Token[self.numero-1].get_Columna()+1, "ID", "Falta el ID")
                    if actual == 2:
                        self.Agregar_Error(self.Token[self.numero-1].get_Fila(), self.Token[self.numero-1].get_Columna()+1, "numero", "Falta un numero")
                    if actual == 4:
                        self.Agregar_Error(self.Token[self.numero-1].get_Fila(), self.Token[self.numero-1].get_Columna()+1, ")", "Falta el parentesis que cierra")
                
                if self.preanalisis == 5 or self.preanalisis == 6 or self.preanalisis == 7 or self.preanalisis == 8 or self.preanalisis == 4:
                    self.OP()
                if self.preanalisis == 1 or self.preanalisis == 2 or self.preanalisis == 3:
                    self.A()

    

    def A(self):
        if self.preanalisis == 3:
            self.parea(3)
            self.A()
            self.parea(4)
            self.OP()
        if self.preanalisis == 1:
            self.parea(1)
            self.OP()
        if self.preanalisis == 2:
            self.parea(2)
            self.OP()
        if self.preanalisis == 6:
            self.SIG()
            self.A()

    def OP(self):
        if self.preanalisis == 5:
            self.parea(5)
            self.A()
        if self.preanalisis == 6:
            self.parea(6)
            self.A()
        if self.preanalisis == 7:
            self.parea(7)
            self.A()
        if self.preanalisis == 8:
            self.parea(8)
            self.A()

    def SIG(self):
        if self.preanalisis == 6:
            self.parea(6)

    def Agregar_Error(self, fila, columna, lex, des):
        nuevo = Errores(fila, columna, lex, des)
        self.errores.append(nuevo)

    def Crear_Html(self):
        archivo_error = "<html> \n <head> \n <title>Errores de Java Scrip</title> \n <head> \n <body>"

        archivo_error += "<TABLE BORDER> \n"
        archivo_error += "  <TR> \n"
        archivo_error += "      <TH>Fila</TH> <TH>Columna</TH> <TH>Error</TH> <TH>Descripcion</TH> \n"
        archivo_error += "  </TR> \n"
        for a in self.errores:
            archivo_error += "  <TR> \n"
            archivo_error += "      <TD>"+str(a.get_Fila())+"</TD> <TD>"+str(a.get_Columna())+"</TD> <TD>"+a.get_Lexema()+"</TD> <TD>"+a.get_Descripcion() +"</TD> \n"
            archivo_error += "  </TR> \n"

        archivo_error += "</TABLE> \n </body> \n </html>"

        crear = open("Errores de Java Scrip.html", "w", encoding="utf-8")
        crear.write(archivo_error)
        crear.close()
        webbrowser.open_new_tab('Errores de Java Scrip.html')

    def Resultado(self):
        return self.ErrorSintactico

