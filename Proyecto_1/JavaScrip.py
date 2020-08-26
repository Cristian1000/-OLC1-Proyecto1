import string
from Lexema import *
from tkinter import messagebox 

class JavaScrip(object):
    """description of class"""
    Token = list()
    Reservadas = ["await","break", "case", "catch", "class", "const", "continue", "debugger", "default", "delete", "do", "else", "export", "extends", "finally", "for", "function", "if", "import", "in", "instanceof", "new", "return", "super", "switch", "this", "throw", "try", "typeof", "var", "void", "while", "with", "yield", "let", "static", "null", "true", "false" ]

    def Analisis_L(self, entrada):
        
        estado = 1
        numToken = 1
        palabra = ""
        en = str(entrada)
        lineas = en.split('\n')
        for fila in range(len(lineas)):
            #messagebox.showinfo('Project 1', str(len(lineas)))
            letra = list(lineas[fila])
            for columna in range(len(letra)-1):
                if estado == 1:
                    if letra[columna] == '/':
                        estado = 2
                    elif letra[columna].isalpha():
                        estado = 3
                        palabra += letra[columna]
                        #messagebox.showinfo('Project 1', 'es una letra')
                    elif letra[columna].isdigit():
                        estado = 4
                        palabra += letra[columna]
                        #messagebox.showinfo('Project 1', 'es un digito')
                    elif letra[columna] == '\"':
                        estado = 6
                    else:
                        self.agregar(numToken, fila, columna, letra[columna], "es un simbolo")
                        estado = 1
                        numToken+= 1
                if estado == 2:
                    if letra[columna] == '/':
                        estado = 7

                    if letra[columna] == '*':
                        estado = 8
                if estado == 3:
                    if letra[columna].isalpha():
                        estado = 3
                        palabra += letra[columna]
                    elif letra[columna].isdigit() or letra[columna] == '_':
                        estado = 9
                        palabra += letra[columna]
                    else:
                        if palabra in self.Reservadas:
                            self.agregar(numToken, fila, columna, palabra, "Es una palabra reservada")
                            numToken+=1
                            columna-=1
                            palabra = ""
                            estado = 1
                        else:
                            self.agregar(numToken, fila, columna, palabra, "Es un ID")
                            numToken+=1
                            columna-=1
                            palabra = ""
                            estado = 1
                if estado == 4:
                    if letra[columna].isdigit():
                        estado = 4
                        palabra+=letra[columna]
                    elif letra[columna] == '.':
                        estado = 10
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
                    if letra[columna] == '\"' :
                        estado = 1
                        self.agregar(numToken, fila, columna, palabra, "Es una cadena")
                        numToken+=1
                        columna-=1
                        palabra=""
                    else:
                        palabra += letra[columna]

                if estado == 7:
                    if columna < len(letra):
                        estado = 1
                if estado == 8:
                    if letra[columna] == '*':
                        estado = 13
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
                if estado == 14:
                    if letra[columna].isdigit():
                        estado = 14
                    else:
                        estado = 1
                if estado == 15:
                    estado = 1
        
            
    def agregar(self,num, fila , columna, lex, des):
        nuevo = Lexema(num, fila, columna, lex, des)
        self.Token.append(nuevo)

    def Regresar_Lista(self):
        return self.Token

    def imprimir(self, lista):
        for a in lista:
            print(a)
        
