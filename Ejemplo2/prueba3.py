import tkinter as tk
class InterfazEmpleado(tk.Tk):
    def __init__(self,tituloventana):
        super().__init__()
        self.title(tituloventana)
        self.frame=tk.Frame()
        #imagen de cabecera
        self.imagen_cabecera=tk.PhotoImage(file="C:\Users\USUSARIO\Desktop\programas\Tkinter\Python-Tkinter-Demo\Ejemplo2\imagenes\Encabezado.png")
        tk.Label(self.frame,image=self.imagen_cabecera).grid(row=1,column=1)
#codigo de arranque
x=InterfazEmpleado("Sistema de un Empleado")
x.mainloop()
