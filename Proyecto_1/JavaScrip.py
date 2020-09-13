import string
from Lexema import *
from Errores import *
from tkinter import messagebox 
import os
import webbrowser

class JavaScrip(object):
    """description of class"""
    Token = list()
    errores = list() 
    Reservadas = ["await","break", "case", "catch", "class", "const", "continue", "debugger", "default", "delete", "do", "else", "export", "extends", "finally", "for", "function", "if", "import", "in", "instanceof", "new", "return", "super", "switch", "this", "throw", "try", "typeof", "var", "void", "while", "with", "yield", "let", "static", "null", "true", "false" ]
    simbolos = ["=", "+", "-", "|", "&"]
    grafo1 = ""
    grafo2 = ""
    grafo3 = ""
    buscar = 0
    error = ['$', '@', '#', '^', '?', '~', "°"]
    nuevo = ""

    def Analisis_L(self, entrada):
        self.Token.clear()
        self.Ruta(entrada)
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
            listo = ""
            while columna < len(letra) and listo == "":
                print(letra[columna] + " " + str(estado))
                
                if estado == 1:
                    if letra[columna] in self.error:
                        self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                        columna += 1

                    if letra[columna] == ';':
                        listo = "ya"

                    if letra[columna] != ' ' and letra[columna] != '\n' and letra[columna] != '\t':
                        palabra += letra[columna]
                    else:
                        self.agregar(numToken, fila, columna, letra[columna], "Es una palabra reservada")
                        numToken+=1

                    if letra[columna] == '/':
                        estado = 2
                        columna+=1

                    if letra[columna].isalpha():
                        self.grafo1 += "S1 -> S2 [label = \" "+letra[columna]+" \"]; \n"
                        estado = 3
                        columna+=1
                        #messagebox.showinfo('Project 1', str(estado) +"  " + palabra)

                    if letra[columna].isnumeric():
                        self.grafo2 += "S1 -> S2 [label = \" "+letra[columna]+" \"]; \n"
                        estado = 4
                        columna+=1
                        #messagebox.showinfo('Project 1', str(estado) +"  " + palabra)

                    if letra[columna] == '\"' or letra[columna] == '\'':
                        self.grafo3 += "S1 -> S2 [label = \" \\"+letra[columna]+" \"]; \n"
                        estado = 6
                        columna +=1
                        #messagebox.showinfo('Project 1', str(estado) +"  " + palabra)
                    
                    
                    if estado <= 1 and letra[columna] != ' ' and letra[columna] != '\n' and letra[columna] != '\t':
                        columna += 1
                        estado = 11
                    
                if estado == 2:
                    if letra[columna] in self.error:
                        self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                        columna += 1

                    if letra[columna] == '/':
                        estado = 7
                        palabra = ""
                        
                    elif letra[columna] == '*':
                        estado = 8
                        primero = "no"
                        palabra = ""

                    elif letra[columna] != '/' and letra[columna] != '*':
                        self.agregar(numToken, fila, columna, palabra, "Es un Simbolo")
                        numToken+=1
                        estado = 1
                        palabra = ""
                        columna -= 1

                if estado == 3:
                    if letra[columna] in self.error:
                        self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                        columna += 1
                    if letra[columna].isalpha():
                        self.grafo1 += "S2 -> S2 [label = \" "+letra[columna]+" \"]; \n"

                    if letra[columna].isalpha() or letra[columna].isnumeric() or letra[columna] == "_":
                        palabra += letra[columna]
                        if letra[columna].isnumeric() or letra[columna] == "_":
                            self.grafo1 += "S2 -> S3 [label = \" "+letra[columna]+" \"]; \n"
                            estado = 9
                            columna += 1
                    else:
                        estado = 1
                        self.grafo1 = ""
                        if palabra in self.Reservadas:
                            self.agregar(numToken, fila, columna, palabra, "Es una palabra reservada")
                            numToken+=1
                            columna-=1
                            palabra = ""
                        else:
                            self.agregar(numToken, fila, columna, palabra, "Es un ID")
                            numToken+=1
                            columna-=1
                            palabra = ""

                if estado == 4:
                    if letra[columna] in self.error:
                        self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                        columna += 1
                    if letra[columna].isdigit():
                        self.grafo2 += "S2 -> S2 [label = \" "+letra[columna]+" \"]; \n"
                        estado = 4
                        palabra+=letra[columna]
                    elif letra[columna] == '.':
                        palabra += letra[columna]
                        self.grafo2 += "S2 -> S3 [label = \" "+letra[columna]+" \"]; \n"
                        estado = 10
                        columna += 1
                    else:
                        self.grafo2 = ""
                        self.agregar(numToken, fila, columna, palabra, "Es un número")
                        numToken+=1
                        columna-=1
                        palabra=""
                        estado = 1

                if estado == 5:
                    if letra[columna] in self.error:
                        self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                        columna += 1
                    palabra+= letra[columna]
                    self.agregar(numToken, fila, columna, palabra, "Es un simbolo")
                    numToken+=1
                    columna-=1
                    palabra=""
                    estado = 1

                if estado == 6:
                    
                    if letra[columna] == "\"" or letra[columna] == '\'':
                        palabra += letra[columna]
                        self.grafo3 += "S2 -> S3 [label = \" \\"+letra[columna]+" \"]; \n"
                        self.Generar_Automata3(self.grafo3, "cadena.dot")
                        self.grafo3 = ""
                        estado = 1
                        self.agregar(numToken, fila, columna, palabra, "Es una cadena")
                        numToken+=1
                        palabra=""
                    else:
                        palabra += letra[columna]
                        self.grafo3 += "S2 -> S2 [label = \" "+letra[columna]+" \"]; \n"

                if estado == 7:
                    estado = 1
                    columna = len(letra)

                if estado == 8:
                    if letra[columna] == '*' and primero != "no":
                        estado = 13
                    if primero == "no":
                        primero = ""

                if estado == 9:
                    if letra[columna] in self.error:
                        self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                        columna += 1

                    if letra[columna].isdigit() or letra[columna].isalpha() or letra[columna]=='_':
                        palabra+=letra[columna]
                        self.grafo1 += "S3 -> S3 [label = \" "+letra[columna]+" \"]; \n"
                    else:
                        self.Generar_Automata1(self.grafo1, "ID.dot")
                        self.grafo1 = ""
                        self.agregar(numToken, fila, columna, palabra, "Es un ID")
                        numToken+=1
                        columna-=1
                        palabra=""
                        estado = 1

                if estado == 10:
                    if letra[columna] in self.error:
                        self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                        columna += 1
                    if letra[columna].isdigit():
                        self.grafo2 += "S3 -> S4 [label = \" "+letra[columna]+" \"]; \n"
                        palabra+=letra[columna]
                        estado = 14
                        columna += 1
                    else:
                        estado = 1

                if estado == 11:
                    if letra[columna] in self.error:
                        self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                        columna += 1

                    if letra[columna] in self.simbolos and listo == "":
                        palabra += letra[columna]
                        self.agregar(numToken, fila, columna, palabra, "Es un Simbolo")
                        numToken+=1
                        palabra = ""
                        estado = 1
                    else:
                        self.agregar(numToken, fila, columna, palabra, "Es un Simbolo")
                        numToken+=1
                        palabra = ""
                        columna -= 1
                        estado = 1

                    if palabra == ';':
                        columna = len(letra)
                if estado == 12:
                    self.agregar(numToken, fila, columna, palabra, "Es un cadena")
                    numToken+=1
                    columna-=1
                    palabra=""
                    estado = 1

                if estado == 13:
                    if letra[columna] == '/':
                        estado = 15
                        columna += 1
                    else:
                        estado = 8

                if estado == 14:
                    if letra[columna] in self.error:
                        self.Agregar_Error(fila, columna, letra[columna], "Simbolo no reconocido")
                        columna += 1
                    if letra[columna].isdigit():
                        self.grafo2 += "S4 -> S4 [label = \" "+letra[columna]+" \"]; \n"
                        estado = 14
                    else:
                        self.Generar_Automata2(self.grafo2, "numero.dot")
                        self.agregar(numToken, fila, columna, palabra, "Es un numero")
                        numToken+=1
                        columna-=1
                        palabra=""
                        estado = 1
                        self.grafo2 = ""

                if estado == 15:
                    estado = 1
                
                columna+=1
            self.agregar(numToken, fila, columna, '\n', "salto de linea")
            numToken+=1
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

    def imprimir(self, lista):
        for a in lista:
            print(a)

    def Generar_Automata1(self, texto, nombre):
        automata = "digraph g{ \n"
        automata += "rankdir=LR; \n"
        automata += "node[shape=doublecircle]; S2, S3; \n"
        automata += "node[shape=circle]; \n \n"
        automata += texto
        automata += "} \n"

        self.escribir2 = open(nombre, "w", encoding="utf-8")
        self.escribir2.write(automata)
        self.escribir2.close()

    def Generar_Automata2(self, texto, nombre):
        automata = "digraph g{ \n"
        automata += "rankdir=LR; \n"
        automata += "node[shape=doublecircle]; S2, S4; \n"
        automata += "node[shape=circle]; \n \n"
        automata += texto
        automata += "} \n"

        self.escribir2 = open(nombre, "w", encoding="utf-8")
        self.escribir2.write(automata)
        self.escribir2.close()
        
        
    def Generar_Automata3(self, texto, nombre):
         automata = "digraph g{ \n"
         automata += "rankdir=LR; \n"
         automata += "node[shape=doublecircle]; S3; \n"
         automata += "node[shape=circle]; \n \n"
         automata += texto
         automata += "} \n"

         self.escribir2 = open(nombre, "w", encoding="utf-8")
         self.escribir2.write(automata)
         self.escribir2.close()

    def Ruta(self, texto):
        estado = 1
        en = str(texto)
        lineas = en.split('\n')
        while self.buscar < len(lineas):
            primero = ""
            lineas[self.buscar] += "          "
            letra = list(lineas[self.buscar])
            columan = 0
            while columan < len(letra):
                if estado == 1:
                    if letra[columan].isalpha():
                        self.nuevo += letra[columan]

                    if letra[columan] == ':':
                        if self.nuevo == "PATHW":
                            estado = 2
                            columan += 1
                            self.nuevo = ""
                        else:
                            self.nuevo = ""
                            columan = len(letra)

                if estado == 2:
                    if letra[columan] != ' ':
                        self.nuevo += letra[columan]
                    else:
                        self.buscar = len(lineas)
                columan += 1
            self.buscar += 1

        print(self.nuevo)


    def Crear_archivo(self):
        nuevo_Archivo = ""
        tamaño = 0
        while tamaño < len(self.Token):
            nuevo_Archivo += self.Token[tamaño].get_Lexema()
            #if self.Token[tamaño].get_Lexema() == ';' or self.Token[tamaño].get_Lexema() == '{' or self.Token[tamaño].get_Lexema() == '}':
            #    nuevo_Archivo += '\n'
            #elif self.Token[tamaño].get_Lexema() != '.':
            #    if tamaño < len(self.Token) - 1:
            #        if self.Token[tamaño + 1].get_Lexema() != '.':
            #            nuevo_Archivo += ' '
            #    else:
            #        nuevo_Archivo += ' '

            tamaño += 1

        os.system('mkdir ' + self.nuevo)
        self.escribir2 = open(self.nuevo+'\\JavaScrip.js', "w", encoding="utf-8")
        self.escribir2.write(nuevo_Archivo)
        self.escribir2.close()

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

        crear = open("Errores de Java Scrip.html", "w", encoding="utf-8")
        crear.write(archivo_error)
        crear.close()
        webbrowser.open_new_tab('Errores de Java Scrip.html')
