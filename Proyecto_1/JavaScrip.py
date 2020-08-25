import string

class JavaScrip(object):
    """description of class"""
    Token = list()

    def Analisis_S(self, entrada):
        estado = 1
        palabra = ""
        token = entrada.splitline()
        for linea in token:
            letras = list(linea)
            for letra in letras:
                if estado == 1:
                    if letra.isalpha:
                        palabra += letra
                        estado = 2

                    if letra.isdigit:
                        palabra += letra
                        estado = 3

                    if (not(letra.isalpha) and not(letra.isdigit)):
                        palabra += letra
                        estado = 4

                if esta == 2:
                    if letra.isalpha:
                        palabra += letra

                    else:
                        if (letra == " " or letra == '\n'):
                            lexema
                        else:
                            palabra += letra

                if esta == 3:
                    if letra.isdigit:
                        palabra += letra

                    elif letra == ".":
                        palabra += letra
                        estado = 6

                if esta == 4:

                if esta == 5:

                if esta == 6:

                if esta == 7:

                if esta == 8:

                if esta == 9:

                if esta == 10:

                if esta == 11:

                if esta == 12:

