from tkinter import *              
from tkinter import Menu           
from tkinter import filedialog     
from tkinter import scrolledtext  
from tkinter import messagebox   
from tkinter.ttk import *
import string

class  Venta():
    ruta=""
    def __init__(self):
        self.window = Tk()
        self.txtEntrada = Entry(self.window,width=10)
        self.txtConsola = Entry(self.window,width=10)
        self.window.title("Proyecto 1")
        self.window.geometry('1000x700')
        
        self.lbl = Label(self.window, text="Proyecto 1", font=("Time New Roman", 15))
        self.lbl.place(x=440, y = 10)

        self.menu = Menu(self.window)
        self.file_item = Menu(self.menu)  
        self.file_item.add_command(label='Nuevo Archivo', command=self.abrirFile)
        self.file_item.add_separator()
        self.file_item.add_command(label='Analizar', command=self.separar)
        self.file_item.add_separator()
        self.file_item.add_command(label='Guardar', command=self.guardar)
        self.file_item.add_separator()
        self.file_item.add_command(label='Guardar Como', command=self.guardarComo)
        self.file_item.add_separator()
        self.file_item.add_command(label='Salir', command=self.salir)

        self.report_item = Menu(self.menu)    
        self.report_item.add_separator()
        self.report_item.add_command(label='Errores HTML')
        self.report_item.add_separator()
        self.report_item.add_command(label='Errores CSS')    
        self.report_item.add_separator()
        self.report_item.add_command(label='Errores JAVA SCRIP')
        self.report_item.add_separator()
        self.report_item.add_command(label='Reporte HTML')    
        self.report_item.add_separator()
        self.report_item.add_command(label='REporte CSS')
        self.report_item.add_separator()
        self.report_item.add_command(label='Reporte JAVA SCRIP')

        self.menu.add_cascade(label='Archivo', menu=self.file_item)
        self.menu.add_cascade(label='Reportes', menu=self.report_item)
        self.window.config(menu=self.menu)
        
        # propiedades del textarea
        self.txtEntrada = scrolledtext.ScrolledText(self.window,width=80,height=25)   
        self.txtEntrada.place(x=50, y = 50)
        #ent = txtEntrada.get("1.0","10.10")
        #print("ent: ",ent)

        self.combo = Combobox(self.window)
        self.combo['values']= ("HTML", "CSS", "Java Scrip")
        self.combo.place(x=750, y= 50)
        self.combo.current(0)

        self.lbl = Label(self.window, text="Console:")  
        self.lbl.place(x=50, y = 465)
        self.txtConsola = scrolledtext.ScrolledText(self.window,width=80,height=10)  
        self.txtConsola.place(x=50, y = 490)
        
        self.window.mainloop()

    def Analyze(self):
        entrada = self.txtEntrada.get("1.0", END) #fila 1 col 0 hasta fila 2 col 10
        retorno = lexer(entrada)
        self.txtConsola.delete("1.0", END)
        self.txtConsola.insert("1.0", retorno)
        messagebox.showinfo('Project 1', 'Analysis Finished')

    
    def abrirFile(self):
        nameFile=filedialog.askopenfilename(title = "Seleccione archivo",filetypes = (("js files","*.js"), ("html files","*.html"),("css files","*.css"),("All Files","*.*")))
        if nameFile!='':
            archi1=open(nameFile, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
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
        lineas = texto.splitlines()
        letra = list(lineas[0])
        for el in letra:
            print(el)
            #self.txtConsola.delete("1.0", END) 
            #self.txtConsola.insert("1.0", el)


ventana = Venta()