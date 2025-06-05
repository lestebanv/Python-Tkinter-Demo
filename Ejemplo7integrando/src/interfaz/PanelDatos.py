import os
import tkinter as tk
from PIL import Image, ImageTk

class PanelDatos(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")
        self.padre =master 

        self.config(padx=10, pady=10)
        self.crear_widgets()
        self.actualizar_etiquetas()

    def crear_widgets(self):
        # Imagen lateral
        try:
            ruta_base = os.path.dirname(os.path.abspath(__file__))
            ruta_icono = os.path.join(ruta_base, "..", "..", "data", "foto1.png")
            imagen = Image.open(ruta_icono)
            imagen = imagen.resize((150, 150))
            self.foto = ImageTk.PhotoImage(imagen)
        except Exception as e:
            print("No se pudo cargar la imagen de datos:", e)
            self.foto = None

        self.imagen_label = tk.Label(self, image=self.foto, bg="white")
        self.imagen_label.pack(side="left", padx=10)

        # Panel de etiquetas
        frame_etiquetas = tk.Frame(self, bg="white")
        frame_etiquetas.pack(side="left", fill="both", expand=True)

        self.etiqueta_nombre = tk.Label(frame_etiquetas, text="", anchor="w", bg="white")
        self.etiqueta_direccion = tk.Label(frame_etiquetas, text="", anchor="w", bg="white")
        self.etiqueta_telefono = tk.Label(frame_etiquetas, text="", anchor="w", bg="white")
        self.etiqueta_correo = tk.Label(frame_etiquetas, text="", anchor="w", bg="white")

        for widget in [
            self.etiqueta_nombre,
            self.etiqueta_direccion,
            self.etiqueta_telefono,
            self.etiqueta_correo,
        ]:
            widget.pack(fill="x", pady=5)

    def actualizar_etiquetas(self):
        est = self.padre.est
        self.etiqueta_nombre.config(text=f"Nombre: {est.nombre}")
        self.etiqueta_direccion.config(text=f"Dirección: {est.direccion}")
        self.etiqueta_telefono.config(text=f"Teléfono: {est.telefono}")
        self.etiqueta_correo.config(text=f"Correo: {est.correo}")
