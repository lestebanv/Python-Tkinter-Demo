import tkinter as tk
import os
from tkinter.simpledialog import askstring

class PanelInformacion(tk.LabelFrame):
    def __init__(self,panelpadre):
        super().__init__(panelpadre,text="Información")
        tk.Label(self,text="Carga total:",width=57,anchor="w").grid(row=1,column=1,sticky="w")
        tk.Label(self,text="Carga promedio:",width=57,anchor="w").grid(row=2,column=1,sticky="w")

        tk.Entry(self,width=57,text="100 Kg.",state='disabled').grid(row=1,column=2)

        self.txtcp = tk.Entry(self)
        self.txtcp.insert(0,"25.0 Kg.")
        self.txtcp.config(width=57)
        self.txtcp.grid(row=2,column=2)      
       
class PanelCamion(tk.LabelFrame):
    def __init__(self,panelpadre):
        super().__init__(panelpadre)
        tk.Label(self,text="Matricula:",font="Verdana 10 bold").grid(row=1,column=2,sticky="e")
        tk.Label(self,text="Capacidad:",font="Verdana 10 bold").grid(row=2,column=2,sticky="e")
        tk.Label(self,text="Consumo:",font="Verdana 10 bold").grid(row=3,column=2,sticky="e")
        tk.Label(self,text="Carga Actual:",font="Verdana 10 bold").grid(row=4,column=2,sticky="e")

        tk.Entry(self,width=30).grid(row=1,column=3,sticky="e")
        tk.Entry(self,width=30).grid(row=2,column=3,sticky="e")
        tk.Entry(self,width=30).grid(row=3,column=3,sticky="e")
        self.carga_actual = tk.Entry(self,width=30,state="disable")
        self.carga_actual.grid(row=4,column=3,sticky="e")


        self.btn_cargar=tk.Button(self,text="Cargar",command=lambda: self.accion("cargar") ,width=20)
        self.btn_cargar.grid(row=5,column=2,sticky="e")
        
        self.btn_descargar=tk.Button(self,text="Descargar",command=lambda: self.accion("descargar"),state="disable",width=20)
        self.btn_descargar.grid(row=5,column=3,sticky="e")


        #Imangen del cambion vacio
        file_path = os.path.dirname(os.path.abspath(__file__))
        ruta_vacio = os.path.join(file_path, 'imagenes', "camionVacio.png")
        ruta_cargado = os.path.join(file_path, 'imagenes', "camionCargado.png")
        self.camion_vacio=tk.PhotoImage(file=ruta_vacio)
        self.camion_cargado=tk.PhotoImage(file=ruta_cargado)
        
        self.imagen_camion=tk.Label(self,image=self.camion_vacio)
        self.imagen_camion.grid(row=1,column=1,rowspan=4)
        
    def accion(self,comando:str):
        if(comando=="cargar"):
            capacidad=askstring("Sobre este camion", "Peso a cargar..")
            self.carga_actual.config(state="normal")
            self.carga_actual.insert(0,capacidad +"K.g")
            self.carga_actual.config(state="disable")
            self.btn_descargar.config(state="normal")
            self.btn_cargar.config(state="disable")
            self.imagen_camion.config(image=self.camion_cargado)
        if(comando=="descargar"):
            self.carga_actual.config(state="normal")
            self.carga_actual.delete(0,tk.END)
            self.carga_actual.config(state="disable")
            self.btn_descargar.config(state="disable")
            self.btn_cargar.config(state="normal")
            self.imagen_camion.config(image=self.camion_vacio)
            
            
            
            
        
        
class PanelCamiones(tk.Frame):
    def __init__(self,panelpadre):
        super().__init__(panelpadre)
        #para cada camion un PanelCamion
        self.camion1=PanelCamion(self).grid(row=1,column=1,padx=10,pady=10)
        self.camion2=PanelCamion(self).grid(row=1,column=2,padx=10,pady=10)
        self.camion3=PanelCamion(self).grid(row=2,column=1,padx=10,pady=10)
        self.camion4=PanelCamion(self).grid(row=2,column=2,padx=10,pady=10)
        
        
class PanelOpciones(tk.LabelFrame):
    def __init__(self,panelpadre):
        super().__init__(panelpadre,text="Opciones")
        tk.Button(self,text="Buscar mejor camión",width=52).grid(row=1,column=1,sticky="e")
        tk.Button(self,text="Capacidad total",width=52).grid(row=1,column=2,sticky="e")
        tk.Button(self,text="Opción 1",width=52).grid(row=2,column=1,sticky="e")
        tk.Button(self,text="Opción 2",width=52).grid(row=2,column=2,sticky="e")
        
        

class InterfazEmpresaTransporte(tk.Tk):
    def __init__(self, tituloventana):
        super().__init__()
        self.title(tituloventana)

        #Imangen de cabecera
        file_path = os.path.dirname(os.path.abspath(__file__))
        imagen_path = os.path.join(file_path, 'imagenes', "encabezado.png")
        self.imagen_cabecera=tk.PhotoImage(file=imagen_path) 
        tk.Label(self,image=self.imagen_cabecera).grid(row=1,column=1)

        #panel informacion     
        PanelInformacion(self).grid(row=2,column=1,sticky="nsew")

        #panel camiones
        PanelCamiones(self).grid(row=3,column=1,sticky="nsew")

        #panel opciones
        PanelOpciones(self).grid(row=4,column=1,sticky="nsew")


#codigo de prueba
app = InterfazEmpresaTransporte("Empresa de transporte")
app.mainloop()
