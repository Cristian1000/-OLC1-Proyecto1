import string

class JavaScrip(object):
    """description of class"""
    Token = list()

    def Analisis_S(self, entrada):
        estado = 1
        palabra = ""
        lineas = entrada.splitline()
        for fila in range(len(lineas)):
            letra = lsit(lineas[i])
            for columna in range(len(letra)-1):
                if estado == 1:
                    if letra[columna] == '/':
                        estado = 2

                    if letra[columna].isalpha():
                        estado = 3

                    if letra[columna].isdigit():
                        estado = 4

                    if letra[columna] == '\"':
                        estado = 6

                if estado == 2:
                    if letra[columna] == '/':
                        estado = 7

                    if letra[columna] == '*':
                        estado = 8
                if estado == 3:
                    if letra[columna].isalpha():
                        estado = 3

                    if letra[columna].isdigit() or letra[columna] == '_':
                        estado = 9

                if estado == 4:
                    if letra[columna].isdigit():
                        estado = 4

                    if letra[columna] == '.':
                        estado = 10

                if estado == 5:
                    estado = 11
                if estado == 6:
                    if letra[columna] == '\"' :
                        estado = 12

                if estado == 7:
                    if columna < len(letra):
                        estado = 1
                if estado == 8:
                    if letra[columna] == '*':
                        estado = 13
                if estado == 9:
                    if letra[columna].isdigit() and letra[columna].isalpha() and letra[columna]=='_':
                        estado = 9
                    else:
                        estado = 1
                if estado == 10:
                    if letra[columna].isdigit():
                        estado = 14
                    else:
                        estado = 1
                if estado == 11:
                    estado = 1
                if estado == 12:
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

