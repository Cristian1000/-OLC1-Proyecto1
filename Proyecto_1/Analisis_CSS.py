import string
from Lexema import *
from tkinter import messagebox 

class Analisis_CSS(object):
    """description of class"""
    Token = list()
    Reservada = ["color", "background-color", "background-image", "border", "Opacity", "background", "text-align", "font-family", "font-style", "font-weight", "font-size", "font", "padding-left", "padding-right", "padding-bottom", "padding-top", "padding", "display", "line-height", "width", "height", "margin-top", "margin-right", "margin-bottom", "margin-left", "margin", "border-style", "display", "position", "bottom", "top", "right", "left", "float", "clear", "max-width", "min-width", "max-height", "min-height"]
    reporte = "Reporte de CSS \n"

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
            lineas[fila] += "          "
            letra = list(lineas[fila])
            columna = 0
            while columna < len(letra):
                #messagebox.showinfo('Project 1', str(fila)+ ' ' + str(columna) + ' ' + palabra)
                if estado == 1:
                    ver = ""

                    if letra[columna] != ' ' and letra[columna] != '\n' and letra[columna] != '\t':
                        palabra += letra[columna]

                    if letra[columna] == '/':
                        self.reporte += "S1 -> S2 con  /  \n"
                        estado = 2
                        columna += 1
                        palabra = ""
                        ver = "en"

                    if letra[columna].isalpha() and ver == "":
                        self.reporte += "S1 -> S3 con " + letra[columna] + "  \n"
                        estado = 3
                        columna += 1
                        ver = "en"

                    if letra[columna].isnumeric() and ver == "":
                        self.reporte += "S1 -> S4 con " + letra[columna] + "  \n"
                        estado = 4
                        columna += 1
                        ver = "en"

                    if letra[columna] == '#' and ver == "":
                        self.reporte += "S1 -> S6 con " + letra[columna] + "  \n"
                        estado = 6
                        columna += 1
                        ver = "en"

                    if letra[columna] == '\"' and ver == "":
                        self.reporte += "S1 -> S7 con " + letra[columna] + "  \n"
                        estado = 7
                        columna += 1
                        ver = "en"


                    if estado <= 1 and letra[columna] != ' ' and letra[columna] != '\n' and letra[columna] != '\t':
                        self.reporte += "S1 -> S5 con " + letra[columna] + "  \n"
                        self.agregar(numToken, fila, columna, palabra, "Es un Simbolo")
                        numToken+=1
                        palabra = ""
                        estado = 1

                    print ('estado: '+ str(estado)+' '+str(columna)+' ' + palabra)
                    
                if estado == 2:
                    if letra[columna] == '*':
                        self.reporte += "S2 -> S8 con " + letra[columna] + "  \n"
                        estado = 8
                        primero = "no"
                        print ('estado: '+ str(estado)+' '+str(columna)+' ' + palabra)
                if estado == 3:
                    ver = ""
                    if letra[columna].isalpha():
                        palabra += letra[columna]
                        ver = "en"
                        self.reporte += "S3 -> S3 con " + letra[columna] + "  \n"

                    if letra[columna].isnumeric() or letra[columna] == '-' or letra[columna] == '_':
                        palabra += letra[columna]
                        self.reporte += "S3 -> S9 con " + letra[columna] + "  \n"
                        estado = 9
                        columna +=1
                        ver = "en"

                    if ver == "":
                        if palabra in self.Reservada:
                            self.reporte += "Estado de aceptacion con  "+ palabra + "  \n"
                            self.agregar(numToken, fila, columna, palabra, "Es una Palabra reservada")
                            numToken+=1
                            palabra = ""
                            estado = 1
                            if letra[columna] == '#':
                                self.agregar(numToken, fila, columna, letra[columna], "Es un Numeral")
                                numToken+=1
                                palabra = ""
                            else:
                                columna -= 1
                        else:
                            self.agregar(numToken, fila, columna, palabra, "Es un ID")
                            numToken+=1
                            palabra = ""
                            estado = 1
                            if letra[columna] == '#':
                                self.agregar(numToken, fila, columna, letra[columna], "Es un Numeral")
                                numToken+=1
                                palabra = ""
                            else:
                                columna -= 1

                if estado == 4:
                    ver = ""
                    if letra[columna].isnumeric(): 
                        self.reporte += "S4 -> S4 con " + letra[columna] + "  \n"
                        palabra += letra[columna]
                        ver = "en"
                    if letra[columna] == '.':
                        self.reporte += "S4 -> S11 con " + letra[columna] + "  \n"
                        palabra += letra[columna]
                        estado = 11
                        columna += 1
                        ver = "en"
                    if letra[columna].isalpha():
                        self.reporte += "S4 -> S10 con " + letra[columna] + "  \n"
                        palabra += letra[columna]
                        estado = 10
                        columna += 1
                        ver = "en"
                    if letra[columna] == '%':
                        self.reporte += "S4 -> S12 con " + letra[columna] + "  \n"
                        palabra += letra[columna]
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
                    print ('estado: '+ str(estado)+' '+str(columna)+' ' + palabra)
                if estado == 5:
                    estado = 1
                    print ('estado: '+ str(estado)+' '+str(columna)+' ' + palabra)
                if estado == 6:
                    if letra[columna].isalpha() or letra[columna].isnumeric():
                        palabra += letra[columna]
                        self.reporte += "S6 -> S13 con " + letra[columna] + "  \n"
                        estado = 13
                        columna += 1
                    print ('estado: '+ str(estado)+' '+str(columna)+' ' + palabra)
                if estado == 7:
                    palabra += letra[columna]
                    if letra[columna] == '\"':
                        estado = 1
                        self.reporte += "S7 -> S14 con " + letra[columna] + "  \n"
                        self.agregar(numToken, fila, columna, palabra, "Es una Cadena")
                        numToken+=1
                        palabra = ""
                    else:
                        self.reporte += "S7 -> S7 con " + letra[columna] + "  \n"
                    print ('estado: '+ str(estado)+' '+str(columna)+' ' + palabra)
                if estado == 8:
                    if letra[columna] == '*':
                        estado = 15
                        self.reporte += "S8 -> S15 " + letra[columna] + "  \n"
                    else:
                        self.reporte += "S8 -> S8 con " + letra[columna] + "  \n"
                    print ('estado: '+ str(estado)+' '+str(columna)+' ' + palabra)

                if estado == 9:
                    ver = ""
                    if letra[columna].isalpha() or letra[columna].isnumeric() or letra[columna] == '_':
                        palabra += letra[columna]
                        ver = "en"
                        self.reporte += "S9 -> S9 con " + letra[columna] + "  \n"

                    if ver == "":
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
                    print ('estado: '+ str(estado)+' '+str(columna)+' ' + palabra)
                if estado == 10:
                    if letra[columna].isalpha():
                        palabra += letra[columna]
                        estado = 1
                        self.reporte += "S10 -> S17 con " + letra[columna] + "  \n"
                        self.agregar(numToken, fila, columna, palabra, "Es un Número")
                        numToken+=1
                        palabra = ""
                    
                    print ('estado: '+ str(estado)+' '+str(columna)+' ' + palabra)
                if estado == 11:
                    if letra[columna].isnumeric():
                        palabra += letra[columna]
                        self.reporte += "S11 -> S16 con " + letra[columna] + "  \n"
                        estado = 16
                        columna += 1

                    print ('estado: '+ str(estado)+' '+str(columna)+' ' + palabra)

                if estado == 12:
                    estado = 1
                    print ('estado: '+ str(estado)+' '+str(columna)+' ' + palabra)
                if estado == 13:
                    ver = ""
                    if letra[columna].isalpha() or letra[columna].isnumeric():
                        palabra += letra[columna]
                        ver = "en"
                        self.reporte += "S13 -> S13 con " + letra[columna] + "  \n"

                    if ver == "" :
                        self.agregar(numToken, fila, columna, palabra, "Es un Color")
                        numToken+=1
                        palabra = ""
                        estado = 1
                        columna -= 1

                    print ('estado: '+ str(estado)+' '+str(columna)+' ' + palabra)

                if estado == 14:
                    estado = 1
                    print ('estado: '+ str(estado)+' '+str(columna)+' ' + palabra)
                if estado == 15:
                    if letra[columna] == '/':
                        self.reporte += "S15 -> S18 con " + letra[columna] + "  \n"
                        estado = 1
                    print ('estado: '+ str(estado)+' '+str(columna)+' ' + palabra)
                if estado == 16:
                    ver = ""
                    if letra[columna].isalpha():
                        palabra += letra[columna]
                        estado = 10
                        ver = "en"
                        self.reporte += "S16 -> S10 con " + letra[columna] + "  \n"

                    if letra[columna] == '%':
                        self.reporte += "S16 -> S12 con " + letra[columna] + "  \n"
                        palabra += letra[columna]
                        ver = "en"
                        self.agregar(numToken, fila, columna, palabra, "Es un Número Porcentual")
                        numToken+=1
                        palabra = ""
                        estado = 1
                    if letra[columna].isnumeric():
                        ver = "en"
                        palabra += letra[columna]
                        self.reporte += "S16 -> S16 con " + letra[columna] + "  \n"
                    if ver == "":
                        self.agregar(numToken, fila, columna, palabra, "Es un Número Real")
                        numToken+=1
                        palabra = ""
                        columna -= 1
                        estado = 1

                    print ('estado: '+ str(estado) +' '+str(columna)+' ' + palabra)

                if estado == 17:
                    estado = 1
                    print ('estado: '+ str(estado)+' '+str(columna)+' ' + palabra)
                if estado == 18:
                    estado = 1
                    print ('estado: '+ str(estado)+' '+str(columna)+' ' + palabra)


                columna += 1


            fila += 1

    def agregar(self,num, fila , columna, lex, des):
        nuevo = Lexema(num, fila, columna, lex, des)
        self.Token.append(nuevo)

    def Regresar_Lista(self):
        return self.Token

    def Reporte_CSS(self):
        return self.reporte
