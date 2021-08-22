import tkinter as tk

class PanelSuperior(tk.Frame):
    padre=None
    def __init__(self,panelpadre):
        super().__init__(panelpadre)
        self.padre=panelpadre
        self.config(width=480,height=100,bg="green")

class PanelDatos(tk.Frame):
    padre=None
    nombre=None
    apellido=None
    descripcion=None
    boton=None
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
        
        self.boton=tk.Button(self, text="opcion 1",command=lambda: self.eventos("Limpiar"))
        self.boton.grid(row=4, column=1)

        
    
class InterfazEjemplo(tk.Tk):
    frame=None
    panel1=None
    paneldatos=None
    def __init__(self, titulo):
        super().__init__()
        self.frame=tk.Frame()
        self.frame.config(bg="red")
        self.frame.pack(fill="both",expand="yes",padx=10, pady=10)

        panel1=PanelSuperior(self.frame)
        panel1.pack()

        paneldatos=PanelDatos(self.frame)
        paneldatos.pack()
        #print(panel1.config())

#codigo de prueba
app = InterfazEjemplo("Demo tkinter")
app.mainloop()
