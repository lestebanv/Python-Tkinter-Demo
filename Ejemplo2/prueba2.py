import tkinter as tk
import os

class PanelDatos(tk.LabelFrame):
    def __init__(self,panelpadre):
        super().__init__(panelpadre,text="Datos")
        tk.Label(self,text="Nombre:").grid(row=1,column=1,sticky="e")
        tk.Label(self,text="Apellido:").grid(row=2,column=1,sticky="e")
        tk.Label(self,text="Genero:").grid(row=3,column=1,sticky="e")
        tk.Label(self,text="Fecha Nacimiento:").grid(row=4,column=1,sticky="e")
        tk.Label(self,text="Fecha Ingreso:").grid(row=5,column=1,sticky="e")
        tk.Label(self,text="Salario:").grid(row=6,column=1,sticky="e")

        tk.Label(self,text="...",width=30).grid(row=1,column=2)
        tk.Label(self,text="...",width=30).grid(row=2,column=2)
        tk.Label(self,text="...",width=30).grid(row=3,column=2)
        tk.Label(self,text="...",width=30).grid(row=4,column=2)
        tk.Label(self,text="...",width=30).grid(row=5,column=2)
        tk.Label(self,text="...",width=30).grid(row=6,column=2)

        ruta=os.path.dirname(os.path.abspath(__file__))
        cadena=os.path.join(ruta,"imagenes","empleado1.png")
        self.foto=tk.PhotoImage(file=cadena)
        tk.Label(self,image=self.foto).grid(row=1,column=3,rowspan=7)

        tk.Button(self,text="Modificar Salario").grid(row=7,column=2)

class PanelCalculos(tk.LabelFrame):
    def __init__(self,panelpadre):
        super().__init__(panelpadre,text="Cálculos")
        tk.Button(self,text="Calcular Edad",width=40).grid(row=1,column=1)
        tk.Button(self,text="Calcular Antiguedad",width=40).grid(row=2,column=1)
        tk.Button(self,text="Calcular Prestaciones",width=40).grid(row=3,column=1)

        tk.Entry(self,width=40).grid(row=1,column=2)
        tk.Entry(self,width=40).grid(row=2,column=2)
        tk.Entry(self,width=40).grid(row=3,column=2)

class PanelOpciones(tk.LabelFrame):
    def __init__(self,panelpadre):
        super().__init__(panelpadre,text="Opciones")
        tk.Button(self,text="Cambiar Empleado",width=25).grid(row=1,column=1)
        tk.Button(self,text="Opción 1",width=25).grid(row=1,column=2)
        tk.Button(self,text="Opción 2",width=25).grid(row=1,column=3)

class InterfazEmpleado(tk.Tk):
    def __init__(self,tituloventana):
        super().__init__()
        self.title(tituloventana)
        self.frame=tk.Frame()
        self.frame.grid(row=1,column=1)
        #imagen de cabecera
        ruta=os.path.dirname(os.path.abspath(__file__))
        cadena=os.path.join(ruta,"imagenes","Encabezado.png")
        self.imagen_cabecera=tk.PhotoImage(file=cadena)
        tk.Label(self.frame,image=self.imagen_cabecera).grid(row=1,column=1)
        #panel datos
        PanelDatos(self.frame).grid(row=2,column=1,sticky="nsew")
        #panel Calculos
        PanelCalculos(self.frame).grid(row=3,column=1,sticky="nsew")
        #panel Opciones
        PanelOpciones(self.frame).grid(row=4,column=1,sticky="nsew")
        
        
#codigo de arranque
x=InterfazEmpleado("Sistema de un Empleado")
x.mainloop()
