class Errores(object):
    """description of class"""
    fila = 0
    culumna = 0
    lexema = ""
    descripcion = ""

    def __init__(self, fila, columna, lexema, descripcion):
        self.fila = fila
        self.columan = columna
        self.lexema = lexema
        self.descripcion = descripcion

    def set_Columna(self, columna):
        self.columan = columna

    def set_Lexema(self, lexema):
        self.lexema = lexema

    def set_Descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_Numero(self):
        return self.numero

    def get_Fila(self):
        return self.fila

    def get_Columna(self):
        return self.columan

    def get_Lexema(self):
        return self.lexema

    def get_Descripcion(self):
        return self.descripcion