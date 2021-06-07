import tkinter as tk
from tkinter import ttk
import os


class PanelCajaTexto(tk.Frame):
    def __init__(self,ventana_padre):
        super().__init__(ventana_padre)
        self.ventana_padre=ventana_padre
        
        ttk.Label(self,text="Nombre").grid(row=1,column=1)
        self.caja1=ttk.Entry(self)
        self.caja1.config(width=30)
        self.caja1.grid(row=1,column=2)

        self.boton1 = ttk.Button(self, text="Agregar",command=lambda: self.eventos("Agregar"))
        self.boton1.grid(row=1, column=3)
        
        ttk.Label(self,text="Todos los nombre").grid(row=2,column=1)
        self.caja2=tk.Text(self)
        self.caja2.config(width=30, height=10)
        self.caja2.config(font=("Consolas",12), selectbackground="red", padx=5, pady=5)
        self.caja2.grid(row=3,column=1, columnspan=3)
        ttk.Button(self, text="Limpiar",command=lambda: self.eventos("Limpiar")).grid(row=4, column=1)
    def eventos(self,comando:str):
        if comando=="Agregar":
            self.caja2.insert(tk.INSERT,str(self.caja1.get()+"\n"))
        if comando=="Limpiar":
            self.caja2.delete("1.0","end")

class PanelCombo(tk.Frame):
    def __init__(self,ventana_padre):
        super().__init__(ventana_padre)
        self.ventana_padre=ventana_padre
        ttk.Label(self,text="Lenguajes").grid(row=1,column=1)
        ttk.Label(self,text="Agregados").grid(row=2,column=1)

        self.combo = ttk.Combobox(self)
        self.combo["values"] = ["Python", "C", "C++", "Java"]
        self.combo.grid(row=1,column=2)

        self.boton1 = ttk.Button(self, text="Agregar Lenguaje",command=lambda: self.eventos("Agregar"))
        self.boton1.grid(row=1, column=3)
        
        self.caja2=tk.Text(self)
        self.caja2.config(width=30, height=10)
        self.caja2.config(font=("Consolas",12), selectbackground="red", padx=5, pady=5)
        self.caja2.grid(row=3,column=1,columnspan=3)
        
        ttk.Button(self, text="Limpiar",command=lambda: self.eventos("Limpiar")).grid(row=5, column=3)
    def eventos(self,comando:str):
        if comando=="Agregar":
            self.caja2.insert(tk.INSERT,str(self.combo.get()+"\n"))
        if comando=="Limpiar":
            self.caja2.delete("1.0","end")


class RadioBotones(tk.LabelFrame):
    def __init__(self,ventana_padre,titulo,lista_opciones):
        super().__init__(ventana_padre,text=titulo)
        self.ventana_padre=ventana_padre
        self.config(bd=2)
        self.opciones=lista_opciones
        n_op=len(lista_opciones)
        self.opcion=tk.IntVar()
        i=0
        while(i<n_op):
            tk.Radiobutton(self, text=lista_opciones[i], variable=self.opcion,value=i).grid(row=i+1,column=1,sticky='w')
            i=i+1
    def get_seleccion(self):
        return self.opcion.get()
        

class PanelRadioBotones(tk.Frame):
    def __init__(self,ventana_padre):
        super().__init__(ventana_padre)
        self.ventana_padre=ventana_padre
       
        self.radio_boton = RadioBotones(self,"Lenguajes",["Python", "C", "C++", "Java"])
        self.radio_boton.grid(row=1,column=1)

        self.boton1 = ttk.Button(self, text="Agregar Lenguaje",command=lambda: self.eventos("Agregar"))
        self.boton1.grid(row=2, column=1)       

        self.caja2=tk.Text(self)
        self.caja2.config(width=30, height=10)
        self.caja2.config(font=("Consolas",12), selectbackground="red", padx=5, pady=5)
        self.caja2.grid(row=1,column=2,rowspan=2)
        
        ttk.Button(self, text="Limpiar",command=lambda: self.eventos("Limpiar")).grid(row=3, column=2)
    def eventos(self,comando:str):
        if comando=="Agregar":
            texto=self.radio_boton.opciones[self.radio_boton.get_seleccion()]
            self.caja2.insert(tk.INSERT,str(texto+"\n"))
        if comando=="Limpiar":
            self.caja2.delete("1.0","end")      

class CajasChequeo(tk.LabelFrame):
    def __init__(self,ventana_padre,titulo,lista_opciones):
        super().__init__(ventana_padre,text=titulo)
        self.ventana_padre=ventana_padre
        self.config(bd=2)
        self.opciones=lista_opciones
        self.n_op=len(lista_opciones)
        self.opcion=tk.IntVar()
        self.cajas=[]
        self.valor=[]
        i=0
        while(i<self.n_op):
            self.valor.append(tk.IntVar())
            self.cajas.append(tk.Checkbutton(self, text=lista_opciones[i], onvalue=1,offvalue=0,variable=self.valor[i]).pack(anchor="w"))
            i=i+1
    def get_seleccion(self)->list:
        rta=[]
        i=0
        while(i<self.n_op):
            if (self.valor[i].get()==1):
                rta.append(self.opciones[i])
            i=i+1
        return rta

class PanelCajasChequeo(tk.Frame):
    def __init__(self,ventana_padre):
        super().__init__(ventana_padre)
        self.ventana_padre=ventana_padre
       
        self.chequeo = CajasChequeo(self,"Lenguajes",["Python", "C", "C++", "Java"])
        self.chequeo.grid(row=1,column=1)

        self.boton1 = ttk.Button(self, text="Agregar Lenguaje",command=lambda: self.eventos("Agregar"))
        self.boton1.grid(row=2, column=1)
        
        self.caja2=tk.Text(self)
        self.caja2.config(width=30, height=10)
        self.caja2.config(font=("Consolas",12), selectbackground="red", padx=5, pady=5)
        self.caja2.grid(row=1,column=2, rowspan=2)

        ttk.Button(self, text="Limpiar",command=lambda: self.eventos("Limpiar")).grid(row=3, column=2)
    def eventos(self,comando:str):
        if comando=="Agregar":
            texto=self.chequeo.get_seleccion()
            self.caja2.insert(tk.INSERT,str(texto)+"\n")
        if comando=="Limpiar":
            self.caja2.delete("1.0","end") 

class PanelImagen(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.ventana_padre=master
        file_path = os.path.dirname(os.path.abspath(__file__))
        imagen_path = os.path.join(file_path, 'data', "softwarelibre.png")
        self.imagen_cabecera=tk.PhotoImage(file=imagen_path) 
        self.etiqueta=ttk.Label(self,image=self.imagen_cabecera)
        self.etiqueta.pack(fill="both")
        
   

class BarraHerramientas(tk.LabelFrame):
    def __init__(self,ventana_padre,lista_iconos,lista_comandos):
        super().__init__(ventana_padre)
        self.ventana_padre=ventana_padre
        self.config(bd=2)
        self.lista_comandos=lista_comandos
        self.iconos=[]
        file_path = os.path.dirname(os.path.abspath(__file__))
        num_iconos=len(lista_iconos)
        i=0
        x=tk.IntVar()
        while(i<num_iconos):
            imagen_path = os.path.join(file_path, 'iconos', lista_iconos[i])
            self.iconos.append(tk.PhotoImage(file=imagen_path))
            cadena=self.lista_comandos[i]
            boton = tk.Button(self,image=self.iconos[i], relief="raised", borderwidth=3)
            boton.config(command=lambda w=cadena: self.eventos(w))
            boton.pack(side=tk.LEFT, padx=2, pady=2)
            i=i+1
    def eventos(self,comando:str):
        self.ventana_padre.eventos(comando)
    
class PanelBarraHerramientas(tk.Frame):
    def __init__(self,ventana_padre):
        super().__init__(ventana_padre)
        self.ventana_padre=ventana_padre
        self.barra_herramientas = BarraHerramientas(self,["carpeta.png","lupa.png","play.png","video.png"],["abrir","zoom","play","video"])
        self.barra_herramientas.pack(side=tk.TOP, padx=2, pady=2)

        self.caja2=tk.Text(self)
        self.caja2.config(width=30, height=10)
        self.caja2.config(font=("Consolas",12), selectbackground="red", padx=5, pady=5)
        self.caja2.pack(side=tk.TOP, padx=2, pady=2)

        ttk.Button(self, text="Limpiar",command=lambda: self.eventos("Limpiar")).pack(side=tk.TOP, padx=2, pady=2)
    def eventos(self,comando:str):
        if (comando=="Limpiar"):
            self.caja2.delete("1.0","end") 
        else:
            self.caja2.insert(tk.INSERT,str(comando)+"\n")

class PanelMenu(tk.Frame):
    def __init__(self,ventana_padre):
        super().__init__(ventana_padre)
        self.ventana_padre=ventana_padre
        menubar = tk.Menu(self)
        self.ventana_padre.config(menu=menubar)
        filemenu = tk.Menu(menubar)
        editmenu = tk.Menu(menubar)
        helpmenu = tk.Menu(menubar)
        
        filemenu = tk.Menu(menubar,tearoff=0)
        filemenu.add_command(label="Nuevo",command=lambda: self.eventos("Nuevo"))
        filemenu.add_command(label="Abrir")
        filemenu.add_command(label="Guardar")
        filemenu.add_command(label="Cerrar")
        filemenu.add_separator()
        filemenu.add_command(label="Salir")
        
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cortar")
        editmenu.add_command(label="Copiar")
        editmenu.add_command(label="Pegar")
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Ayuda")
        helpmenu.add_separator()
        helpmenu.add_command(label="Acerca de...")
        menubar.add_cascade(label="Archivo", menu=filemenu)
        menubar.add_cascade(label="Editar", menu=editmenu)
        menubar.add_cascade(label="Ayuda", menu=helpmenu)
        
    def eventos(self,comando:str):
        print(comando)
        
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog
class PanelDialogos(tk.Frame):
    def __init__(self,ventana_padre):
        super().__init__(ventana_padre)
        self.ventana_padre=ventana_padre

        ttk.Label(self,text="Dialogos").grid(row=1,column=1)
        ttk.Label(self,text="Salida").grid(row=1,column=2)
  
        self.caja2=tk.Text(self)
        self.caja2.config(width=40, height=10)
        self.caja2.config(font=("Consolas",12), selectbackground="red", padx=5, pady=5)
        self.caja2.grid(row=2,column=2,rowspan=9)

        self.btn_mensaje = ttk.Button(self, text="Mensaje",command=lambda: self.eventos("Mensaje"))
        self.btn_mensaje.grid(row=2, column=1)

        self.btn_error = ttk.Button(self, text="Error",command=lambda: self.eventos("Error"))
        self.btn_error.grid(row=3, column=1)

        self.btn_advertencia = ttk.Button(self, text="Advertencia",command=lambda: self.eventos("Advertencia"))
        self.btn_advertencia.grid(row=4, column=1)

        self.btn_pregunta = ttk.Button(self, text="Pregunta",command=lambda: self.eventos("Pregunta"))
        self.btn_pregunta.grid(row=5, column=1)

        self.btn_cancelar = ttk.Button(self, text="Ok Cancelar",command=lambda: self.eventos("Cancelar"))
        self.btn_cancelar.grid(row=6, column=1)

        self.btn_reintentar = ttk.Button(self, text="Reintentar",command=lambda: self.eventos("Reintentar"))
        self.btn_reintentar.grid(row=7, column=1)

        self.btn_color = ttk.Button(self, text="Color",command=lambda: self.eventos("Color"))
        self.btn_color.grid(row=8, column=1)

        self.btn_archivos = ttk.Button(self, text="Abrir Archivos",command=lambda: self.eventos("Archivos"))
        self.btn_archivos.grid(row=9, column=1)

        self.btn_guardar = ttk.Button(self, text="Guardar como",command=lambda: self.eventos("Guardar"))
        self.btn_guardar.grid(row=10, column=1)

        ttk.Button(self, text="Limpiar",command=lambda: self.eventos("Limpiar")).grid(row=11, column=2)
    def eventos(self,comando:str):
        if comando=="Mensaje":
            MessageBox.showinfo("Titulo ventana", "Mensaje a mostrar") 
            self.caja2.insert(tk.INSERT,"Solo muestra mensaje\n")
        if comando=="Error":
            MessageBox.showerror("Error", "Mensaje Error") 
            self.caja2.insert(tk.INSERT,"Muestra mensaje de error\n")
        if comando=="Advertencia":
            MessageBox.showwarning("Advertencia", "Mensaje de advertencia Warning") 
            self.caja2.insert(tk.INSERT,"Muestra mensaje adverntecia\n")
        if comando=="Limpiar":
            self.caja2.delete("1.0","end")
        if comando=="Pregunta":
            resultado = MessageBox.askquestion("Salir","¿Está seguro que desea salir sin guardar?")
            self.caja2.insert(tk.INSERT,resultado+"\n")
        if comando=="Cancelar":
            resultado = MessageBox.askokcancel("Sobrescribir","¿Está seguro de sobreescribir el archivo?")
            self.caja2.insert(tk.INSERT,str(resultado)+"\n")
        if comando=="Reintentar":
            resultado = MessageBox.askretrycancel("Reintentar","No se puede conectar")
            self.caja2.insert(tk.INSERT,str(resultado)+"\n")
        if comando=="Color":
            resultado = ColorChooser.askcolor(title="Elige un color")
            self.caja2.insert(tk.INSERT,str(resultado)+"\n")
        if comando=="Archivos":
            resultado =  FileDialog.askopenfilename(title="Abrir un fichero")
            self.caja2.insert(tk.INSERT,str(resultado)+"\n")
        if comando=="Guardar":
            resultado =  FileDialog.asksaveasfile(title="Guardar un archivo")
            self.caja2.insert(tk.INSERT,str(resultado)+"\n")

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
class VentanaGraficasLineales(tk.Toplevel):
    def __init__(self,ventana_padre):
        super().__init__(ventana_padre)
        self.panel_controles=tk.LabelFrame(self,text="Funciones Lineales",bd=2)
        self.m = tk.DoubleVar(value=1.0)
        self.b = tk.DoubleVar(value=-2.0)
        self.x1 = tk.DoubleVar(value=-6.0)
        self.x2 = tk.DoubleVar(value=6.0)
        self.color=(0.0, 128.5/256, 0.0)
        self.color_hexa='#008000'
        # Creamos el canvas, que podemos decir que es el lugar en donde
        # se mostrara el gráfico
        ttk.Label(self.panel_controles,text=" f(x)=mx +b").grid(sticky="e",row=1,column=1)
        ttk.Label(self.panel_controles,text="Pendiente m=").grid(sticky="e",row=2,column=1)
        ttk.Label(self.panel_controles,text="Y intecepto b=").grid(sticky="e",row=3,column=1)
        ttk.Entry(self.panel_controles,width=10,textvariable=self.m).grid(row=2,column=2)
        ttk.Entry(self.panel_controles,width=10,textvariable=self.b).grid(row=3,column=2)

        ttk.Label(self.panel_controles,text="Intervalo de graficación").grid(sticky="e",row=4,column=1)
        ttk.Label(self.panel_controles,text="Límite Inferior x1=").grid(sticky="e",row=5,column=1)
        ttk.Label(self.panel_controles,text="Límite Superior x2=").grid(sticky="e",row=6,column=1)
        
        self.etiqueta_color=tk.Label(self.panel_controles,text="Color")
        self.etiqueta_color.config(bg=self.color_hexa)
        self.etiqueta_color.grid(sticky="e",row=7,column=1)
        
        self.btn_color = ttk.Button(self.panel_controles, text="Seleccionar",command=lambda: self.eventos("Color"))
        self.btn_color.grid(row=7, column=2)
        
        ttk.Entry(self.panel_controles,width=10,textvariable=self.x1).grid(row=5,column=2)
        ttk.Entry(self.panel_controles,width=10,textvariable=self.x2).grid(row=6,column=2)
        self.btn_graficar = ttk.Button(self.panel_controles, text="Graficar",command=lambda: self.eventos("Graficar"))
        self.btn_graficar.grid(row=10, column=1)
        self.btn_graficar = ttk.Button(self.panel_controles, text="Nueva Grafica",command=lambda: self.eventos("Nueva Grafica"))
        self.btn_graficar.grid(row=10, column=2)
        
        self.panel_controles.pack()
        self.figura=plt.figure(1,figsize=(6, 6), dpi=80)
        self.figura=self.graficar(self.x1.get(),self.x2.get(),self.m.get(),self.b.get(),self.figura.number)
        self.canvas = FigureCanvasTkAgg(self.figura, master=self)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()
        self.toolbar =  NavigationToolbar2Tk(self.canvas, self )
        self.toolbar.pack()
        self.toolbar.update()
        
    def f(self,x,m,b):
        y=(m*x)+b
        return(y)
    def graficar(self,x1,x2,m,b,numfig):
        fig=plt.figure(numfig,figsize=(6, 6), dpi=80)
        plano=fig.gca()
        x=np.linspace(x1,x2,100)
        y=self.f(x,m,b)
        plano.plot(x,y,color=self.color)
        return(fig)
    def eventos(self, comando:str):
        if (comando=="Graficar"):
            self.figura=self.graficar(self.x1.get(),self.x2.get(),self.m.get(),self.b.get(),self.figura.number)
            self.canvas.draw()
        if (comando=="Nueva Grafica"):
            self.figura.clear()
            self.figura=self.graficar(self.x1.get(),self.x2.get(),self.m.get(),self.b.get(),self.figura.number)
            self.canvas.draw()
        if (comando=="Color"):
            ((r,g,b),h) = ColorChooser.askcolor(master=self,title="Elige un color")
            self.lift()
            self.color_hexa=h
            self.color=(r/256,g/256,b/256)
            self.etiqueta_color.config(bg=self.color_hexa)

class VentanaGraficasExponenciales(tk.Toplevel):
    def __init__(self,ventana_padre):
        super().__init__(ventana_padre)
        self.panel_controles=tk.LabelFrame(self,text="Funciones Lineales",bd=2)
        self.a = tk.DoubleVar(value=1.0)
        self.b = tk.DoubleVar(value=-2.0)
        self.x1 = tk.DoubleVar(value=-6.0)
        self.x2 = tk.DoubleVar(value=6.0)
        self.color=(0.0, 128.5/256, 0.0)
        self.color_hexa='#008000'
        # Creamos el canvas, que podemos decir que es el lugar en donde
        # se mostrara el gráfico
        ttk.Label(self.panel_controles,text=" f(x)= a*exp(b*x)").grid(sticky="e",row=1,column=1)
        ttk.Label(self.panel_controles,text="Factor a=").grid(sticky="e",row=2,column=1)
        ttk.Label(self.panel_controles,text="Factor b=").grid(sticky="e",row=3,column=1)
        ttk.Entry(self.panel_controles,width=10,textvariable=self.a).grid(row=2,column=2)
        ttk.Entry(self.panel_controles,width=10,textvariable=self.b).grid(row=3,column=2)

        ttk.Label(self.panel_controles,text="Intervalo de graficación").grid(sticky="e",row=4,column=1)
        ttk.Label(self.panel_controles,text="Límite Inferior x1=").grid(sticky="e",row=5,column=1)
        ttk.Label(self.panel_controles,text="Límite Superior x2=").grid(sticky="e",row=6,column=1)
        
        self.etiqueta_color=tk.Label(self.panel_controles,text="Color")
        self.etiqueta_color.config(bg=self.color_hexa)
        self.etiqueta_color.grid(sticky="e",row=7,column=1)
        
        self.btn_color = ttk.Button(self.panel_controles, text="Seleccionar",command=lambda: self.eventos("Color"))
        self.btn_color.grid(row=7, column=2)
        
        ttk.Entry(self.panel_controles,width=10,textvariable=self.x1).grid(row=5,column=2)
        ttk.Entry(self.panel_controles,width=10,textvariable=self.x2).grid(row=6,column=2)
        self.btn_graficar = ttk.Button(self.panel_controles, text="Graficar",command=lambda: self.eventos("Graficar"))
        self.btn_graficar.grid(row=10, column=1)
        self.btn_graficar = ttk.Button(self.panel_controles, text="Nueva Grafica",command=lambda: self.eventos("Nueva Grafica"))
        self.btn_graficar.grid(row=10, column=2)
        
        self.panel_controles.pack()
        self.figura=plt.figure(1,figsize=(6, 6), dpi=80)
        self.figura=self.graficar(self.x1.get(),self.x2.get(),self.a.get(),self.b.get(),self.figura.number)
        self.canvas = FigureCanvasTkAgg(self.figura, master=self)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()
        self.toolbar =  NavigationToolbar2Tk(self.canvas, self )
        self.toolbar.pack()
        self.toolbar.update()
        
    def f(self,x,a,b):
        y=a*np.exp(b*x)
        return(y)
    def graficar(self,x1,x2,a,b,numfig):
        fig=plt.figure(numfig,figsize=(6, 6), dpi=80)
        plano=fig.gca()
        x=np.linspace(x1,x2,100)
        y=self.f(x,a,b)
        plano.plot(x,y,color=self.color)
        return(fig)
    def eventos(self, comando:str):
        if (comando=="Graficar"):
            self.figura=self.graficar(self.x1.get(),self.x2.get(),self.a.get(),self.b.get(),self.figura.number)
            self.canvas.draw()
        if (comando=="Nueva Grafica"):
            self.figura.clear()
            self.figura=self.graficar(self.x1.get(),self.x2.get(),self.a.get(),self.b.get(),self.figura.number)
            self.canvas.draw()
        if (comando=="Color"):
            ((r,g,b),h) = ColorChooser.askcolor(master=self,title="Elige un color")
            self.lift()
            self.color_hexa=h
            self.color=(r/256,g/256,b/256)
            self.etiqueta_color.config(bg=self.color_hexa)

class VentanaGraficasSenosoidales(tk.Toplevel):
    def __init__(self,ventana_padre):
        super().__init__(ventana_padre)
        self.panel_controles=tk.LabelFrame(self,text="Funciones Lineales",bd=2)
        #f(x)= a*exp(-c*x).(cos(w*x+b))
        self.a = tk.DoubleVar(value=10)
        self.c = tk.DoubleVar(value=1)
        self.w = tk.DoubleVar(value=10)
        self.b = tk.DoubleVar(value=0.1)
        self.x1 = tk.DoubleVar(value=-6.0)
        self.x2 = tk.DoubleVar(value=6.0)
        self.color=(0.0, 128.5/256, 0.0)
        self.color_hexa='#008000'
        # Creamos el canvas, que podemos decir que es el lugar en donde
        # se mostrara el gráfico
        ttk.Label(self.panel_controles,text=" f(x)= a*exp(-c*x).(cos(w*x+b))").grid(sticky="e",row=1,column=1)
        ttk.Label(self.panel_controles,text="Factores a=").grid(sticky="e",row=2,column=1)
        ttk.Label(self.panel_controles,text="c=").grid(sticky="e",row=3,column=1)
        ttk.Label(self.panel_controles,text="w=").grid(sticky="e",row=4,column=1)
        ttk.Label(self.panel_controles,text="b=").grid(sticky="e",row=5,column=1)
        ttk.Entry(self.panel_controles,width=10,textvariable=self.a).grid(row=2,column=2)
        ttk.Entry(self.panel_controles,width=10,textvariable=self.c).grid(row=3,column=2)
        ttk.Entry(self.panel_controles,width=10,textvariable=self.w).grid(row=4,column=2)
        ttk.Entry(self.panel_controles,width=10,textvariable=self.b).grid(row=5,column=2)


        ttk.Label(self.panel_controles,text="Intervalo de graficación").grid(sticky="e",row=6,column=1)
        ttk.Label(self.panel_controles,text="Límite Inferior x1=").grid(sticky="e",row=7,column=1)
        ttk.Label(self.panel_controles,text="Límite Superior x2=").grid(sticky="e",row=8,column=1)
        ttk.Entry(self.panel_controles,width=10,textvariable=self.x1).grid(row=7,column=2)
        ttk.Entry(self.panel_controles,width=10,textvariable=self.x2).grid(row=8,column=2)
       
        
        self.etiqueta_color=tk.Label(self.panel_controles,text="Color")
        self.etiqueta_color.config(bg=self.color_hexa)
        self.etiqueta_color.grid(sticky="e",row=9,column=1)
        
        self.btn_color = ttk.Button(self.panel_controles, text="Seleccionar",command=lambda: self.eventos("Color"))
        self.btn_color.grid(row=9, column=2)
        
        
        self.btn_graficar = ttk.Button(self.panel_controles, text="Graficar",command=lambda: self.eventos("Graficar"))
        self.btn_graficar.grid(row=10, column=1)
        self.btn_graficar = ttk.Button(self.panel_controles, text="Nueva Grafica",command=lambda: self.eventos("Nueva Grafica"))
        self.btn_graficar.grid(row=10, column=2)
        
        self.panel_controles.pack()
        self.figura=plt.figure(1,figsize=(6, 6), dpi=80)
        self.figura=self.graficar(self.x1.get(),self.x2.get(),self.figura.number)
        self.canvas = FigureCanvasTkAgg(self.figura, master=self)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()
        self.toolbar =  NavigationToolbar2Tk(self.canvas, self )
        self.toolbar.pack()
        self.toolbar.update()
    def fsenosoidal(self,x):
        #f(x)= a*exp(-c*x).(cos(w*x+b))
        a=self.a.get()
        b=self.b.get()
        c=self.c.get()
        w=self.w.get()
        y=(a*np.exp(-c*x)*np.cos(w*x+b))
        return y
    def graficar(self,x1,x2,nfig):
        fig =plt.figure(nfig)
        plano= fig.gca()
        x = np.linspace(x1, x2, 500, endpoint=True)
        y = self.fsenosoidal(x)
        plano.plot(x, y,color=self.color)
        return(fig)    
    def eventos(self, comando:str):
        if (comando=="Graficar"):
            self.figura=self.graficar(self.x1.get(),self.x2.get(),self.figura.number)
            self.canvas.draw()
        if (comando=="Nueva Grafica"):
            self.figura.clear()
            self.figura=self.graficar(self.x1.get(),self.x2.get(),self.figura.number)
            self.canvas.draw()
        if (comando=="Color"):
            ((r,g,b),h) = ColorChooser.askcolor(master=self,title="Elige un color")
            self.lift()
            self.color_hexa=h
            self.color=(r/256,g/256,b/256)
            self.etiqueta_color.config(bg=self.color_hexa)
        
class PanelVentanas(tk.Frame):
    def __init__(self,ventana_padre):
        super().__init__(ventana_padre)
        self.ventana_padre=ventana_padre

        ttk.Label(self,text="Ventanas graficas 2D").grid(row=1,column=1)
          
        self.btn_lineal = ttk.Button(self, text="Lineales",command=lambda: self.eventos("Lineales"))
        self.btn_lineal.grid(row=2, column=1)
        self.btn_exponencial = ttk.Button(self, text="Exponenciales",command=lambda: self.eventos("Exponenciales"))
        self.btn_exponencial.grid(row=3, column=1)
        self.btn_senosoidal = ttk.Button(self, text="Senosoidales",command=lambda: self.eventos("Senosoidales"))
        self.btn_senosoidal.grid(row=4, column=1)
    def eventos(self,comando:str):
        if comando=="Lineales":
            self.dialogo=VentanaGraficasLineales(self)
            self.dialogo.title("Graficas Funciones Lineales")
            self.wait_window(self.dialogo)
        if comando=="Exponenciales":
            self.dialogo=VentanaGraficasExponenciales(self)
            self.dialogo.title("Graficas Funciones Exponenciales")
            self.wait_window(self.dialogo)
        if comando=="Senosoidales":
            self.dialogo=VentanaGraficasSenosoidales(self)
            self.dialogo.title("Graficas Funciones Senosoidales")
            self.wait_window(self.dialogo)
        if comando=="Error":
            MessageBox.showerror("Error", "Mensaje Error") 
            self.caja2.insert(tk.INSERT,"Muestra mensaje de error\n")        
        
        
class Applicacion(tk.Frame):
    def __init__(self, ventana_padre):
        super().__init__(ventana_padre)
        self.ventana_padre=ventana_padre
        self.panel_imagen=PanelImagen(self)
        self.panel_imagen.pack(fill="both")

        
        self.pestanias = ttk.Notebook(self)
        self.pestanias.pack(fill="both",expand="yes",padx=10, pady=10)

        self.panel_texto=PanelCajaTexto(self.pestanias)
        self.panel_texto.pack(side="top", anchor="w",padx=10, pady=10)

        self.panel_combo=PanelCombo(self.pestanias)
        self.panel_combo.pack(side="top", anchor="w",padx=10, pady=10)

        self.panel_radio_botones=PanelRadioBotones(self.pestanias)
        self.panel_radio_botones.pack(side="top", anchor="w",padx=10, pady=10)

        self.panel_barra_Herramientas=PanelBarraHerramientas(self.pestanias)
        self.panel_barra_Herramientas.pack(side="top", anchor="w",padx=10, pady=10)

        self.panel_menu=PanelMenu(self.ventana_padre)
        
        self.panel_dialogos=PanelDialogos(self.pestanias)
        self.panel_dialogos.pack(side="top", anchor="w",padx=10, pady=10)

        self.panel_chequeo=PanelCajasChequeo(self.pestanias)
        self.panel_chequeo.pack(side="top", anchor="w",padx=10, pady=10)

        self.panel_ventanas=PanelVentanas(self.pestanias)
        self.panel_ventanas.pack(side="top", anchor="w",padx=10, pady=10)
        
        self.pestanias.add(self.panel_texto, text="Cajas de texto")
        self.pestanias.add(self.panel_combo, text="Combos")
        self.pestanias.add(self.panel_radio_botones, text="Radio Botones")
        self.pestanias.add(self.panel_chequeo, text="Cajas de Chequeo")
        self.pestanias.add(self.panel_barra_Herramientas, text="Barra Herramientas")
        self.pestanias.add(self.panel_dialogos, text="Dialogos")
        self.pestanias.add(self.panel_ventanas, text="Ventanas")
        
        self.pack(fill="both",expand="yes",padx=10, pady=10)
       

main_window = tk.Tk()
app = Applicacion(main_window)
app.mainloop()
