import tkinter as tk
from tkinter import messagebox
"""
Panel Superior
   atributos:
           padre:Frame
"""
class PanelSuperior(tk.Frame):
    def __init__(self,panelPadre):
        super().__init__(panelPadre)
        self.padre=panelPadre
        self.config(width=480,height=100,bg="green")


"""
PanelDatos
   atributos
       padre:Frame
       nombre:CajaTexto
       descripcion:Texto
       boton:Boton
"""
class PanelDatos(tk.Frame):
    def __init__(self,panelpadre):
        super().__init__(panelpadre)
        self.padre=panelpadre

        tk.Label(self,text="Nombre...").grid(row=1,column=1)
        
        self.nombre=tk.Entry(self)
        self.nombre.config(width=30)
        self.nombre.grid(row=1,column=2)

        tk.Label(self,text="Apellido...").grid(row=2,column=1)
        self.apellido=tk.Entry(self)
        self.apellido.config(width=30)
        self.apellido.grid(row=2,column=2)

        tk.Label(self,text="Descripcion...").grid(row=3,column=1)
        self.descripcion=tk.Text(self)
        self.descripcion.config(width=30, height=10)
        self.descripcion.config(font=("Consolas",12), selectbackground="red", padx=5, pady=5)
        self.descripcion.grid(row=3,column=2, columnspan=3)
        
        self.boton=tk.Button(self, text="opcion 1",command=lambda: self.eventos("saludar"))
        self.boton.grid(row=4, column=1)
    def eventos(self,grito):
        if grito=="saludar":
            messagebox.showinfo("Título de la ventana", "Hola")

        
"""
Interfaz Ejemplo
   atributos
       panelPrincipal:Frame
       panelSup:PanelSuperior
       panelD:PanelDatos
"""    
class InterfazEjemplo(tk.Tk):
    def __init__(self, titulo):
        super().__init__()
        self.panelPrincipal=tk.Frame(self)
        self.panelPrincipal.config(bg="red")
        self.panelPrincipal.pack(fill="both",expand="yes",padx=10, pady=10)

        self.panelSup=PanelSuperior(self.panelPrincipal)
        self.panelSup.pack()

        self.panelD=PanelDatos(self.panelPrincipal)
        self.panelD.pack()
        #print(self.panel1.config())

#codigo de prueba
app = InterfazEjemplo("Demo tkinter")
app.mainloop()
