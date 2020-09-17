from tkinter import *              
from tkinter import Menu           
from tkinter import filedialog     
from tkinter import scrolledtext  
from tkinter import messagebox   
from tkinter.ttk import *
import string
from JavaScrip import *
from Analisis_CSS import *
from Exprecion import *
from Analisis_HTML import *
import tkinter as tk
import os

class  Venta():
    ruta=""
    Lista_Token = list()
    reporteCss = ""
    def __init__(self):
        self.window = Tk()
        self.txtEntrada = Entry(self.window,width=10)
        self.txtConsola = Entry(self.window,width=10)
        self.window.title("Proyecto 1")
        self.window.geometry('1200x800')

        
        self.lbl = Label(self.window, text="Proyecto 1", font=("Time New Roman", 15))
        self.lbl.place(x=440, y = 10)

        self.menu = Menu(self.window)
        self.file_item = Menu(self.menu)  
        self.file_item.add_command(label='Nuevo Archivo', command=self.abrirFile)
        self.file_item.add_separator()
        self.file_item.add_command(label='Analizar', command=self.Analizar)
        self.file_item.add_separator()
        self.file_item.add_command(label='Guardar', command=self.guardar)
        self.file_item.add_separator()
        self.file_item.add_command(label='Guardar Como', command=self.guardarComo)
        self.file_item.add_separator()
        self.file_item.add_command(label='Salir', command=self.salir)

        self.report_item = Menu(self.menu)    
        self.report_item.add_separator()
        self.report_item.add_command(label='Errores HTML', command=self.Errores_HTML)
        self.report_item.add_separator()
        self.report_item.add_command(label='Errores CSS', command=self.Errores_CSS)    
        self.report_item.add_separator()
        self.report_item.add_command(label='Errores JAVA SCRIP', command=self.Errores_Java)
        self.report_item.add_separator()
        self.report_item.add_command(label='Reporte HTML')    
        self.report_item.add_separator()
        self.report_item.add_command(label='REporte CSS', command = self.Reporte_CSS)
        self.report_item.add_separator()
        self.report_item.add_command(label='Reporte JAVA SCRIP', command = self.Reporte_Java)

        self.menu.add_cascade(label='Archivo', menu=self.file_item)
        self.menu.add_cascade(label='Reportes', menu=self.report_item)
        self.window.config(menu=self.menu)
        
        
        self.txtEntrada = scrolledtext.ScrolledText(self.window,width=80,height=25)   
        self.txtEntrada.place(x=50, y = 50)
        

        self.combo = Combobox(self.window)
        self.combo['values']= ("HTML", "CSS", "Java Scrip", "rmt")
        self.combo.place(x=900, y= 50)
        self.combo.current(0)

        self.lbl = Label(self.window, text="Console:")  
        self.lbl.place(x=50, y = 550)
        self.txtConsola = scrolledtext.ScrolledText(self.window,width=80,height=10)  
        self.txtConsola.place(x=50, y = 600)
        
        self.window.mainloop()

    def Analyze(self):
        entrada = self.txtEntrada.get("1.0", END) 
        retorno = lexer(entrada)
        self.txtConsola.delete("1.0", END)
        self.txtConsola.insert("1.0", retorno)
        messagebox.showinfo('Project 1', 'Analysis Finished')

    
    def abrirFile(self):
        nameFile=filedialog.askopenfilename(title = "Seleccione archivo",filetypes = (("js files","*.js"), ("html files","*.html"),("css files","*.css"),("rmt files","*.rmt"),("All Files","*.*")))
        if nameFile!='':
            archi1=open(nameFile, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            contenido = self.Numero_Linea(contenido)
            self.txtEntrada.delete("1.0", END) 
            self.txtEntrada.insert("1.0", contenido)
    
    def guardar(self):
        if self.ruta=='':
            self.ruta=filedialog.asksaveasfilename(title = "Seleccione archivo",filetypes = (("HTML files","*.html"), ))
            self.escribir = open(self.ruta, "w", encoding="utf-8")
            self.escribir.write(self.txtEntrada.get("1.0", "end-1c"))
            self.escribir.close()
        else:
            self.escribir = open(self.ruta, "w", encoding="utf-8")
            self.escribir.write(self.txtEntrada.get("1.0", "end-1c"))
            self.escribir.close()
    def guardarComo(self):
        self.url=filedialog.asksaveasfilename(title = "Seleccione archivo",filetypes = (("HTML files","*.html"), ))
        self.escribir2 = open(self.url, "w", encoding="utf-8")
        self.escribir2.write(self.txtEntrada.get("1.0", "end-1c"))
        self.escribir2.close()

    def salir(self):
        self.window.destroy()

    def separar(self):
        #lineas = list()
        texto = str(self.txtEntrada.get("1.0", "end-1c"))
        lineas = texto.split('\n')
        letra = list(lineas[0])
        a= ""
        for el in letra:
            a+=el + '\n'
        self.txtConsola.delete("1.0", END) 
        self.txtConsola.insert("1.0", a)

    def Reporte_Java(self):
        os.system("dot -Tpng ID.dot -o ID.png")
        os.system("dot -Tpng cadena.dot -o cadena.png")
        os.system("dot -Tpng numero.dot -o numero.png")
        os.system("ID.png")
        os.system("cadena.png")
        os.system("numero.png")
        

    def Analizar(self):
        valor = self.combo.get()
        if valor == "HTML":
            HTML = Analisis_HTML()
            entrada_HTML = str(self.txtEntrada.get("1.0", "end-1c"))
            HTML.Analisis_L(entrada_HTML)
            self.Lista_Token = HTML.Regresar_Lista()
            messagebox.showinfo('Project 1', 'Se analizo el archivo HTML')

            en = ""
            for a in self.Lista_Token:
                en += a.get_Lexema() + "  "+ a.get_Descripcion() +'\n'

            self.txtConsola.delete("1.0", END) 
            self.txtConsola.insert("1.0", en)
        elif valor == 'CSS':
            CSS = Analisis_CSS()
            entrada_CSS = str(self.txtEntrada.get("1.0", "end-1c"))
            CSS.Analisis(entrada_CSS)
            self.Lista_Token = CSS.Regresar_Lista()
            self.reporteCss = CSS.Reporte_CSS()
            messagebox.showinfo('Project 1', 'Se analizo el Archivo CSS')

            #en = ""
            #for a in self.Lista_Token:
            #    en += a.get_Lexema() + "  "+ a.get_Descripcion() +'\n'
            
            

        elif valor == 'Java Scrip':
            self.Lista_Token = []
            Java = JavaScrip()
            entrad = str(self.txtEntrada.get("1.0", "end-1c"))
            
            Java.Analisis_L(entrad)
            self.Lista_Token = Java.Regresar_Lista()
            
            messagebox.showinfo('Project 1', 'Se analizo el Archivo Java Scrip')
            #en = ""
            #for a in self.Lista_Token:
            #    en += a.get_Lexema() + "  "+ a.get_Descripcion() +'\n'

            #self.txtConsola.delete("1.0", END) 
            #self.txtConsola.insert("1.0", en)

        elif valor == "rmt":
            exp = Exprecion()
            entrada = str(self.txtEntrada.get("1.0", "end-1c"))
            exp.Analisis_L(entrada)

            self.txtConsola.delete("1.0", END) 
            self.txtConsola.insert("1.0", exp.Resultado())

    def Errores_Java(self):
        webbrowser.open_new_tab('Errores de Java Scrip.html')

    def Errores_CSS(self):
        webbrowser.open_new_tab('Errores de CSS.html')

    def Errores_HTML(self):
        webbrowser.open_new_tab('Errores de HTML.html')

    def Reporte_CSS(self):
        self.txtConsola.delete("1.0", END) 
        self.txtConsola.insert("1.0", self.reporteCss)

    def Numero_Linea(self, texto):
        linea = texto.split('\n')
        contador = 0
        texto = ""
        while contador < len(linea):
            texto += str(contador) + " " + linea[contador] + "\n"
            contador += 1

        return texto


ventana = Venta()
