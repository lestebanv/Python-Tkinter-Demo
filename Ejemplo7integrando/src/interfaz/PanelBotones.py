from tkinter import filedialog, messagebox
from tkinter import PhotoImage
import tkinter as tk
from PIL import Image, ImageTk
import os

from src.interfaz.VentanaExtra import VentanaExtra

class PanelBotones(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg='lightgray')
        self.padre = master
        self.crear_botones()

    def crear_botones(self):
        boton1 = tk.Button(self, text="Cambiar encabezado", command=self.cambiar_encabezado)
        boton1.pack(side="left", padx=10, pady=10)

        boton2 = tk.Button(self, text="Cambiar datos del estudiante", command=self.cambiar_estudiante)
        boton2.pack(side="left", padx=10, pady=10)

        boton3 = tk.Button(self, text="Opción 3")
        boton3.pack(side="left", padx=10, pady=10)

    def cambiar_encabezado(self):
        ruta = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.gif")]
        )
        if ruta:
            try:
                nueva_imagen = Image.open(ruta)
                nueva_imagen = nueva_imagen.resize((600, 100))  # Ajuste opcional
                icono = ImageTk.PhotoImage(nueva_imagen)
                self.padre.pSuperior.label_img.configure(image=icono)
                self.padre.pSuperior.label_img.image = icono  # Referencia necesaria
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

    def cambiar_estudiante(self):
        ventana = VentanaExtra(self.padre)
        ventana.grab_set()
