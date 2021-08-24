import tkinter as tk
import os


class PanelDatos(tk.LabelFrame):
   def __init__(self,panelpadre):
        super().__init__(panelpadre,text="Datos")
        tk.Label(self,text="Nombre:").grid(row=1,column=1,sticky="W")
        tk.Label(self,text="Apellido:").grid(row=2,column=1,sticky="W")
        tk.Label(self,text="Género:").grid(row=3,column=1,sticky="W")
        tk.Label(self,text="Fecha de Nacimiento:").grid(row=4,column=1,sticky="W")
        tk.Label(self,text="Fecha de Ingreso:").grid(row=5,column=1,sticky="W")
        tk.Label(self,text="Salario:").grid(row=6,column=1,sticky="W")

        
        tk.Entry(self).grid(row=1,column=2,sticky="W")
        tk.Entry(self).grid(row=2,column=2,sticky="W")
        tk.Entry(self).grid(row=3,column=2,sticky="W")
        tk.Entry(self).grid(row=4,column=2,sticky="W")
        tk.Entry(self).grid(row=5,column=2,sticky="W")
        tk.Entry(self).grid(row=6,column=2,sticky="W")
        
        tk.Button(self, text="Modificar Salario",command=lambda: self.eventos("Limpiar")).grid(row=7,column=2)
        
        #Foto del empleado
        file_path = os.path.dirname(os.path.abspath(__file__))
        imagen_path = os.path.join(file_path, 'imagenes', "empleado1.png")
        self.foto=tk.PhotoImage(file=imagen_path) 
        tk.Label(self,image=self.foto).grid(row=1,column=3,rowspan=7)
        
class PanelCalculos(tk.LabelFrame):
   def __init__(self,panelpadre):
        super().__init__(panelpadre,text="Cálculos")
        tk.Label(self,text="...").grid(row=1,column=2,sticky="w")
        tk.Label(self,text="...").grid(row=2,column=2,sticky="w")
        tk.Label(self,text="...").grid(row=3,column=2,sticky="w")       
        tk.Button(self, text="Calcular Edad",width=30,command=lambda: self.eventos("Limpiar")).grid(row=1,column=1,sticky="w")
        tk.Button(self, text="Calcular Antiguedad",width=30,command=lambda: self.eventos("Limpiar")).grid(row=2,column=1,sticky="w")
        tk.Button(self, text="Calcular Prestaciones",width=30,command=lambda: self.eventos("Limpiar")).grid(row=3,column=1,sticky="w")
        
class PanelOpciones(tk.LabelFrame):
   def __init__(self,panelpadre):
        super().__init__(panelpadre,text="Opciones")     
        tk.Button(self, text="Cambiar Empleado",width=25,command=lambda: self.eventos("Limpiar")).grid(row=1,column=1)
        tk.Button(self, text="Opcion1",width=25,command=lambda: self.eventos("Limpiar")).grid(row=1,column=2)
        tk.Button(self, text="Opcion2",width=25,command=lambda: self.eventos("Limpiar")).grid(row=1,column=3)
       
    
class InterfazEjemplo2(tk.Tk):

    def __init__(self, tituloventana):
        super().__init__()
        
        self.title(tituloventana)
        #creando el panel de la ventana principal
        self.frame=tk.Frame().grid(row=1,column=1,padx=10, pady=10)

        #Imangen de cabecera
        file_path = os.path.dirname(os.path.abspath(__file__))
        imagen_path = os.path.join(file_path, 'imagenes', "encabezado.png")
        self.imagen_cabecera=tk.PhotoImage(file=imagen_path) 
        tk.Label(self.frame,image=self.imagen_cabecera).grid(row=1,column=1)
        
        #panel datos     
        PanelDatos(self.frame).grid(row=2,column=1,sticky="nsew")
        #panel Calculos     
        PanelCalculos(self.frame).grid(row=3,column=1,sticky="nsew")
        #panel Calculos     
        PanelOpciones(self.frame).grid(row=4,column=1,sticky="nsew")

        
    

#codigo de prueba
app = InterfazEjemplo2("Sistemas de Un empleado")
app.mainloop()
