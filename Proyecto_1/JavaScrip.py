import string
from Lexema import *
from tkinter import messagebox 

class JavaScrip(object):
    """description of class"""
    Token = list()
    Reservadas = ["await","break", "case", "catch", "class", "const", "continue", "debugger", "default", "delete", "do", "else", "export", "extends", "finally", "for", "function", "if", "import", "in", "instanceof", "new", "return", "super", "switch", "this", "throw", "try", "typeof", "var", "void", "while", "with", "yield", "let", "static", "null", "true", "false" ]

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
            letra = list(lineas[fila])
            columna = 0
            while columna < len(letra):
                print(letra[columna] + " " + str(estado))
                
                if estado == 1:
                    if letra[columna] != ' ' and letra[columna] != '\n' and letra[columna] != '\t':
                        palabra += letra[columna]

                    if letra[columna] == '/':
                        estado = 2
                        columna+=1

                    if letra[columna].isalpha():
                        estado = 3
                        columna+=1
                        #messagebox.showinfo('Project 1', str(estado) +"  " + palabra)

                    if letra[columna].isnumeric():
                        estado = 4
                        columna+=1
                        #messagebox.showinfo('Project 1', str(estado) +"  " + palabra)

                    if letra[columna] == '\"':
                        estado = 6
                        columna +=1
                        #messagebox.showinfo('Project 1', str(estado) +"  " + palabra)
                    
                    if estado <= 1:
                        self.agregar(numToken, fila, columna, palabra, "Es un Simbolo")
                        numToken+=1
                        palabra = ""
                        estado = 1
                    messagebox.showinfo('Project 1', str(columna) + " " + palabra)
                if estado == 2:
                    
                    if letra[columna] == '/':
                        estado = 7
                        palabra = ""
                        
                    elif letra[columna] == '*':
                        estado = 8
                        primero = "no"
                        palabra = ""

                    elif letra[columna] != '/' and letra[columna] != '*':
                        estado = estado
                        #self.agregar(numToken, fila, columna, palabra, "Es un Simbolo")
                        #numToken+=1
                        #estado = 1
                        #palabra = ""

                if estado == 3:
                    if letra[columna].isalpha() or letra[columna].isnumeric() or letra[columna] == "_":
                        palabra += letra[columna]
                        if letra[columna].isnumeric() or letra[columna] == "_":
                            estado = 9
                            columna += 1
                    else:
                        estado = 1
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
                    if letra[columna].isdigit():
                        estado = 4
                        palabra+=letra[columna]
                    elif letra[columna] == '.':
                        estado = 10
                        columna += 1
                        palabra += letra[columna]
                    else:
                        self.agregar(numToken, fila, columna, palabra, "Es un número")
                        numToken+=1
                        columna-=1
                        palabra=""
                        estado = 1

                if estado == 5:
                    palabra+= letra[columna]
                    self.agregar(numToken, fila, columna, palabra, "Es un simbolo")
                    numToken+=1
                    columna-=1
                    palabra=""
                    estado = 1

                if estado == 6:
                    palabra += letra[columna]
                    if (letra[columna] == "\"" ):
                        estado = 1
                        self.agregar(numToken, fila, columna, palabra, "Es una cadena")
                        numToken+=1
                        palabra=""
                        

                if estado == 7:
                    estado = 1
                    columna = len(letra)

                if estado == 8:
                    if letra[columna] == '*' and primero != "no":
                        estado = 13
                    if primero == "no":
                        primero = ""

                if estado == 9:
                    if letra[columna].isdigit() or letra[columna].isalpha() or letra[columna]=='_':
                        palabra+=letra[columna]
                    else:
                        self.agregar(numToken, fila, columna, palabra, "Es un ID")
                        numToken+=1
                        columna-=1
                        palabra=""
                        estado = 1

                if estado == 10:
                    if letra[columna].isdigit():
                        palabra+=letra[columna]
                        estado = 14
                        columna += 1
                    else:
                        estado = 1

                if estado == 11:
                    estado = 1

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

                if estado == 14:
                    if letra[columna].isdigit():
                        estado = 14
                    else:
                        estado = 1

                if estado == 15:
                    estado = 1
                
                columna+=1
                
            fila += 1
    def agregar(self,num, fila , columna, lex, des):
        nuevo = Lexema(num, fila, columna, lex, des)
        self.Token.append(nuevo)

    def Regresar_Lista(self):
        return self.Token

    def imprimir(self, lista):
        for a in lista:
            print(a)

        
