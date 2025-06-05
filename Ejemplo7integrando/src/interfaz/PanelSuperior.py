import tkinter as tk
from PIL import Image, ImageTk
import os

class PanelSuperior(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg='lightblue', height=100)
        self.pack_propagate(False)

        # Ruta absoluta a la imagen (por ejemplo: data/encabezado.png)
        ruta_base = os.path.dirname(os.path.abspath(__file__))
        ruta_img = os.path.join(ruta_base, "..", "..", "data", "encabezado1.png")

        # Cargar imagen
        imagen = Image.open(ruta_img)
        imagen = imagen.resize((500, 200))  # Ajusta el tamaño si es necesario
        self.imgEncabezado = ImageTk.PhotoImage(imagen)  # guardar en self para evitar recolección de basura

        # Mostrar imagen como encabezado
        self.label_img = tk.Label(self, image=self.imgEncabezado, bg='lightblue')
        self.label_img.pack()

        # Texto opcional debajo de la imagen
        label_text = tk.Label(self, text="Perfil de Estudiante", font=("Arial", 18, "bold"), bg='lightblue')
        label_text.pack(pady=5)
