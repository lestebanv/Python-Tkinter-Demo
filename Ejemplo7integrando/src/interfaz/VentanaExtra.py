import tkinter as tk
from tkinter import simpledialog

class VentanaExtra(tk.Toplevel):
    def __init__(self, ventana_padre):
        super().__init__(ventana_padre)
        self.padre = ventana_padre
        self.title("Cambiar datos del estudiante")
        self.geometry("400x200")
        self.resizable(False, False)
        self.crear_widgets()

    def crear_widgets(self):
        self.columnconfigure(1, weight=1)
        etiquetas = ["Nombre del estudiante","Telefono", "Dirección", "Correo"]
        self.entradas = {}

        i=0
        while(i<len(etiquetas)):
            texto=etiquetas[i]
            tk.Label(self, text=texto).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entrada = tk.Entry(self, width=30)
            entrada.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            self.entradas[texto] = entrada
            i=i+1            
        boton = tk.Button(self, text="Aceptar", command=self.accion_aceptar)
        boton.grid(row=4, column=0, columnspan=2, pady=10)

    def accion_aceptar(self):
        self.padre.est.nombre = self.entradas["Nombre del estudiante"].get()
        self.padre.est.direccion = self.entradas["Dirección"].get()
        self.padre.est.correo = self.entradas["Correo"].get()
        self.padre.est.telefono = self.entradas["Telefono"].get()
        self.padre.pDatos.actualizar_etiquetas()
        self.destroy()
