import string
from Lexema import *
from tkinter import messagebox 
from Errores import *
import os
import webbrowser

class Analisis_CSS(object):
    """description of class"""
    Token = list()
    errores = list()
    Reservada = ["color", "background-color", "background-image", "border", "Opacity", "background", "text-align", "font-family", "font-style", "font-weight", "font-size", "font", "padding-left", "padding-right", "padding-bottom", "padding-top", "padding", "display", "line-height", "width", "height", "margin-top", "margin-right", "margin-bottom", "margin-left", "margin", "border-style", "display", "position", "bottom", "top", "right", "left", "float", "clear", "max-width", "min-width", "max-height", "min-height"]
    reporte = "Reporte de CSS \n"
    nuevo = ""
    separador = [";", "{", "}"]
    error = ["¬", "$", "<", ">", "?", "¿", "°"]
    terminacion = [":", ";", ",", "{", "(", " ", "#"]

    def Analisis(self, entrada):
        self.Token.clear()
        self.Ruta(entrada)
        print(self.nuevo)
        estado = 1
        numToken = 1
        palabra = ""
        en = str(entrada)
        lineas = en.split('\n')
        fila = 0
        while fila < len(lineas):
            primero = ""
            lineas[fila] += "  "
            letra = list(lineas[fila])
            columna = 0
            listo = ""
            while columna < len(letra) and listo == "":
                
                #if letra[columna] in self.error:
                #       self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                #        columna += 1
                #messagebox.showinfo('Project 1', str(fila)+ ' ' + str(columna) + ' ' + palabra)
                if estado == 1:
                    ver = ""
                    if letra[columna] in self.error:
                        self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                        columna += 1
                    if letra[columna] != ' ' and letra[columna] != '\n' and letra[columna] != '\t':
                        palabra += letra[columna]
                    else:
                        self.agregar(numToken ,fila, columna, letra[columna], "Espacio en blanco")
                        numToken += 1


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


                    if estado == 1 and letra[columna] != ' ' and letra[columna] != '\n' and letra[columna] != '\t':
                        self.reporte += "S1 -> S5 con " + letra[columna] + "  \n"
                        self.agregar(numToken, fila, columna, letra[columna], "Es un Simbolo")
                        numToken+=1
                        palabra = ""
                        estado = 1
                        if letra[columna] == ';':
                            lsito = "ya"

                    
                if estado == 2:
                    if letra[columna] == '*':
                        self.reporte += "S2 -> S8 con " + letra[columna] + "  \n"
                        estado = 8
                        primero = "no"
                    else:
                        estado = 1
                        columna -= 1

                if estado == 3:
                    if letra[columna] in self.error:
                        self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                        columna += 1
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
                        if letra[columna] in self.terminacion:
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
                        else:
                            self.Agregar_Error(fila, columan, letra[columan], "el simbolo no pertenece al patron")
                        
                                   
                if estado == 4:
                    if letra[columna] in self.error:
                        self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                        columna += 1
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
                if estado == 5:
                    estado = 1
                if estado == 6:
                    if letra[columna] in self.error:
                        self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                        columna += 1
                    if letra[columna].isalpha() or letra[columna].isnumeric():
                        palabra += letra[columna]
                        self.reporte += "S6 -> S13 con " + letra[columna] + "  \n"
                        estado = 13
                        columna += 1
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
                if estado == 8:
                    if letra[columna] == '*':
                        estado = 15
                        self.reporte += "S8 -> S15 " + letra[columna] + "  \n"
                    else:
                        self.reporte += "S8 -> S8 con " + letra[columna] + "  \n"

                if estado == 9:
                    if letra[columna] in self.error:
                        self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                        columna += 1
                    ver = ""
                    if letra[columna].isalpha() or letra[columna].isnumeric() or letra[columna] == '_':
                        palabra += letra[columna]
                        ver = "en"
                        self.reporte += "S9 -> S9 con " + letra[columna] + "  \n"

                    if ver == "":
                        if letra[columna] in self.terminacion:
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
                    if letra[columna] in self.error:
                        self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                        columna += 1
                    if letra[columna].isalpha():
                        palabra += letra[columna]
                        self.reporte += "S10 -> S17 con " + letra[columna] + "  \n"
                        estado =  17
                        columna += 1
                    else:
                        estado = 1
                        self.agregar(numToken, fila, columna, palabra, "Es un Número")
                        numToken+=1
                        palabra = ""
                        columna -= 1
                        
                if estado == 11:
                    if letra[columna] in self.error:
                        self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                        columna += 1
                    if letra[columna].isnumeric():
                        palabra += letra[columna]
                        self.reporte += "S11 -> S16 con " + letra[columna] + "  \n"
                        estado = 16
                        columna += 1


                if estado == 12:
                    estado = 1
                if estado == 13:
                    if letra[columna] in self.error:
                        self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                        columna += 1
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


                if estado == 14:
                    estado = 1
                if estado == 15:
                    if letra[columna] == '/':
                        self.reporte += "S15 -> S18 con " + letra[columna] + "  \n"
                        estado = 1
                if estado == 16:
                    if letra[columna] in self.error:
                        self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                        columna += 1
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


                if estado == 17:
                    if letra[columna].isalpha():
                        palabra += letra[columna]
                        self.reporte += "S17 -> S19 con " + letra[columna] + "  \n"
                        estado = 19
                        columna += 1
                    else:
                        estado = 1
                        self.agregar(numToken, fila, columna, palabra, "Es un Número")
                        numToken+=1
                        palabra = ""
                        columna -= 1
                if estado == 18:
                    estado = 1

                if estado == 19:
                    if letra[columna] in self.error:
                        self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                        columna += 1
                    if letra[columna].isalpha():
                        estado = 1
                        columna -= 4
                        palabra = ""
                    else:
                        estado = 1
                        self.agregar(numToken, fila, columna, palabra, "Es un Número")
                        numToken+=1
                        palabra = ""
                        columna -= 1


                columna += 1

            self.agregar(numToken, fila, columna, '\n', "salto de linea")
            numToken += 1
            fila += 1
        self.Crear_archivo()
        if len(self.errores) >= 0:
            self.Crear_Html()

    def agregar(self,num, fila , columna, lex, des):
        nuevo = Lexema(num, fila, columna, lex, des)
        self.Token.append(nuevo)

    def Agregar_Error(self, fila, columna, lex, des):
        nuevo = Errores(fila, columna, lex, des)
        self.errores.append(nuevo)

    def Regresar_Lista(self):
        return self.Token

    def Reporte_CSS(self):
        return self.reporte

    def Ruta(self, texto):
        buscar = 0
        estado = 1
        en = str(texto)
        lineas = en.split('\n')
        listo = ""
        while buscar < len(lineas) and listo == "":
            primero = ""
            lineas[buscar] += "  "
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
                    if letra[columan] != ' ' and letra[columan] != '*':
                        self.nuevo += letra[columan]
                    else:
                        print(self.nuevo)
                        listo = "ya"
                        break
                        buscar = len(lineas)
                columan += 1
            buscar += 1
            print(self.nuevo)

    def Crear_archivo(self):
        nuevo_Archivo = ""
        tamaño = 0
        while tamaño < len(self.Token):
            nuevo_Archivo += self.Token[tamaño].get_Lexema()
            #if self.Token[tamaño].get_Lexema() in self.separador:
            #    nuevo_Archivo += "\n"
            tamaño += 1

        os.system('mkdir ' + self.nuevo)
        self.escribir2 = open(self.nuevo+'\\NuevoCss.css', "w", encoding="utf-8")
        self.escribir2.write(nuevo_Archivo)
        self.escribir2.close()

    def imprimir_Error(self):
        for a in self.errores:
            print(a.get_Lexema() + ' \n')

    def Crear_Html(self):
        archivo_error = "<html> \n <head> \n <title>Errores de Java Scrip</title> \n <head> \n <body>"

        archivo_error += "<TABLE BORDER> \n"
        archivo_error += "  <TR> \n"
        archivo_error += "      <TH>Fila</TH> <TH>Columna</TH> <TH>Error</TH> \n"
        archivo_error += "  </TR> \n"
        for a in self.errores:
            archivo_error += "  <TR> \n"
            archivo_error += "      <TD>"+str(a.get_Fila())+"</TD> <TD>"+str(a.get_Columna())+"</TD> <TD>"+a.get_Lexema()+"</TD> \n"
            archivo_error += "  </TR> \n"

        archivo_error += "</TABLE> \n </body> \n </html>"

        crear = open("Errores de CSS.html", "w", encoding="utf-8")
        crear.write(archivo_error)
        crear.close()
        webbrowser.open_new_tab('Errores de Java Scrip.html')