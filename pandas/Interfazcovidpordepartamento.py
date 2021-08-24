import tkinter as tk
from tkinter import ttk
import procesamiento as lib
from tkinter import filedialog as FileDialog
import os
import io

class PanelDatos(tk.LabelFrame):
    data_frame=None
    def __init__(self,panelpadre):
         super().__init__(panelpadre,text="Selección de Archivo de Datos")
         self.archivo=tk.StringVar();
         self.archivo.set("Aun sin seleccionar")
         self.descripcion=tk.StringVar();
         self.descripcion.set("Sin informacion")
         
         tk.Label(self,text="Archivo excel").grid(row=1,column=1,sticky="e")
         self.btn_seleccionar=tk.Button(self,text="Seleccionar",command=lambda: self.eventos("seleccionar"))
         self.btn_seleccionar.grid(row=1,column=2)
         self.ruta=tk.Entry(self,textvariable=self.archivo,width=80,state="disabled")
         self.ruta.grid(row=2,column=1,columnspan=3)
         tk.Label(self,text="Municipio...").grid(row=3,column=1,sticky="e")
         self.combo_municipio = ttk.Combobox(self,state="disable")
         self.combo_municipio["values"] = ["Pamplona", "Cucuta"]
         self.combo_municipio.grid(row=3,column=2)
         self.btn_analizar=tk.Button(self,text="Analizar",state="disable",command=lambda: self.eventos("analizar"))
         self.btn_analizar.grid(row=3,column=3)

         self.caja_info=tk.Text(self,width=80, height=10)
         self.caja_info.config(font=("Consolas",10), padx=5, pady=5)
         self.caja_info.grid(row=4,column=1, columnspan=3)
         
  
    def eventos(self,comando):
        if comando=="seleccionar":
            self.archivo.set(FileDialog.askopenfilename(title="Abrir un fichero"))
            if self.archivo.get()=="":
                self.archivo.set("Archivo no seleccionado")
            else:
                self.data_frame=lib.cargar_informacion(self.archivo.get())
                self.btn_seleccionar.config(state="disable")
                self.btn_analizar.config(state="active")
                self.combo_municipio["state"]="enabled"
                self.combo_municipio["values"]=lib.obtener_lista_municipios(self.data_frame)
        if comando=="analizar":
            self.data_frame_municipio=lib.filtrar_por_municipio(self.data_frame,self.combo_municipio.get())
            buffer = io.StringIO()
            self.data_frame_municipio.info(buf=buffer)
            cadena=buffer.getvalue()
            self.caja_info.delete("1.0","end")
            self.caja_info.insert(tk.INSERT,cadena)
            
                
            
            
        
         

class InterfazCovid(tk.Tk):
    def __init__(self,tituloventana:str):
        super().__init__()
        self.title(tituloventana)
        #creando el panel de la ventana principal
        self.frame=tk.Frame().grid(row=1,column=1,padx=10, pady=10)

        #Imangen de cabecera
        file_path = os.path.dirname(os.path.abspath(__file__))
        imagen_path = os.path.join(file_path, "data","imagenes", "softwarelibre.png")
        self.imagen_cabecera=tk.PhotoImage(file=imagen_path) 
        tk.Label(self.frame,image=self.imagen_cabecera).grid(row=1,column=1)
        #panel de datos
        PanelDatos(self.frame).grid(row=2,column=1)

#Codigo de arranque

app=InterfazCovid("Covid por departamento")
app.mainloop()
        
