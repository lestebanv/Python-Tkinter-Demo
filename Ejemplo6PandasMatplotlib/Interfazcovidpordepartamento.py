import tkinter as tk
from tkinter import ttk
import procesamiento as lib

import os
import io
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class PanelDatos(tk.LabelFrame):
    data_frame=None
    data_frame_municipio=None
    figura=None
    ruta_archivo=None
    descripcion=None
    actual_municipio=None
    def __init__(self,panelpadre):
         super().__init__(panelpadre,text="Selección de Archivo de Datos")
         self.ruta_archivo=tk.StringVar(value="Aun sin seleccionar");
         self.actual_municipio=tk.StringVar(value="")
               
         
         self.ruta=tk.Entry(self,textvariable=self.ruta_archivo,width=80,state="disabled")
         self.ruta.grid(row=2,column=1,columnspan=3)

         tipo_letra="Arial 20 bold italic"
         tk.Label(self,textvariable=self.actual_municipio,font=tipo_letra).grid(row=4,column=1,sticky="e")


         self.descripcion=tk.StringVar();
         self.descripcion.set("Sin informacion")
         
         
         tk.Label(self,text="Archivo excel").grid(row=1,column=1,sticky="e")
         self.btn_seleccionar=tk.Button(self,text="Seleccionar",command=lambda: self.eventos("seleccionar"))
         self.btn_seleccionar.grid(row=1,column=2)
         
         
         tk.Label(self,text="Municipio...").grid(row=3,column=1,sticky="e")
         self.combo_municipio = ttk.Combobox(self,state="disable")
         self.combo_municipio["values"] = ["Pamplona", "Cucuta"]
         self.combo_municipio.grid(row=3,column=2)

         self.btn_analizar=tk.Button(self,text="Analizar",state="disable",command=lambda: self.eventos("analizar"))
         self.btn_analizar.grid(row=3,column=3)
         
         
         
         self.caja_info=tk.Text(self,width=70, height=10,bg="#d6d6d6", borderwidth=2, relief="solid")
         self.caja_info.config(font=("Consolas",8), padx=5, pady=5)
         self.caja_info.grid(row=5,column=1, columnspan=2)
         
         self.figura= Figure( figsize=(7, 3), dpi=80 )
         self.figura.clear()
         self.canvas = FigureCanvasTkAgg(self.figura, master=self)
         self.canvas.get_tk_widget().grid(row=6,column=1, columnspan=3,sticky="ewns")

         #panel ventanas con botones para acceder a otros tipos de graficos
         self.panel_v=PanelVentanas(self)
         self.panel_v.grid(row=5,column=3)
         self.panel_v.deshabilitar()
         
         

    def graficar_contagios(self):
        self.figura.clear()
        df=lib.agrupar_por_fecha(self.data_frame_municipio)
        lib.graficar(self.figura,df,"fecha reporte web","contagios","Contagios diarios Detectados","Fecha","Numero de Contagios")
        self.canvas.draw()
        
         
    def eventos(self,comando):
        if comando=="seleccionar":
            self.ruta_archivo.set(tk.filedialog.askopenfilename(title="Abrir un fichero"))
            if self.ruta_archivo.get()=="":
                self.ruta_archivo.set("No selecciono ningun archivo.. intentelo de nuevo")
            else:
                self.data_frame=lib.cargar_informacion(self.ruta_archivo.get())
                self.btn_seleccionar.config(state="disable")
                self.btn_analizar.config(state="active")
                self.combo_municipio["state"]="enabled"
                self.combo_municipio["values"]=lib.obtener_lista_municipios(self.data_frame)        
        if comando=="analizar":
            self.actual_municipio.set(self.combo_municipio.get())
            if(self.actual_municipio.get()!=""):
                self.data_frame_municipio=lib.filtrar_por_municipio(self.data_frame,self.actual_municipio.get())

                # redireccionar la salida estandar a un string
                buffer = io.StringIO()
                self.data_frame_municipio.info(buf=buffer)
                cadena=buffer.getvalue()
                self.caja_info.delete("1.0","end")
                self.caja_info.insert(tk.INSERT,cadena)

                #graficar en el canvas
                self.graficar_contagios()

                #habilitar subpanel
                self.panel_v.habilitar()
            
            


class PanelVentanas(tk.LabelFrame):
    def __init__(self,panelpadre):
         super().__init__(panelpadre,text="Otros graficos")
         self.panelpadre=panelpadre
         
         tk.Button(self,text="Contagios por edad",width=20,command=lambda: self.eventos("contagio edad")).grid(row=1,column=1)
         tk.Button(self,text="Muertes por edad",width=20,command=lambda: self.eventos("muerte edad")).grid(row=2,column=1)
         tk.Button(self,text="Contagio por genero",width=20,command=lambda: self.eventos("contagio genero")).grid(row=3,column=1)
         tk.Button(self,text="Muertes por genero",width=20,command=lambda: self.eventos("muerte genero")).grid(row=4,column=1)

    def deshabilitar(self):
        for x in self.winfo_children():
            x.configure(state='disable')

            
    def habilitar(self):
        for objeto in self.winfo_children():
            objeto.configure(state='normal')

    def eventos(self,comando):
        if comando=="contagio edad":
            figura=Figure( figsize=(7, 3), dpi=80 )
            plano=figura.gca()
            plano.set_title("Contagios por edad "+self.panelpadre.actual_municipio.get())
            plano.hist(self.panelpadre.data_frame_municipio["Edad"],10,alpha=1, edgecolor = 'black',  linewidth=1)

            ventana_emergente=VentanaGraficas(self,"Graficas Contagios por edad",figura)
            self.wait_window(ventana_emergente)

            
        if comando=="muerte edad":
            tmp_df=self.panelpadre.data_frame_municipio
            muertos_municipio=tmp_df[tmp_df["Fecha de muerte"].notnull()]

            figura=Figure( figsize=(7, 3), dpi=80 )
            plano=figura.gca()
            plano.set_title("Muertes por edad "+self.panelpadre.actual_municipio.get())
            plano.hist(muertos_municipio["Edad"],10,alpha=1, edgecolor = 'black',  linewidth=1)
            ventana_emergente=VentanaGraficas(self,"Graficas Muertes por edad",figura)
            self.wait_window(ventana_emergente)
            
        
        

#ventana
class VentanaGraficas(tk.Toplevel):
    def __init__(self,ventana_padre,titulo,figura):
        super().__init__(ventana_padre)
        self.title=titulo
        self.figura=figura
        self.canvas = FigureCanvasTkAgg(self.figura, master=self)
        self.canvas.get_tk_widget().grid(row=1,column=1)
        self.canvas.draw()
"""
        self.toolbar =  NavigationToolbar2Tk(self.canvas, self )
        self.toolbar.pack()
        self.toolbar.update()
"""         

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
        
